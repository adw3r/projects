import abc
import datetime
import json
import logging
import pathlib
import tempfile
from typing import NoReturn

import redis
import requests

from module import config

STATUS_EXPIRATION_LIMIT_IN_SEC = 30
REDIS_CLI = redis.Redis()


class ProjectController(abc.ABC):

    def __repr__(self):
        return self.project_name

    def __init__(self, name: str, prom_link: str, project_name: str, targets_base: str):
        self.name = name
        self.prom_link = prom_link
        self.project_name = project_name
        self.targets_base = targets_base

    @abc.abstractmethod
    def send_count(self, count) -> int:
        ...

    @abc.abstractmethod
    def get_status(self) -> bool:
        ...

    @abc.abstractmethod
    def retrieve_attached_link(self):
        ...


class ProjectServerController(ProjectController):
    __url = config.URL

    def send_count(self, count) -> int:
        response = None

        params = {'key': config.ZENNO_KEY, 'project': self.name, 'count': count}
        while type(response) is not requests.Response:
            try:
                response = requests.get(self.__url, params=params)
            except Exception as err:
                logging.error(err)
            else:
                return response.status_code

    def retrieve_attached_link(self) -> str | None:
        response = None

        params = {'key': config.ZENNO_KEY, 'getlink': '1', 'project': self.name}
        while type(response) is not requests.Response:
            try:
                resp = requests.get(self.__url, params=params)
            except Exception as error:
                logging.error(error)
            else:
                content = resp.content.decode()
                if 'Undefined variable' in content:
                    return None
                else:
                    return content

    def get_status(self) -> bool:
        if not self.name:
            return False

        params = {
            'key': config.ZENNO_KEY,
            'iswork': '1',
            'project': self.name,
            'prom_link': self.prom_link.removeprefix('https://'),
            'project_name': self.project_name,
            'targets_base': self.targets_base
        }
        response = None

        while not response:
            try:
                resp = requests.get(self.__url, params=params)
                cont = resp.text
                if cont == '1':
                    return True
                else:
                    return False
            except Exception as error:
                logging.error(error)


def _dump_json(file_path: pathlib.Path, status: dict) -> NoReturn:
    with open(file_path, 'w') as file:
        json.dump(status, file, default=str)


def _load_json(file_path: pathlib.Path) -> dict:
    with open(file_path) as file:
        result = json.load(file)
        return result


def get_current_time():
    return str(datetime.datetime.now())


class ProjectServerControllerCached(ProjectServerController):

    def __init__(self, name: str, prom_link: str, project_name: str, targets_base: str):
        super().__init__(name, prom_link, project_name, targets_base)
        self.cached_status_file = pathlib.Path(tempfile.mktemp(suffix='.json', prefix=self.name))
        self._dump_status()

    def _dump_status(self, status: bool | None = None, timestamp: str | datetime.datetime = get_current_time()):
        _dump_json(self.cached_status_file, {'status': status, 'timestamp': timestamp})

    def _load_status(self) -> dict:
        try:
            json = _load_json(self.cached_status_file)
            return json
        except Exception as error:
            print(error)
            return {'status': None, 'timestamp': get_current_time()}

    def _check_status_is_not_expired(self, timestamp) -> bool:
        if not timestamp:
            return False
        timestamp = datetime.datetime.fromisoformat(timestamp)
        check_status = datetime.datetime.now() < timestamp + datetime.timedelta(seconds=STATUS_EXPIRATION_LIMIT_IN_SEC)
        return check_status

    def get_status(self) -> bool:
        if not self.name:
            return False
        cached_status_dict: dict = self._load_status()
        status: bool = cached_status_dict.get('status')
        timestamp: str = cached_status_dict.get('timestamp')

        expired: bool = self._check_status_is_not_expired(timestamp)
        if status is None or not expired:
            status: bool = super().get_status()
            self._dump_status(status)
            return status
        else:
            return status


class ProjectControllerOnRedis(ProjectServerController):  # todo tests
    def __init__(self, name: str, prom_link: str, project_name: str, targets_base: str):
        super().__init__(name, prom_link, project_name, targets_base)
        super().get_status()

    def _dump_status(self, status: bool):
        REDIS_CLI.set(self.name, int(status), ex=STATUS_EXPIRATION_LIMIT_IN_SEC)

    def _load_status(self) -> bool | None:
        result = REDIS_CLI.get(self.name)
        if result is None:
            return result
        else:
            return bool(result)

    def get_status(self) -> bool:
        if not self.name:
            return False

        status: bool | None = self._load_status()

        if status is None:
            status: bool = super().get_status()
            self._dump_status(status)
            return status
        else:
            return status
