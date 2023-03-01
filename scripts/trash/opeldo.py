import requests

cookies = {
    'PHPSESSID': '08425460e3444ec6535a28c0077d05be',
}

headers = {
    'authority': 'opeldo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=08425460e3444ec6535a28c0077d05be',
    'origin': 'https://opeldo.com',
    'pragma': 'no-cache',
    'referer': 'https://opeldo.com/tutorial_demo/flower_garden/contact.php',
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


s = 'have received your message,'
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(False).replace(self.promo_link, self.promo_link.replace('https://', 'www.telegra.ph/Ispolzuj-50-frispinov-03-01'))
        data = {
            'name': 'name',
            'email': target,
            'reason': 'About Tutorial',
            'message': text,
            'send_copy': 'Yes',
            'submit': '',
        }

        response = requests.post('https://opeldo.com/tutorial_demo/flower_garden/contact.php', cookies=cookies,
                                 headers=headers, data=data)
        print(response.text)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
