from os.path import basename

import requests

from module import Spam

cookies = {
    'ic_window_resolution': '1920',
    'ic_pixel_ratio': '1',
}

headers = {
    'authority': 'www.zappconsulting.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarypsFAInLEmi3BoFGA',
    'origin': 'https://www.zappconsulting.com',
    'referer': 'https://www.zappconsulting.com/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n58\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.1.7\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f58-p15-o1\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n15\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nname\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundarypsFAInLEmi3BoFGA--\r\n'
        data = data.replace('test', self.get_text()).replace('wezxasqw@gmail.com', target)
        response = requests.post(
            'https://www.zappconsulting.com/wp-json/contact-form-7/v1/contact-forms/58/feedback',
            cookies=cookies,
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
