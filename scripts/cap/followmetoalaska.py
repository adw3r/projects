from os.path import basename

import requests

import module

url = 'https://followmetoalaska.com/contact/'
key = '6LcWJEokAAAAAH-CzwQ4MBiLvxfclt5oJ5NyrzsL'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://followmetoalaska.com',
    'Referer': 'https://followmetoalaska.com/contact/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        captcha = self.solve_captcha(url, key)
        if not captcha:
            return
        data = {
            'contact_name': 'test',
            'contact_email': target,
            'contact_subject': 'text',
            'contact_message': self.get_text(),
            'contact_email_copy': '1',
            'g-recaptcha-response': captcha,
            'submit': '1',
        }
        for _ in range(15):
            try:
                response = requests.post('https://followmetoalaska.com/contact/', headers=headers, data=data,
                                         proxies=self.get_proxies(), timeout=10)
                return response
            except Exception as e:
                print(e)
        return


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Your email was sent successfully. Thank you!')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
