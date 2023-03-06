from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '3o7plv396m3p4ki59s181sn2t4',
    '_ga': 'GA1.3.2058588844.1677854880',
    '_gid': 'GA1.3.1653690752.1677854880',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=3o7plv396m3p4ki59s181sn2t4; _ga=GA1.3.2058588844.1677854880; _gid=GA1.3.1653690752.1677854880; _gat=1',
    'Origin': 'http://www.thebasementbar.co.uk',
    'Pragma': 'no-cache',
    'Referer': 'http://www.thebasementbar.co.uk/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Thank you.'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = 'test'
        data = {
            'fromName': 'name',
            'fromEmail': target,
            'cc': '1',
            'phone': text,
            'subject': text,
            'message': text,
            'send': 'Send',
            '__formName': 'Feedback',
            '__formKey': '1929360555640209a99a062',
        }

        response = requests.post('http://www.thebasementbar.co.uk/contact.php', cookies=cookies, headers=headers,
                                 data=data, verify=False)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
