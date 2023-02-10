from os.path import basename

import requests

import module

cookies = {
    '_fbp': 'fb.1.1674813265050.1856752646',
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
}

headers = {
    'authority': 'placesirememberlealane.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_fbp=fb.1.1674813265050.1856752646; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22',
    'origin': 'https://placesirememberlealane.com',
    'referer': 'https://placesirememberlealane.com/contact-us/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
url = 'https://placesirememberlealane.com/contact-us/'
key = '6Le-DPEUAAAAAKAQYawITgPe0VAVs6NKkOlgPoIe'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(url, key)
        if not cap:
            return
        data = {
            'contact_name': 'test',
            'contact_email': target,
            'contact_subject': self.get_text(),
            'contact_message': self.get_text(),
            'contact_email_copy': '1',
            'gdpr': '1',
            'g-recaptcha-response': cap,
            'submit': '1',
        }

        response = requests.post('https://placesirememberlealane.com/contact-us/', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Your email was sent successfully. Thank you!')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
