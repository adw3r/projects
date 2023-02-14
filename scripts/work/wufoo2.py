import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'tmp.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    response = session.get('https://tmp.wufoo.com/forms/z1u0o04g0czpse7/', headers=headers)
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'tmp.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryPyYpbOKWsirqCmcp',
        # 'cookie': 'ep201=L5DimjUZWAiFcUPZKvDVH3QJJZs=; ep202=AcXdIWSQ8dT+9GAIUEvOUSQu7AI=; endpage=%7B%22Username%22%3A%22rosenfeldmedia%22%2C%22FormHash%22%3A%22p1lf6a8x1m49id3%22%7D; submission-rosenfeldmedia-7=submitted; _ga=GA1.2.2015933685.1676385321; _gid=GA1.2.1337314481.1676385321; _gcl_au=1.1.242011716.1676385321; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+14+2023+16%3A35%3A21+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=78b23aaa-cc19-44d4-bbbc-5b7e21192b84&interactionCount=0&landingPath=https%3A%2F%2Fwww.wufoo.com%2F&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; _fbp=fb.1.1676385321486.1600960129; _uetsid=cf775ba0ac7411ed92815d6f991dc6b3; _uetvid=cf777bd0ac7411edaa97494ab2e8e1e5; PHPSESSID=hi4p47h36qjmfchea4up9n28qpits651; _splunk_rum_sid=%7B%22id%22%3A%2262b1dfa177b599cda848c30e990533d9%22%2C%22startTime%22%3A1676385544312%7D',
        'origin': 'https://tmp.wufoo.com',
        'referer': 'https://tmp.wufoo.com/forms/z1u0o04g0czpse7/',
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

    data = '------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="Field18"\r\n\r\n5 - Product manufacturer, service providor, vendor or supplier representative doing business with growers or others\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="Field3"\r\n\r\ntest\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="Field11"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nXS9K1dTXcmIZ6tdtdAy5PoQc6Fdk4JfKQ55IfAnWkA0=\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":21650,"endTime":31335,"referer":"https://www.google.com/"}\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryPyYpbOKWsirqCmcp--\r\n'
    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post('https://tmp.wufoo.com/forms/z1u0o04g0czpse7/', headers=headers,
                            data=data.encode())
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
    spam = ConcreteSpam('wufoo2', 'Thank you',
                        target_pool_name='pobcasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
