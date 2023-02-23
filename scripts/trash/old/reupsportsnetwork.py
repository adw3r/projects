from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '9da2af94409bd36f4ad5741929aa279f',
    'coree27fvisit': '1677075585',
    '_ga': 'GA1.2.2042800516.1677075590',
    '_gid': 'GA1.2.114535536.1677075590',
    '_gat_gtag_UA_198067436_1': '1',
}

headers = {
    'authority': 'reupsportsnetwork.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=9da2af94409bd36f4ad5741929aa279f; coree27fvisit=1677075585; _ga=GA1.2.2042800516.1677075590; _gid=GA1.2.114535536.1677075590; _gat_gtag_UA_198067436_1=1',
    'origin': 'https://reupsportsnetwork.com',
    'referer': 'https://reupsportsnetwork.com/contact/',
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

s = 'successfully'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'val[category_id]': 'Suggestions',
            'val[full_name]': 'test',
            'val[subject]': 'subject',
            'val[email]': target,
            'val[text]': self.get_text(),
            'val[copy]': '1',
        }

        response = requests.post('https://reupsportsnetwork.com/contact/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
