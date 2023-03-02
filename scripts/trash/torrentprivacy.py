from os.path import basename

import requests

import module.config
from module import Spam

cookies = {
    'PHPSESSID': '40e347b56f09dd967fb86a19b9a0c3cd',
    'v1_site_version': '0',
    'v2_site_version': '1',
    'uniq2': '1',
    '__utma': '91903775.1811241102.1677755211.1677755211.1677755211.1',
    '__utmc': '91903775',
    '__utmz': '91903775.1677755211.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '_ym_uid': '167775521130785712',
    '_ym_d': '1677755211',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '__utmb': '91903775.3.10.1677755211',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJKitYZnypIxKV3zr',
    # 'Cookie': 'PHPSESSID=40e347b56f09dd967fb86a19b9a0c3cd; v1_site_version=0; v2_site_version=1; uniq2=1; __utma=91903775.1811241102.1677755211.1677755211.1677755211.1; __utmc=91903775; __utmz=91903775.1677755211.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _ym_uid=167775521130785712; _ym_d=1677755211; _ym_isad=2; _ym_visorc=w; __utmb=91903775.3.10.1677755211',
    'Origin': 'https://torrentprivacy.com',
    'Pragma': 'no-cache',
    'Referer': 'https://torrentprivacy.com/index.php?mod=v2_support',
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

params = {
    'mod': 'v2_support',
}

s = 'Thank you. Your message has been sent.'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryJKitYZnypIxKV3zr\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest\r\n------WebKitFormBoundaryJKitYZnypIxKV3zr\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryJKitYZnypIxKV3zr\r\nContent-Disposition: form-data; name="category_0"\r\n\r\n4\r\n------WebKitFormBoundaryJKitYZnypIxKV3zr\r\nContent-Disposition: form-data; name="body"\r\n\r\ntest\r\n------WebKitFormBoundaryJKitYZnypIxKV3zr\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryJKitYZnypIxKV3zr\r\nContent-Disposition: form-data; name="copy"\r\n\r\non\r\n------WebKitFormBoundaryJKitYZnypIxKV3zr\r\nContent-Disposition: form-data; name="Submit"\r\n\r\nSend message\r\n------WebKitFormBoundaryJKitYZnypIxKV3zr--\r\n'
        data = data.replace(module.config.TEST_TARGET, target).replace('test', self.get_text())

        response = requests.post('https://torrentprivacy.com/index.php', params=params, cookies=cookies,
                                 headers=headers, data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
