import logging

import requests

from module.config import LINKS_HOST


class LinkBase:
    endpoint = None

    def get_link(self, target_pool_name: str, referal_to_project: str) -> str:
        response = None
        params = {'targets_base': target_pool_name, 'project_name': referal_to_project}
        retries = 3
        timeout = 10

        while retries > 0 and response is None:
            try:
                response = requests.get(f'http://{LINKS_HOST}/{self.endpoint}', params=params, timeout=timeout)
                response.raise_for_status()
                return response.text
            except requests.exceptions.RequestException as err:
                logging.error(f'Error fetching link: {err}')
                retries -= 1

        raise Exception('Failed to fetch link')


class LinkV2(LinkBase):
    endpoint = 'link_v2'


class Link(LinkBase):
    endpoint = 'link'
