from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        pageurl = 'https://kjubrealestate.lu/contact-us/'
        googlekey = '6LdDoN8dAAAAAEFBkhHwRSzJo6FYL1A881LIWHu0'
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        import requests

        cookies = {
            '_ga': 'GA1.1.937590697.1676974810',
            '_ga_KR13ZXYE7M': 'GS1.1.1676974809.1.1.1676976765.0.0.0',
        }

        headers = {
            'authority': 'kjubrealestate.lu',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': '_ga=GA1.1.937590697.1676974810; _ga_KR13ZXYE7M=GS1.1.1676974809.1.1.1676976765.0.0.0',
            'origin': 'https://kjubrealestate.lu',
            'referer': 'https://kjubrealestate.lu/contact-us/',
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

        data = {
            'contact_name': 'name',
            'contact_email': target,
            'contact_subject': self.get_text(),
            'contact_message': self.get_text(),
            'contact_email_copy': '1',
            'gdpr': '1',
            'g-recaptcha-response': cap,
            'submit': '1',
        }

        response = requests.post('https://kjubrealestate.lu/contact-us/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Your email was sent successfully. Thank you!')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
