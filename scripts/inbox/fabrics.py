from os.path import basename

import requests

from module import Spam

cookies = {
    'd016c4f59c9c5afccdfacac7a5eaeabb': 'X96vnSpkwHnsjCA4hH3mrHX8erHbrvszqNWESjsLO6N%2FVVn482%2BAgT4naegv98rRZTkaGqUK8GjOJMIeYIuytufjx%2BU%2B88NchBGUDl0OcXE%3D000074',
}

headers = {
    'authority': 'fabrics.automaticblindsandshades.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'd016c4f59c9c5afccdfacac7a5eaeabb=X96vnSpkwHnsjCA4hH3mrHX8erHbrvszqNWESjsLO6N%2FVVn482%2BAgT4naegv98rRZTkaGqUK8GjOJMIeYIuytufjx%2BU%2B88NchBGUDl0OcXE%3D000074',
    'origin': 'https://fabrics.automaticblindsandshades.com',
    'pragma': 'no-cache',
    'referer': 'https://fabrics.automaticblindsandshades.com/contact.php',
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
        text = self.get_text(False)
        data = {
            'Subject': text,
            'first_name': text,
            'last_name': text,
            'Email': target,
            'Phone': text,
            'Spam': 'four',
            'Comment': 'test<br>',
            'contact_form': 'Submit',
        }
        response = requests.post('https://fabrics.automaticblindsandshades.com/contact.php', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'successfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
