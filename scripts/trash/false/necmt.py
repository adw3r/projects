cookies = {
    'PHPSESSID': '759fe371ef130db5bc74036dd4a25978',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=759fe371ef130db5bc74036dd4a25978',
    'Origin': 'http://necmt.org',
    'Pragma': 'no-cache',
    'Referer': 'http://necmt.org/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Thank you for contacting'
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'recip_role': 'Admin',
            'sender_email': target,
            'messagetext': self.get_text(),
            'Submit': 'Send Message',
        }

        response = requests.post('http://necmt.org/sendmail.php', cookies=cookies, headers=headers, data=data,
                                 verify=False, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
