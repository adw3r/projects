import requests

cookies = {
    '_ga': 'GA1.2.383815290.1677755202',
    '_gid': 'GA1.2.127173853.1677755202',
    '_gat_gtag_UA_96829080_1': '1',
}

headers = {
    'authority': 'themickeywiki.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.2.383815290.1677755202; _gid=GA1.2.127173853.1677755202; _gat_gtag_UA_96829080_1=1',
    'origin': 'https://themickeywiki.com',
    'pragma': 'no-cache',
    'referer': 'https://themickeywiki.com/index.php/Special:Contact',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Your email message has been sent.'
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = f'test {self.promo_link}'
        data = {
            'wpFromName': 'name',
            'wpFromAddress': target,
            'wpSubject': text,
            'wpText': text,
            'wpCCme': '1',
            'wpEditToken': '+\\',
            'title': 'Special:Contact',
            'wpFormType': '',
        }

        response = requests.post('https://themickeywiki.com/index.php/Special:Contact', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
