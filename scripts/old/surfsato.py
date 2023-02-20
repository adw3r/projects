from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        headers = {
            'authority': 'surfsato.net',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryfiA8GMek1VEp37JB',
            'origin': 'https://surfsato.net',
            'referer': 'https://surfsato.net/contact-us/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = '------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n5\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.1.4\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f5-p4310-o1\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n4310\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryfiA8GMek1VEp37JB--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()
        response = requests.post('https://surfsato.net/wp-json/contact-form-7/v1/contact-forms/5/feedback',
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'mail_sent')
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)


if __name__ == '__main__':
    main()
