import re
from os.path import basename

import requests

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
        'https://gichd.wufoo.com/forms/m9iwqlh0i4a2u0/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'gichd.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarycs6AwBfBrCDIZiqA',
        'origin': 'https://gichd.wufoo.com',
        'referer': 'https://gichd.wufoo.com/forms/m9iwqlh0i4a2u0/',
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

    data = '------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field140"\r\n\r\nMs\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field5"\r\n\r\nfield\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field4"\r\n\r\nfield\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field6"\r\n\r\ntest\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field9"\r\n\r\nState\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field544"\r\n\r\nAFGHANISTAN\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field545"\r\n\r\nAFGHANISTAN NATIONAL DISASTER MANAGEMENT AUTHORITY\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field298"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field546"\r\n\r\nADMINISTRATION\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field304"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field547"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field141"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field548"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field308"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field549"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field311"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field968"\r\n\r\nYes\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field970"\r\n\r\nOnline (link will be sent to e-mail address provided)\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field29"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field762"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field153"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field158"\r\n\r\n380\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field163"\r\n\r\n123124214\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field975"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field972"\r\n\r\n380\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field161"\r\n\r\n12312\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field974"\r\n\r\n123124214\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field319"\r\n\r\nfield\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field323"\r\n\r\nfield\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field324"\r\n\r\nfield\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field326"\r\n\r\nfie\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field551"\r\n\r\nBELGIUM\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="Field555"\r\n\r\nI understand this condition.\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nLjRWw4U0LKkzFgCRrjkf58wuslashgwPwuslashY2iTDFqg0cjyTrkA=\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":8627,"endTime":53972,"referer":null}\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarycs6AwBfBrCDIZiqA--\r\n'

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
        # s.proxies = self.get_proxies()
        get_resp = get(s)
        pattern = re.compile('(?<=name="idstamp" value=").*(?=" >)')
        idstamp = pattern.findall(get_resp.text)
        if not idstamp:
            return
        # 100 chars
        text = f'🔥Используй 40 FS за принятие участия в проекте AllRight  по  ссылке  ➡️ {self.promo_link} ⬅️'
        post_resp = post(s, idstamp[0], text, target)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Your registration is confirmed.')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
