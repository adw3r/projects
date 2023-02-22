from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '66d45a31f40187cd0082eaec3bdc80a5',
    'coreb43fvisit': '1677069009',
}

headers = {
    'authority': 'www.tapped-out.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'PHPSESSID=66d45a31f40187cd0082eaec3bdc80a5; coreb43fvisit=1677069009',
    'origin': 'https://www.tapped-out.co.uk',
    'referer': 'https://www.tapped-out.co.uk/contact/',
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
        text = self.get_text()
        data = {
            'val[category_id]': 'Sales',
            'val[full_name]': text,
            'val[subject]': text,
            'val[email]': target,
            'val[text]': text,
            'val[copy]': '1',
        }

        response = requests.post('https://www.tapped-out.co.uk/contact/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'successfully')
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
