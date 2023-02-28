from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.744944198.1677078866',
    '_gid': 'GA1.2.442858766.1677078866',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.744944198.1677078866; _gid=GA1.2.442858766.1677078866; _gat=1',
    'Origin': 'http://www.marriagescelebrant.com',
    'Referer': 'http://www.marriagescelebrant.com/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Thank you'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': 'name',
            'email': target,
            'phone': '123132123',
            'reason': 'Other general enquiry',
            'message': self.get_text(False),
            'spamq': 'wed',
            'GBPERSVFI7C41X2FI7C41X0194FI7C41X183FI7C41X167FI7C41X244HTTPFI7C41XFI7C41XFI7C41XWWWFI7C41XMARRIAGESCELEBRANTFI7C41XCOMFI7C41XCONTACTFI7C41XPHPAEDTFI7C41X110039600': '',
            'p-mail': '',
            'GBAEDTXZ7R9E6110039600PERSHTTPXZ7R9E6XZ7R9E6XZ7R9E6WWWXZ7R9E6MARRIAGESCELEBRANTXZ7R9E6COMXZ7R9E6CONTACTXZ7R9E6PHPVXZ7R9E62XZ7R9E60194XZ7R9E6183XZ7R9E6167XZ7R9E6244': 'GBAEDTXZ7R9E6110039600PERSHTTPXZ7R9E6XZ7R9E6XZ7R9E6WWWXZ7R9E6MARRIAGESCELEBRANTXZ7R9E6COMXZ7R9E6CONTACTXZ7R9E6PHPVXZ7R9E62XZ7R9E60194XZ7R9E6183XZ7R9E6167XZ7R9E6244',
            'gbcc': 'gbcc',
            '1946WPSA3C1836WPSA3C1676WPSA3C244AEDT6WPSA3C110039600V6WPSA3C26WPSA3C0PERSHTTP6WPSA3C6WPSA3C6WPSA3CWWW6WPSA3CMARRIAGESCELEBRANT6WPSA3CCOM6WPSA3CCONTACT6WPSA3CPHP': 'Submit Form',
        }

        response = requests.post('http://www.marriagescelebrant.com/contact.php', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='fkasn23')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(5)


if __name__ == '__main__':
    main()
