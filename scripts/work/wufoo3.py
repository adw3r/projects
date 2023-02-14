import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'educatorpreparation.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'ep202=dsIIpL0lwuMNvJqjw+KG4xBhNGc=; submission-kaffessamusic-2=submitted; submission-generalbaptist-1=submitted; ep201=WyjRUIFRcr+AfbHPh/JTjgzSSbw=; submission-odoc-1=submitted; submission-louisvilleky-1273=submitted; submission-scicommjc-1=submitted; wuConfirmPage=1; _ga=GA1.2.1459898289.1676391314; _gid=GA1.2.763602989.1676391314; _gcl_au=1.1.882066834.1676391315; _fbp=fb.1.1676391314559.341238326; _uetsid=cf775ba0ac7411ed92815d6f991dc6b3; _uetvid=cf777bd0ac7411edaa97494ab2e8e1e5; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+14+2023+18%3A15%3A15+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=b5cc151a-5164-4382-b243-7d61ad56d9c1&interactionCount=1&landingPath=https%3A%2F%2Fwww.wufoo.com%2Fendpage%2F&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1; endpage=%7B%22Username%22%3A%22educatorpreparation%22%2C%22FormHash%22%3A%22z1pzy0q41k6xwb7%22%7D; submission-educatorpreparation-19=submitted; wuentry=z-426-f-1103',
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

    response = session.get('https://educatorpreparation.wufoo.com/forms/z1pzy0q41k6xwb7/', headers=headers)
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'educatorpreparation.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryLc4x61Tix7TOTMqB',
        'origin': 'https://educatorpreparation.wufoo.com',
        'referer': 'https://educatorpreparation.wufoo.com/forms/z1pzy0q41k6xwb7/',
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

    data = '------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field116"\r\n\r\n\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field116"\r\n\r\nMrs.\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field116_other_Other"\r\n\r\n\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field3"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field9"\r\n\r\n\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field9"\r\n\r\nK-12 Math Teacher\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field9_other_Other"\r\n\r\n\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field118"\r\n\r\n\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="Field118"\r\n\r\nYes\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nwuslashgqYvEzwuslashPNRovUDehrIZ81B3TrWMDokwuslashQmr4iIJ22vM=\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":30122,"endTime":41585,"referer":"https://www.google.com/"}\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryLc4x61Tix7TOTMqB--\r\n'
    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target).encode()

    response = session.post(
        'https://educatorpreparation.wufoo.com/forms/z1pzy0q41k6xwb7/',
        headers=headers,
        data=data,
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thanks for')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
