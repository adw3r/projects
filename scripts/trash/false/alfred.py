from os.path import basename

import requests

from module import Spam

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Origin': 'http://www.alfred-fischer.de',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.alfred-fischer.de/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = f'test {self.promo_link}'
        data = {
            'cf[company]': 'company',
            'cf[name]': 'name',
            'cf[phone]': '12642634',
            'cf[email]': target,
            'cf[category]': 'General Inquiry',
            'cf[copy]': 'on',
            'cf[data]': 'on',
            'cf[message]': text,
        }

        response = requests.post('http://www.alfred-fischer.de/contact.php', headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


def main():
    s = 'successfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
