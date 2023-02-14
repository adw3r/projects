from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers = {
            'authority': 'shop.highcharts.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://shop.highcharts.com',
            'referer': 'https://shop.highcharts.com/contact/quote',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'woocommerce-session': 'Session eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Nob3AuaGlnaGNoYXJ0cy5jb20vd29hcGkiLCJpYXQiOjE2NzYzNzE0NjMsIm5iZiI6MTY3NjM3MTQ2MywiZXhwIjoxNjc3NTgxMDYzLCJkYXRhIjp7ImN1c3RvbWVyX2lkIjoidF84MWQxYWE2ZjhjNDA5OTJhOTA0M2U0MmUxNDZkNTYifX0.orn7y4agGEVwiKZGiBWCYqJouuFtA2gyleHfsKjfJCU',
        }
        json_data = {
            'operationName': 'SUBMIT_FORM',
            'variables': {
                'input': {
                    'formId': 2,
                    'data': [
                        {
                            'id': 7,
                            'value': target,
                        },
                        {
                            'id': 60,
                            'value': self.get_text(),
                        },
                        {
                            'id': 61,
                            'value': self.get_text(),
                        },
                        {
                            'id': 9,
                            'value': self.get_text(),
                        },
                        {
                            'id': 10,
                            'value': 'AF',
                        },
                        {
                            'id': 11,
                            'value': 'Financial Services',
                        },
                        {
                            'id': 12,
                            'value': 'test',
                        },
                        {
                            'id': 14,
                            'value': 'true',
                        },
                        {
                            'id': 15,
                            'value': 'true',
                        },
                        {
                            'id': 51,
                            'value': 'true',
                        },
                        {
                            'id': 56,
                        },
                        {
                            'id': 5,
                            'value': '',
                        },
                        {
                            'id': 6,
                            'value': '',
                        },
                        {
                            'id': 8,
                            'value': '',
                        },
                        {
                            'id': 13,
                            'value': '',
                        },
                        {
                            'id': 16,
                            'value': '',
                        },
                        {
                            'id': 17,
                            'value': '',
                        },
                    ],
                },
            },
            'query': 'mutation SUBMIT_FORM($input: SubmitFormInput!) {\n  submitForm(input: $input) {\n    success\n    __typename\n  }\n}\n',
        }
        response = requests.post('https://shop.highcharts.com/woapi/graphql/', headers=headers, json=json_data,
                                 proxies=self.get_proxies())
        return response


def main():
    s = 'success":true'
    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
