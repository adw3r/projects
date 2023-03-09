cookies = {
    'PHPSESSID': '84hesar75tp74qr1o2sk08ktdt',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=84hesar75tp74qr1o2sk08ktdt',
    'Origin': 'https://gglconsulting.net',
    'Pragma': 'no-cache',
    'Referer': 'https://gglconsulting.net/contact.php',
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

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': target,
            'subject': self.get_text(),
            'message': self.get_text(),
            'send_copy': 'on',
        }

        response = requests.post('https://gglconsulting.net/contact.php', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    s = 'successfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='pobcasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
