import logging
from random import choice

import requests

from module import config
from module.apis.pools import Pool


class TargetServerPool(Pool):

    @staticmethod
    def get_targets_json() -> dict:
        response = None
        while not response:
            try:
                response = requests.get(f'http://{config.TARGETS_HOST}/targets/')
                content = response.json()
                return content
            except Exception as error:
                logging.error(error)

    def get_pool_json(self) -> dict:
        response = None
        url = f'http://{config.TARGETS_HOST}/targets/{self.pool_name}'
        while not response:
            try:
                response = requests.get(url)
                content = response.json()
                return content
            except Exception as error:
                logging.error(error)

    def get_pool(self) -> str:
        response = None
        params = {'method': 'pool'}
        url = f'http://{config.TARGETS_HOST}/targets/{self.pool_name}'
        while not response:
            try:
                response = requests.get(url, params=params)
                content = response.text
                return content
            except Exception as error:
                logging.error(error)

    def pop(self) -> str:
        response = None
        params = {'method': 'pop'}
        url = f'http://{config.TARGETS_HOST}/targets/{self.pool_name}'
        while not response:
            try:
                response = requests.get(url, params=params)
                content = response.content.decode('latin-1')
                return content
            except Exception as err:
                logging.error(err)


def get_random_target_pool() -> str:
    keys = tuple(TargetServerPool.get_targets_json().keys())
    target_pool = choice(keys)
    return target_pool
