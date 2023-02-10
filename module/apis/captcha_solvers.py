import logging
from time import sleep

import requests

from module import config


class Solver:

    def solve(self, *args, **kwargs) -> str | None:
        ...


class CapMonsterSolver(Solver):

    def solve(self, googlekey: str, pageurl: str, time_limit: int = 30, version: str = 'v2') -> str | None:
        request: str = self._send_request(googlekey=googlekey, pageurl=pageurl, version=version).text
        print(request)
        if 'OK' not in request:
            return
        status, request_id = request.split('|')
        request: str = self._await_for_result(request_id, time_limit=time_limit)
        if 'OK' in request:
            status, captcha_answer = request.split('|')
            return captcha_answer
        else:
            print(request)
            return

    def _send_request(self, googlekey: str, pageurl: str, version: str = 'v2') -> requests.Response:
        params = {
            'method': 'userrecaptcha',
            'soft_id': '19',
            'version': version,
            'pageurl': pageurl,
            'googlekey': googlekey
        }
        if version == 'v3':
            params['action'] = 'verify'
            params['min_score'] = '0.3'
        response = requests.get(f'http://{config.CAPMONSTER_HOST}/in.php', params=params)
        return response

    def _check_request(self, request_id: str) -> requests.Response:
        params = {
            'action': 'get',
            'id': request_id
        }
        response = requests.get(f'http://{config.CAPMONSTER_HOST}/res.php', params=params)
        return response

    def _await_for_result(self, request_id: str, time_limit: int) -> str:
        for _ in range(time_limit):
            try:
                res = self._check_request(request_id)
                result = res.text
                match result:
                    case 'CAPCHA_NOT_READY':
                        sleep(1)
                    case _:
                        return result
            except Exception as error:
                logging.exception(error)
                return ''
        return ''
