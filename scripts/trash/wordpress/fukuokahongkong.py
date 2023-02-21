from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'fukuokahongkong.com',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryN7yI2sTqCsLVwHtD',
    'origin': 'https://fukuokahongkong.com',
    'referer': 'https://fukuokahongkong.com/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n17\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.4.2\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f17-p15-o1\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n15\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nanem\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="tel"\r\n\r\ntest\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryN7yI2sTqCsLVwHtD--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://fukuokahongkong.com/wp-json/contact-form-7/v1/contact-forms/17/feedback',
            headers=headers,
            data=data.encode(), proxies=self.get_proxies()
        )
        return response


def main():
    s = 'mail_sent'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)


if __name__ == '__main__':
    main()
