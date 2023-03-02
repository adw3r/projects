import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session) -> requests.Response:
    cookies = {
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'PHPSESSID=nc5p53nar9h5a9evqlkmgt1qj6bc3rgr; _ga=GA1.2.549261065.1677749283; _gid=GA1.2.346141452.1677749283; twk_idm_key=sbsDiQ7PWeUKYGCLNSVsP; hasShown=true; TawkConnectionTime=0; twk_uuid_602981609c4f165d47c332ae=%7B%22uuid%22%3A%221.2U5h4B0kDFxL3mx5GqAYSaBbcBvIUehKng7zM7QF33A4gQZszFk9jSfCR5r3TzeMOVae9Ll3DeFZ5gF1CIVhRJsOAu54Bau1szaRFSvNsvww9jw2X7UaIxwOQyPMsYk%22%2C%22version%22%3A3%2C%22domain%22%3A%22amtelwebfunding.com%22%2C%22ts%22%3A1677749844776%7D',
        'Pragma': 'no-cache',
        'Referer': 'https://amtelwebfunding.com/contact-us',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = session.get('https://amtelwebfunding.com/contact-us', cookies=cookies, headers=headers)
    return response


def post(session, token, text, target) -> requests.Response:
    cookies = {
    }

    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'PHPSESSID=nc5p53nar9h5a9evqlkmgt1qj6bc3rgr; _ga=GA1.2.549261065.1677749283; _gid=GA1.2.346141452.1677749283; twk_idm_key=sbsDiQ7PWeUKYGCLNSVsP; hasShown=true; _gat_gtag_UA_177644814_1=1; TawkConnectionTime=0; twk_uuid_602981609c4f165d47c332ae=%7B%22uuid%22%3A%221.2U5h4B0kDFxL3mx5GqAYSaBbcBvIUehKng7zM7QF33A4gQZszFk9jSfCR5r3TzeMOVae9Ll3DeFZ5gF1CIVhRJsOAu54Bau1szaRFSvNsvww9jw2X7UaIxwOQyPMsYk%22%2C%22version%22%3A3%2C%22domain%22%3A%22amtelwebfunding.com%22%2C%22ts%22%3A1677749837087%7D',
        'Origin': 'https://amtelwebfunding.com',
        'Pragma': 'no-cache',
        'Referer': 'https://amtelwebfunding.com/contact-us',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'names': 'name',
        'email': target,
        'subject': 'subject',
        'message': text,
        'self': 'on',
        'token': token,
        'url': '../../../contact-us',
        'what': 'new_contact_message',
    }

    response = session.post('https://amtelwebfunding.com/besik-admin/controller/create/', cookies=cookies,
                            headers=headers, data=data)
    return response


pattern = re.compile('(?<=<input type="hidden" name="token" value=").+(?=">)')


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        with requests.Session() as session:
            session.proxies = self.get_proxies()
            get_resp = get(session)
            token = pattern.search(get_resp.text).group(0)
            post_resp = post(session, token, self.get_text(False), target)
            return post_resp


def main():
    s = '{"success": true}'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
