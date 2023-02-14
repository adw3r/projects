from os.path import basename

import requests

from module import Spam

cookies = {
    '__utma': '133244492.1479827536.1676365697.1676365697.1676365697.1',
    '__utmc': '133244492',
    '__utmz': '133244492.1676365697.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmt': '1',
    '__utmb': '133244492.5.10.1676365697',
}

headers = {
    'authority': 'studio101.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__utma=133244492.1479827536.1676365697.1676365697.1676365697.1; __utmc=133244492; __utmz=133244492.1676365697.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=133244492.5.10.1676365697',
    'origin': 'https://studio101.org',
    'referer': 'https://studio101.org/contact',
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
            '_wpcf7': '410',
            '_wpcf7_version': '5.1.6',
            '_wpcf7_locale': 'en_US',
            '_wpcf7_unit_tag': 'wpcf7-f410-p9-o1',
            '_wpcf7_container_post': '9',
            'your-name': 'test',
            'your-email': target,
            'your-subject': self.get_text(False),
            'your-message': self.get_text(False),
        }

        response = requests.post('https://studio101.org/contact', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'あなたのメッセージは送信')
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)


if __name__ == '__main__':
    main()
