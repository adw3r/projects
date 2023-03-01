cookies = {
    'PHPSESSID': '9uhl8lod5q2ubm7pm8eon6egck',
    'coree9e3visit': '1677077178',
    '_ga': 'GA1.1.1836791938.1677077181',
    'color_scheme': 'dark',
    '_ga_48EZER7MDB': 'GS1.1.1677077180.1.1.1677077213.0.0.0',
}

headers = {
    'authority': 'ddlgfriends.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=9uhl8lod5q2ubm7pm8eon6egck; coree9e3visit=1677077178; _ga=GA1.1.1836791938.1677077181; color_scheme=dark; _ga_48EZER7MDB=GS1.1.1677077180.1.1.1677077213.0.0.0',
    'origin': 'https://ddlgfriends.net',
    'referer': 'https://ddlgfriends.net/contact',
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

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'val[category_id]': 'Support',
            'val[full_name]': self.get_text(),
            'val[subject]': self.get_text(),
            'val[email]': target,
            'val[text]': self.get_text(),
            'val[copy]': '1',
        }

        response = requests.post('https://ddlgfriends.net/contact/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    s = 'successfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
