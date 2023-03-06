cookies = {
    'PHPSESSID': '2626c37807ec1760ed57aec9d9fe8b19',
    '_ga': 'GA1.3.375471245.1677854878',
    '_gid': 'GA1.3.96189105.1677854878',
    'twk_idm_key': 'OBry0NkOQ34tb-FKt0ynS',
    '_gat': '1',
    'TawkConnectionTime': '0',
    'twk_uuid_576320f10e138a3e688e1d59': '%7B%22uuid%22%3A%221.Wrq3SRrIpb09dAaeMbcRCIDVFcunJFCXprdFq3WTMQNcvjU0e2tenDIXc4LmFwkOYNbYVVriwx0pjkuphW3mUmipkpUJeVy15pDgvL5bmOhkyzR3sqOeDzZfW%22%2C%22version%22%3A3%2C%22domain%22%3A%22microteam.co.uk%22%2C%22ts%22%3A1677855513280%7D',
}

headers = {
    'authority': 'www.microteam.co.uk',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=2626c37807ec1760ed57aec9d9fe8b19; _ga=GA1.3.375471245.1677854878; _gid=GA1.3.96189105.1677854878; twk_idm_key=OBry0NkOQ34tb-FKt0ynS; _gat=1; TawkConnectionTime=0; twk_uuid_576320f10e138a3e688e1d59=%7B%22uuid%22%3A%221.Wrq3SRrIpb09dAaeMbcRCIDVFcunJFCXprdFq3WTMQNcvjU0e2tenDIXc4LmFwkOYNbYVVriwx0pjkuphW3mUmipkpUJeVy15pDgvL5bmOhkyzR3sqOeDzZfW%22%2C%22version%22%3A3%2C%22domain%22%3A%22microteam.co.uk%22%2C%22ts%22%3A1677855513280%7D',
    'origin': 'https://www.microteam.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://www.microteam.co.uk/contact.php',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        if response:
            return response.status_code < 400
        else:
            return False

    def post(self, target) -> requests.Response | None:
        data = {
            'name': 'test',
            'email': target,
            'subject': 'subject',
            'message': self.get_text(False),
            'captcha': '53wyam',
            'dataCheck': [
                'on',
                'on',
            ],
            'copy': 'on',
        }

        response = requests.post(
            'https://www.microteam.co.uk/assets/php/sky-forms-pro/demo-contacts-process.php',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = ''
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
