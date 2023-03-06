from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            '_gid': 'GA1.2.628328214.1678093169',
            'wikh_share_db_wiki_mwuser-sessionId': '80beed7dc55401cca9b7',
            '_ga_DMBHXB1QVZ': 'GS1.1.1678093166.1.1.1678093681.0.0.0',
            '_ga': 'GA1.2.398774296.1678093167',
            '_gat': '1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': '_gid=GA1.2.628328214.1678093169; wikh_share_db_wiki_mwuser-sessionId=80beed7dc55401cca9b7; _ga_DMBHXB1QVZ=GS1.1.1678093166.1.1.1678093681.0.0.0; _ga=GA1.2.398774296.1678093167; _gat=1',
            'Origin': 'https://en.wikihussain.com',
            'Pragma': 'no-cache',
            'Referer': 'https://en.wikihussain.com/view/Special:Contact',
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

        text = self.get_text()
        data = {
            'title': 'Special:Contact',
            'wpFromName': text,
            'wpFromAddress': target,
            'wpSubject': text,
            'wpText': text,
            'wpCCme': '1',
            'wpEditToken': '+\\',
            'wpFormType': '',
        }

        response = requests.post('https://en.wikihussain.com/view/Special:Contact', cookies=cookies, headers=headers,
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
