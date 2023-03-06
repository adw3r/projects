from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'www.aceprimaresources.com.my',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.aceprimaresources.com.my',
    'pragma': 'no-cache',
    'referer': 'https://www.aceprimaresources.com.my/contact.php',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

s = 'OK'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            'name': 'test',
            'email': target,
            'subject': 'test',
            'message': text[:120].replace(self.promo_link, 'https://telegra.ph/test-03-02-228'),
            'email_copy': '1',
        }
        response = requests.post('https://www.aceprimaresources.com.my/processing/contact_process.php', headers=headers,
                                 data=data)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
