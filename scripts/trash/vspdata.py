from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'PHPSESSID': 'fl6o5hgm97vs91mi4mlda7hhq72uohd4nek851p8avqh3l2smne1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://services.vspdata.cz',
            'Pragma': 'no-cache',
            'Referer': 'https://services.vspdata.cz/de/contact/',
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

        text = self.get_text(False)
        data = {
            'to': 'aik',
            'name': 'text',
            'mail': target,
            'subject': 'text',
            'message': 'text',
            'antibot': 'notabot',
            'sendCopy': 'on',
            'send': 'SENDEN',
            '_token_': 'cx9d3sh23hZHUZukMuy5WUnZjm9rcHnxt5NfU=',
            '_do': 'contactForm-submit',
        }

        response = requests.post('https://services.vspdata.cz/de/contact/', cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'Vielen Dank'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
