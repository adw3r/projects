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
        'https://ajchr.wufoo.com/forms/sejlodl02npkdl/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'ajchr.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryVbyfJBPnvtGyrzXM',
        'origin': 'https://ajchr.wufoo.com',
        'referer': 'https://ajchr.wufoo.com/forms/sejlodl02npkdl/',
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

    data = '------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field3"\r\n\r\ntest\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field4"\r\n\r\ntest\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field5"\r\n\r\ntest\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field6"\r\n\r\ntest\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field7"\r\n\r\n12411\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field8"\r\n\r\nAustralia\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field9"\r\n\r\n123\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field9-1"\r\n\r\n123\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field9-2"\r\n\r\n1123\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field11"\r\n\r\n213\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field11-1"\r\n\r\n231\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field11-2"\r\n\r\n1231\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field12"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field13"\r\n\r\ntest\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field16"; filename="file"\r\nContent-Type: application/octet-stream\r\n\r\nawdawd\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field17"; filename="file"\r\nContent-Type: application/octet-stream\r\n\r\nawdawd\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field21"\r\n\r\n1212\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="Field25"\r\n\r\ngoogle\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nHu8AlM7otGzhgWp7Njla4xtwuslashDtzTB0f7O3kxkwTpX7E=\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":14781,"endTime":47159,"referer":null}\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryVbyfJBPnvtGyrzXM--\r\n'

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
