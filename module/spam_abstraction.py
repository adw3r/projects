import abc
from threading import Thread
from time import sleep
from typing import NoReturn

import requests

from module import config
from module.spam_config import SpamConfig

SLEEP_TIMER = 60


class Spam(SpamConfig):
    attempts = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def solve_captcha(self, pageurl: str, googlekey: str, version: str = 'v2', time_limit: int = 30):
        answer = self.captcha_solver.solve(
            googlekey=googlekey, pageurl=pageurl, time_limit=time_limit,
            version=version
        )
        return answer

    def get_text(self, allow_stickers: bool = True, target: str = ''):
        text = self.text_instance.get_text(allow_stickers=allow_stickers, target=target)
        return text

    def get_target(self) -> str:
        return self.target_instance.pop()

    def get_proxies(self):
        proxy = self.proxy_instance.pop()
        proxies = {'http': proxy, 'https': proxy}
        return proxies

    @abc.abstractmethod
    def post(self, target: str) -> requests.Response | None:
        ...

    def send_post(self, target: str = config.TEST_TARGET) -> bool:
        response: requests.Response | None = self.__try_to_post(target=target)
        result: bool = self.check_success(response)
        self.logger.info(f'{result} {target}')
        return result

    def check_success(self, response: requests.Response | None) -> bool:
        if not response:
            return False
        result = self.success_message in response.text
        return result

    def main(self) -> bool:
        get_controller_status = self.project_controller.get_status()
        if not get_controller_status:
            self.logger.info(f'controller status is %s' % get_controller_status)
            return False
        send_count = 0
        for _ in range(self.attempts):
            target = self.get_target()
            send_count += int(self.send_post(target))
        self.project_controller.send_count(send_count)
        return True

    def run_concurrently(self, threads_amount: int = int(config.THREADS_LIMIT)) -> NoReturn:
        if config.START:
            for _ in range(threads_amount):
                Thread(target=self.__infinite_main).start()

    def __try_to_post(self, target: str) -> requests.Response | None:
        response = None
        for _ in range(10):
            try:
                response: requests.Response | None = self.post(target=target)
            except Exception as e:
                print(e)
            else:
                break
        return response

    def __infinite_main(self) -> NoReturn:
        while True:
            success: bool = self.main()
            if success:
                continue
            else:
                sleep(SLEEP_TIMER)
