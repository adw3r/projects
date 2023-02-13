import abc
import logging
import re
from random import choice
from string import Template, digits, ascii_letters

import requests
from spintax import spintax

from module import config

pattern = re.compile('(?<=@).*(?=\.)')


def generate_text(length: int = 6):
    return ''.join([choice(ascii_letters + digits) for _ in range(length)])


class Text:
    def __init__(self, lang: str, link: str, project: str, text: str, spins: str):
        self.lang = lang
        self.link = link
        self.project = project
        self.text = text
        self.spins = spins

    def get_text(self, allow_stickers: bool = True, target: str = '') -> str:
        template = Template(spintax.spin(self.text))
        params = {'spins': self.spins, 'project': self.project, 'link': self.link}
        message = template.substitute(params)
        if not allow_stickers:
            message = message.replace('🔥', '')
            message = message.replace('➡️', '')
            message = message.replace('⬅️', '')
        return message

    def __get_target_domain(self, target: str = '') -> str:
        '''
        return domain of a target
        :param target:
        :return:
        '''

        value = pattern.findall(target)
        if value:
            return value[0]
        else:
            return ''

    @staticmethod
    def get_texts_from_api() -> dict:
        response = None

        while response is None:
            try:
                response = requests.get(f'http://{config.TEXTS_HOST}/')
                return response.json()
            except Exception as e:
                logging.error(e)
