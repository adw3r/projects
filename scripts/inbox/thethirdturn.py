from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '__utma': '105669702.710854255.1678094598.1678094598.1678094598.1',
            '__utmc': '105669702',
            '__utmz': '105669702.1678094598.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            '__utmt': '1',
            '__gads': 'ID=677a1c1af3cfd0d9-22f9fef145dd00d4:T=1678094598:RT=1678094598:S=ALNI_MbmmR53VrAEkpXjXqsKIBRpw5swJA',
            '__gpi': 'UID=00000bc0f9e33303:T=1678094598:RT=1678094598:S=ALNI_MbCCP4BPXmsMqhrOU9U2LSSXcdHzQ',
            '__utmb': '105669702.3.10.1678094598',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': '__utma=105669702.710854255.1678094598.1678094598.1678094598.1; __utmc=105669702; __utmz=105669702.1678094598.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __gads=ID=677a1c1af3cfd0d9-22f9fef145dd00d4:T=1678094598:RT=1678094598:S=ALNI_MbmmR53VrAEkpXjXqsKIBRpw5swJA; __gpi=UID=00000bc0f9e33303:T=1678094598:RT=1678094598:S=ALNI_MbCCP4BPXmsMqhrOU9U2LSSXcdHzQ; __utmb=105669702.3.10.1678094598',
            'Origin': 'https://www.thethirdturn.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.thethirdturn.com/wiki/Special:Contact',
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

        response = requests.post('https://www.thethirdturn.com/wiki/Special:Contact', cookies=cookies, headers=headers,
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
