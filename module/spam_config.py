import json
import logging
from pathlib import Path

from module.apis.captcha_solvers import CapMonsterSolver
from module.apis.links import Link
from module.apis.project_controller import ProjectControllerOnRedis, ProjectController
from module.apis.proxies import ProxyServerPool
from module.apis.referrals import get_random_project, Referrals
from module.apis.targets import get_random_target_pool, TargetServerPool
from module.apis.texts import Text
from module.config import CONFIGS_FOLDER, PROXIES, LOGGING_LEVEL

LINK = Link()
solver = CapMonsterSolver()
referrals = Referrals()


def get_logger(project_name, *args):
    info = ' '.join(args)
    logger = logging.getLogger(project_name)
    logging.basicConfig(format=f'%(name)s {info} %(asctime)s: %(message)s')
    logger.setLevel(LOGGING_LEVEL)
    return logger


class SpamConfig:
    project_name: str
    success_message: str
    ref_name: str
    proxy_pool_name: str
    target_pool_name: str
    promo_link: str
    lang: str
    text: str
    spins: str

    text_instance: Text
    proxy_instance: ProxyServerPool
    target_instance: TargetServerPool
    captcha_solver = solver
    project_controller: ProjectController

    def __init__(self,
                 project_name: str,
                 success_message: str = '',
                 target_pool_name: str = '',
                 ref_name: str = '',
                 proxy_pool_name: str = ''):
        self.project_name = project_name
        if self.__path_to_config.exists() and 'scratch' not in project_name:
            self.__load_config()
            self.__init_from_config()
        else:
            self.__init_from_apis(proxy_pool_name, ref_name, success_message, target_pool_name)
            if 'scratch' not in project_name:
                self.__dump_config()
        self.text_instance = Text(self.lang, self.promo_link, self.ref_name, self.text, self.spins)
        self.proxy_instance = ProxyServerPool(self.proxy_pool_name)
        self.target_instance = TargetServerPool(self.target_pool_name)
        self.project_controller = ProjectControllerOnRedis(
            name=self.project_name,
            project_name=self.ref_name,
            prom_link=self.promo_link,
            targets_base=self.target_pool_name
        )
        self.__create_logger()
        self.logger.info('Config initialized')

    @property
    def __path_to_config(self):
        return Path(CONFIGS_FOLDER, f'{self.project_name}.json')

    def __init_from_apis(self, proxy_pool_name, ref_name, success_message, target_pool_name):
        self.success_message = success_message
        self.ref_name: str = ref_name if ref_name else get_random_project()
        self.proxy_pool_name: str = proxy_pool_name if proxy_pool_name else PROXIES
        self.target_pool_name: str = target_pool_name if target_pool_name else get_random_target_pool()
        self.promo_link: str = LINK.get_link(self.target_pool_name, self.ref_name)
        self.lang: str = TargetServerPool.get_targets_json().get(self.target_pool_name).get('lang')
        self.text: str = Text.get_texts_from_api().get(self.lang)
        self.spins: str = referrals.get_referrals_json().get(self.ref_name).get('spins')

    def __to_dict(self):
        result = dict(
            project_name=self.project_name,
            success_message=self.success_message,
            ref_name=self.ref_name,
            proxy_pool_name=self.proxy_pool_name,
            target_pool_name=self.target_pool_name,
            link=self.promo_link,
            lang=self.lang,
            text=self.text,
            spins=self.spins
        )
        return result

    def __create_logger(self):
        self.logger = get_logger(
            self.project_name,
            self.promo_link,
            self.ref_name,
            self.target_pool_name,
            self.lang,
            self.proxy_pool_name
        )

    def __init_from_config(self):
        self.success_message: str = self.__config_file['success_message']
        self.text = self.__config_file['text']
        self.spins = self.__config_file['spins']
        self.lang = self.__config_file['lang']
        self.promo_link = self.__config_file['link']
        self.target_pool_name = self.__config_file['target_pool_name']
        self.proxy_pool_name = self.__config_file['proxy_pool_name']
        self.ref_name = self.__config_file['ref_name']

    def __load_config(self):
        with open(self.__path_to_config) as file:
            self.__config_file = json.load(file)

    def __dump_config(self):
        to_dict = self.__to_dict()
        with open(Path(CONFIGS_FOLDER, f'{self.project_name}.json'), 'w') as file:
            json.dump(to_dict, file)
