import logging
from typing import NoReturn

import requests

from module import config
from module.apis.pools import Pool


class ProxyServerPool(Pool):

    def __init__(self, pool_name: str):
        super().__init__(pool_name)

    def pop(self) -> str:
        if len(self) == 0:
            self.get_pool()
        value = self.pool.pop()
        return value

    def get_pool(self) -> NoReturn:
        response = None
        url = f'http://{config.PROXIES_HOST}/proxies/{self.pool_name}?method=pool'
        while type(response) is not requests.Response:
            try:
                response = requests.get(url, timeout=10)
                content = response.content.decode().split('\n')
                self.pool = content
                return content
            except Exception as error:
                logging.error(error)
