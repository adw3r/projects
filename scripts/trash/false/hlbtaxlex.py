from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '67dc13c8291b652bb3bacfcfad456d86',
    '_ga': 'GA1.2.1884665157.1677578700',
    '_gid': 'GA1.2.1558241747.1677578700',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.hlbtaxlex.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.hlbtaxlex.com/contact-us/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'fieldName': self.get_text(),
            'fieldCompanyName': self.get_text(),
            'fieldEmail': target,
            'fieldCity': 'test',
            'fieldCountry': 'test',
            'fieldSubject': self.get_text(),
            'fieldMessage': 'test',
            'fieldSendCopy': 'yes',
            'captcha_1': '809447139',
            'captcha': 'zrhfl6',
            'contact_us_form': '',
            'enter_your_email_for_get_notification': target,
            'contact-us': '',
        }

        response = requests.post('https://www.hlbtaxlex.com/contact-us/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    s = 'succesfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(1)


if __name__ == '__main__':
    main()
