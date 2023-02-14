from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'saizo7.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://saizo7.com',
    'referer': 'https://saizo7.com/contact/',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            '_wpcf7': '21',
            '_wpcf7_version': '5.4.1',
            '_wpcf7_locale': 'ja',
            '_wpcf7_unit_tag': 'wpcf7-f21-p19-o1',
            '_wpcf7_container_post': '19',
            '_wpcf7_posted_data_hash': '',
            'your-name': 'name',
            'your-email': target,
            'tel': self.get_text(),
            'your-message': self.get_text(),
        }

        response = requests.post('https://saizo7.com/contact/', headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'success')
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
