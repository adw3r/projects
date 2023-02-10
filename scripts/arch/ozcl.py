from os.path import basename

import requests

from module import Spam

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarygQ9oJR0cm7ZegTUP',
    'Origin': 'http://ozcl.tokyo',
    'Referer': 'http://ozcl.tokyo/contact/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n128\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n4.9\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f128-p131-o1\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n131\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest http://ozcl.tokyo/contact/\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest http://ozcl.tokyo/contact/\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest http://ozcl.tokyo/contact/\r\n------WebKitFormBoundarygQ9oJR0cm7ZegTUP--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test http://ozcl.tokyo/contact/', self.get_text())
        response = requests.post(
            'http://ozcl.tokyo/wp-json/contact-form-7/v1/contact-forms/128/feedback',
            headers=headers,
            data=data.encode(),
            verify=False, proxies=self.get_proxies(), timeout=30
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'mail_sent')
    res = spam.send_post()
    if res:
        spam.run_concurrently(2)


if __name__ == '__main__':
    main()
