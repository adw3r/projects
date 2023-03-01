from os.path import basename

import requests

import module
from module import Spam

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://hostwriter.org',
    'Referer': 'https://hostwriter.org/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-CSRF-Token': 'null',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    '_format': 'json',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        json_data = {
            'contact_form': [
                {
                    'target_id': 'feedback',
                },
            ],
            'name': [
                {
                    'value': text,
                },
            ],
            'mail': [
                {
                    'value': target,
                },
            ],
            'subject': [
                {
                    'value': 'subject',
                },
            ],
            'message': [
                {
                    'value': text,
                },
            ],
            'copy': [
                {
                    'value': 1,
                },
            ],
        }

        response = requests.post('https://api.hostwriter.org/entity/contact_message', params=params, headers=headers,
                                 json=json_data, proxies=self.get_proxies())

        return response


def main():
    s = 'mail'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
