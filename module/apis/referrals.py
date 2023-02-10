import logging
from random import choice

import requests

from module.config import REFERRALS_HOST


class Referrals:

    def __get_referrals_response(self) -> requests.Response:
        response = None

        while response is None:
            try:
                response = requests.get(f'http://{REFERRALS_HOST}/referals')
                return response
            except Exception as e:
                logging.error(e)

    def get_referrals_json(self) -> dict:
        response: requests.Response = self.__get_referrals_response()
        json_response = response.json()
        return json_response


def get_random_project() -> str:
    refs = Referrals()
    refs_json = refs.get_referrals_json()
    seq = tuple(refs_json.keys())
    ref_name = choice(seq)
    return ref_name
