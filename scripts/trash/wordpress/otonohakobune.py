from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'otonohakobune.com',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary8XZVUOvSfWrpOAAz',
    'origin': 'https://otonohakobune.com',
    'referer': 'https://otonohakobune.com/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'mail_sent'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n44\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.4.2\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f44-p42-o1\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n42\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nname\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="tel"\r\n\r\ntest\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundary8XZVUOvSfWrpOAAz--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://otonohakobune.com/wp-json/contact-form-7/v1/contact-forms/44/feedback',
            headers=headers,
            data=data.encode(),
            proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'))
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)


if __name__ == '__main__':
    main()
