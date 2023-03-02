from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'blueriver-homecare.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://blueriver-homecare.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://blueriver-homecare.co.uk/contact.php',
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

s = 'Thank you for contacting us, we will reply to you soon.'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': 'test',
            'email': target,
            'reason': 'Book Carer',
            'message': f'test {self.promo_link}',
            'send_copy': 'Yes',
            'submit': '',
        }

        response = requests.post('https://blueriver-homecare.co.uk/contact.php', headers=headers, data=data)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
