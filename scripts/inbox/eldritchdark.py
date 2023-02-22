headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'http://www.eldritchdark.com',
    'Referer': 'http://www.eldritchdark.com/contact/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Your email has been sent'
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'age': 'emVybzI=',
            'name': self.get_text(),
            'email': target,
            'subject': self.get_text(),
            'cc': 'on',
            'phone': '2',
            'comments': self.get_text(),
            'action': 'Send Message',
            'from_page': 'http://www.eldritchdark.com/contact',
        }

        response = requests.post('http://www.eldritchdark.com/contact/', headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
