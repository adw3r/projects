from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.1504235734.1677762099',
    '_gid': 'GA1.2.835605239.1677762099',
    'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%220ed79649eae7ab47ef3f1eae11f35663%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%2262.80.185.106%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F110.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1677764009%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dc82abdebfeddd5e12aa9e29b9dd41d78c2bff780',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.kancelariakuciapski.pl',
    'Pragma': 'no-cache',
    'Referer': 'https://www.kancelariakuciapski.pl/eng/contact',
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

s = 'success'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'imie': self.get_text(),
            'email': target,
            'tel': '123123',
            'message': self.get_text(),
            'kopia': 'yes',
        }

        response = requests.post('https://www.kancelariakuciapski.pl/eng/contact', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
