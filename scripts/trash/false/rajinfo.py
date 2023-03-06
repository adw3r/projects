from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.3.1775867503.1677857398',
    '_gid': 'GA1.3.3162921.1677857398',
    '_gat_gtag_UA_164550440_1': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_ga=GA1.3.1775867503.1677857398; _gid=GA1.3.3162921.1677857398; _gat_gtag_UA_164550440_1=1',
    'Origin': 'https://www.rajinfo.co.in',
    'Pragma': 'no-cache',
    'Referer': 'https://www.rajinfo.co.in/contact.php',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

s = 'Your message was successfully sent!'


class ConcreteSpam(Spam):
    def check_success(self, response: requests.Response | None) -> bool:
        if response:
            return response.status_code < 400
        return False

    def post(self, target) -> requests.Response | None:
        data = {
            'name': 'test',
            'email': target,
            'subject': 'test',
            'message': self.get_text(),
            'copy': 'on',
        }

        response = requests.post('https://www.rajinfo.co.in/demo-contacts.php', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        print(response.text)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
