from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '8nd231qrpmnn0f2m66sr5fk9m5',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=8nd231qrpmnn0f2m66sr5fk9m5',
    'Origin': 'http://www.hrp-engineering.com',
    'Referer': 'http://www.hrp-engineering.com/contact.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

s = 'Your message has been sent.'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'nameksljf': 'test',
            'emailksljf': target,
            'copy': 'on',
            'human': '1',
            'message': self.get_text(False),
            'name': '',
            'email': '',
        }

        response = requests.post('http://www.hrp-engineering.com/processForm.php', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
