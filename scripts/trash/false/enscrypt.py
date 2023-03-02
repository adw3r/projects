from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'a3ptrfoc69p8m4fkfhqd709ovo',
    'sc_is_visitor_unique': 'rx12652747.1677576692.C7D8409CDB094FC5EDB94C84FAB2F543.1.1.1.1.1.1.1.1.1-12720744.1677508888.3.3.3.3.3.3.3.3.3',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary5unR4fMmnrIWRgQB',
    # 'Cookie': 'PHPSESSID=a3ptrfoc69p8m4fkfhqd709ovo; sc_is_visitor_unique=rx12652747.1677576692.C7D8409CDB094FC5EDB94C84FAB2F543.1.1.1.1.1.1.1.1.1-12720744.1677508888.3.3.3.3.3.3.3.3.3',
    'Origin': 'https://enscrypt.io',
    'Pragma': 'no-cache',
    'Referer': 'https://enscrypt.io/ensregister.php',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundary5unR4fMmnrIWRgQB\r\nContent-Disposition: form-data; name="fnamelname"\r\n\r\nname name\r\n------WebKitFormBoundary5unR4fMmnrIWRgQB\r\nContent-Disposition: form-data; name="emailid"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary5unR4fMmnrIWRgQB\r\nContent-Disposition: form-data; name="pswordid1"\r\n\r\nZxcasdqwe123\r\n------WebKitFormBoundary5unR4fMmnrIWRgQB\r\nContent-Disposition: form-data; name="pswordid2"\r\n\r\nZxcasdqwe123\r\n------WebKitFormBoundary5unR4fMmnrIWRgQB\r\nContent-Disposition: form-data; name="ucomp_name"\r\n\r\ntest\r\n------WebKitFormBoundary5unR4fMmnrIWRgQB\r\nContent-Disposition: form-data; name="ulanguages"\r\n\r\npython\r\n------WebKitFormBoundary5unR4fMmnrIWRgQB--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post('https://enscrypt.io/ensregister.php', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    s = 'successfully'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
