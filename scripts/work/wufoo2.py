import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'girlscoutshh.wufoo.com',
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
        'https://girlscoutshh.wufoo.com/forms/zwvwccg07ilthj/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'beepdynasty.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'origin': 'https://girlscoutshh.wufoo.com/',
        'referer': 'https://girlscoutshh.wufoo.com/forms/zwvwccg07ilthj/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryhQBFnK2rIBakNrH2',
    }

    data = '------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field139"\r\n\r\n123123\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field3"\r\n\r\n123\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field3-1"\r\n\r\n312\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field3-2"\r\n\r\n1232\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field7"\r\n\r\nMorning\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field5"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field6"\r\n\r\n\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field6"\r\n\r\nTroop Order\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field8"\r\n\r\n\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field8"\r\n\r\nShipped\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field138"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field144"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field140"\r\n\r\n\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field9"\r\n\r\nCredit/Debit\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field111"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field112"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field129"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field128"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field127"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field126"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field125"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field124"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field123"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field122"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field121"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field120"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field119"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field118"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field117"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field116"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field115"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field114"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field113"\r\n\r\ntest\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="Field142"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nU9AhDaSwuBe330bYEcYEGahHA1spTWdiF5EkfyxpVT1wdU=\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit - Enviar\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":35263,"endTime":75757,"referer":null}\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryhQBFnK2rIBakNrH2--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post(
        'https://girlscoutshh.wufoo.com/forms/zwvwccg07ilthj/',
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
