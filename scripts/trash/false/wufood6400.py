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
        'https://d6400.wufoo.com/forms/m19bftgj1lospxk',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'd6400.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryXYpBreAA7Zh2H4h4',
        'origin': 'https://d6400.wufoo.com',
        'pragma': 'no-cache',
        'referer': 'https://d6400.wufoo.com/forms/m19bftgj1lospxk',
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

    data = '------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field528"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field3"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field4"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field5"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field6"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field7"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field8"\r\n\r\nCanada\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field9"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field10"\r\n\r\n123\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field10-1"\r\n\r\n123\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field10-2"\r\n\r\n1233\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field529"\r\n\r\n\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field529"\r\n\r\nYes\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field12"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field134"\r\n\r\nOther\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field531"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field330"\r\n\r\nFor Profit Organization/Business\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field430"\r\n\r\nI am uncertain\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field114"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field115"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field533"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field116"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field117"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field118"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field119"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field120"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field121"\r\n\r\nCanada\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field122"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field123"\r\n\r\n123\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field123-1"\r\n\r\n123\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field123-2"\r\n\r\n1231\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field124"\r\n\r\nhttps://d6400.wufoo.com/forms/m19bftgj1lospxk\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="Field225"\r\n\r\ntest\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nRLEUwuBeZ5cYtliDEuHY2IXN5MqR1aHe10tswuBefSxgOnFk8=\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":1,"startTime":2691,"endTime":53953,"referer":"https://d6400.wufoo.com/forms/m19bftgj1lospxk"}\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryXYpBreAA7Zh2H4h4--\r\n'

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
    s = 'Thank you'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
