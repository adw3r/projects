from concurrent.futures import ThreadPoolExecutor
from os.path import basename

import requests

from module import spam_abstraction
from module.apis import texts

googlekey = '6LcPudEjAAAAAHiEiPG17P7u3yFumpmj60UjLA9U'
pageurl = 'https://app.txtwizard.com/registration'
cookies = {
    'PHPSESSID': '3ku46r1ecjspitvilvrk1nr8kq',
}

headers = {
    'authority': 'app.txtwizard.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=3ku46r1ecjspitvilvrk1nr8kq',
    'origin': 'https://app.txtwizard.com',
    'referer': 'https://app.txtwizard.com/registration',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


class ConcreteSpam(spam_abstraction.Spam):

    def post(self, target) -> requests.Response | None:
        captcha = self.solve_captcha(pageurl=pageurl, googlekey=googlekey, version='v2')
        if not captcha:
            return
        data = {
            'name': self.get_text(target=target, allow_stickers=False),
            'email': target,
            'password': texts.generate_text(12),
            'g-recaptcha-response': captcha,
        }

        for _ in range(20):
            try:
                response = requests.post(pageurl, cookies=cookies, headers=headers, data=data,
                                         proxies=self.get_proxies(),
                                         timeout=10)
                return response
            except Exception as e:
                print(e)
        return


def main():
    s = 'Please enter your phone number.'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    iterables = [f'wezxasqw+{texts.generate_text(6)}@gmail.com' for _ in range(1)]
    with ThreadPoolExecutor() as worker:
        if any(worker.map(spam.send_post, iterables)):
            spam.run_concurrently()


if __name__ == '__main__':
    main()
