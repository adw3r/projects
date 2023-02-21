import re
from os.path import basename

import requests

from module import Spam


def get(s):
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = s.get('https://www.careopinion.org.au/contact', headers=headers)
    return response


def post(s, cap, token, text, target):
    headers = {
        'Origin': 'https://www.careopinion.org.au',
        'Referer': 'https://www.careopinion.org.au/contact',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        '__RequestVerificationToken': token,
        'DeviceId': '',
        'Name': 'name',
        'RealEmail': target,
        'Email': '',
        'Number': '213123213213',
        'TopicId': '6',
        'Message': f'<p>{text}</p>',
        'ReceiptRequested': [
            'true',
            'false',
        ],
        'g-recaptcha-response': cap,
    }

    response = s.post('https://www.careopinion.org.au/contact', headers=headers, data=data)
    return response


pageurl = 'https://www.careopinion.org.au/contact'
googlekey = '6LdeVuEZAAAAAPFxnemR4c8dD3GHOhToci7GxCNw'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        get_resp = get(s)
        token = re.compile('(?<=Token" type="hidden" value=").*(?=" />)').search(get_resp.text)
        cap = self.solve_captcha(pageurl, googlekey)
        if not any((cap, token)):
            return
        post_resp = post(s, cap, token.group(0), self.get_text(False), target)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Message sent')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
