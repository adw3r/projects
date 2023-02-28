import logging

import requests

from module.config import LINKS_HOST


class LinkBase:
    endpoint = None

    def get_link(self, target_pool_name: str, referal_to_project: str, donor: str) -> str:
        params = {'targets_base': target_pool_name, 'project_name': referal_to_project, 'donor': donor}

        try:
            response = requests.get(f'http://{LINKS_HOST}/{self.endpoint}', params=params)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as err:
            logging.error(f'Error fetching link: {err}')
            raise Exception(f'Error fetching link from API {err}')


class LinkV2(LinkBase):
    endpoint = 'link_v2'


class Link(LinkBase):
    endpoint = 'link'
