from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'd35ab9bec77bfcf44addbc0b8b139d1a',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'http://www.webcorpinfo.com',
    'Referer': 'http://www.webcorpinfo.com/NL/contactform.htm',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'connection': 'keep-alive'
}

s = 'Thank you'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            'first_name': text,
            'family_name': 'f',
            'company': text,
            'email': target,
            'phone_number': text,
            'choice4': 'all',
            'comments': text,
            'receive_copy': 'copie',
            'captcha': 'rh6rp',
            'submit': 'Send',
        }

        response = requests.post('http://www.webcorpinfo.com/NL/contactform.htm', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(10)


if __name__ == '__main__':
    main()
