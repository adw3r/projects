import logging

import requests

from module.config import LINKS_HOST


class LinkV2:
    endpoint = 'link_v2'

    def get_link(self, target_pool_name: str, referal_to_project: str) -> str:
        response = None
        params = {'targets_base': target_pool_name, 'project_name': referal_to_project}

        while response is None:
            try:
                response = requests.get(f'http://{LINKS_HOST}/{self.endpoint}', params=params)
                return response.text
            except Exception as err:
                logging.error(err)


class Link:
    endpoint = 'link'

    def get_link(self, target_pool_name: str, referal_to_project: str) -> str:
        response = None
        params = {'targets_base': target_pool_name, 'project_name': referal_to_project}

        while response is None:
            try:
                response = requests.get(f'http://{LINKS_HOST}/{self.endpoint}', params=params)
                return response.text
            except Exception as err:
                logging.error(err)
