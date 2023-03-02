import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'http://www.veyseldrums.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.veyseldrums.com/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'anrede': 'Herr',
            'vorname': self.get_text(),
            'nachname': self.get_text(),
            'email': target,
            'betreff': 'test http://www.veyseldrums.com/contact.php',
            'nachricht': 'test http://www.veyseldrums.com/contact.php',
            'kopie': 'ja',
        }

        response = requests.post('http://www.veyseldrums.com/contact.php', headers=headers, data=data, verify=False, proxies=self.get_proxies())
        return response


def main():
    s = ' Ihre Nachricht wurde gesendet!'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
