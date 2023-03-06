from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'jtmg6l772q5r0v5bp7n1cg8bj2',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'http://www.thapanamassage.co.uk',
    'Pragma': 'no-cache',
    'Referer': 'http://www.thapanamassage.co.uk/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Form Submission Successful...'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'validate': 'yes',
            'name': 'test',
            'tel': '123123',
            'email': target,
            'message': self.get_text(),
            'human': '2023',
            'copy': '1',
            'submit': ' Submit Form ',
        }

        response = requests.post('http://www.thapanamassage.co.uk/contact.php', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
