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
        'https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'wonderpaws.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarym1B98aoph9c4GvKR',
        # 'cookie': 'ep202=dsIIpL0lwuMNvJqjw+KG4xBhNGc=; wuConfirmPage=1; _ga=GA1.2.1459898289.1676391314; _gcl_au=1.1.882066834.1676391315; _fbp=fb.1.1676391314559.341238326; gdpr_consent=true; _gid=GA1.2.85613651.1676537907; ep201=Old4Az2c2QswpZglfMxu5cgbxa0=; wutm=dXRtX3NvdXJjZT1nb29nbGUmdXRtX21lZGl1bT1jJnV0bV9jYW1wYWlnbj0yMF9XdWZvb19XRl9CUl9ST1dfRU5fQ29yZV9QaHJhc2VfWCZ1dG1fY29udGVudD1XRl9CUl9ST1dfRU5fQ29yZV9YJnV0bV90ZXJtPSUyQnd1Zm9vJnNlYXJjaF9lbmdpbmU9R29vZ2xl; _gac_UA-621688-1=1.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; _gcl_aw=GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; _gcl_dc=GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; apex__wid=0Kd6T0Zj2JLyTzRVVzYNVVOVhCwIvBv_2F1lVLyE7CJY9BmaUpwX_2FiJVNqkLrDP7mLMaVDmHSLuFyo4z_2B0VxI7wcQZ96zS04_2FvjIiMtRA_2FB_2FWTyzqEbokg24jlhHKLapRURe09J14DBAZs76eLKfMmzvqQjmTxgd48R37SqDXhfN7JvHpgR509iotCV3c_2B8PhtUE60S_2BdkPPilGI9yGEz4hbbtcgkpHQBs3x4vBV5PAOI_3D; cfu=UserID%3D4078596; wuSecureCookie=%10%16%82%CA%23%BD%0D%18ltX%21%AA%BD%8A%E7; wuSignup=3; wufooPricing=wezxasqw_17_annual; submission-wezxasqw-1=submitted; mp_8bd87105f3c26c252ac6f6cb83860a26_mixpanel=%7B%22distinct_id%22%3A%20%223806406%22%2C%22%24device_id%22%3A%20%221865a63cc003f8-0b39e08f8b80c7-26031951-1fa400-1865a63cc011554%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsecure.wufoo.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22secure.wufoo.com%22%2C%22%24user_id%22%3A%20%223806406%22%2C%22Profile%20ID%22%3A%203806406%2C%22User%20ID%22%3A%204078596%2C%22Plan%20Type%22%3A%20%22Free%22%2C%22Plan%20ID%22%3A%2017%2C%22Billing%20Frequency%22%3A%201%7D; PHPSESSID=b8gdqpag7k1grr37vlnn4fc0dsirfms5; wuNewFormRedirect=%7B%22redirectParams%22%3A%22%22%7D; submission-wezxasqw-2=submitted; _uetsid=138ac000add811eda7ea7dca5a7dfa7c; _uetvid=cf777bd0ac7411edaa97494ab2e8e1e5; _splunk_rum_sid=%7B%22id%22%3A%228415e27e4a7e8403496f3a5c767f6cf1%22%2C%22startTime%22%3A1676556442437%7D; submission-beepdynasty-13=submitted; submission-wonderpaws-6=submitted; wuentry=m-207-c-123066; submission-girlscoutshh-120=submitted; submission-racrj-817=submitted; OptanonAlertBoxClosed=2023-02-16T14:12:44.618Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+16+2023+16%3A12%3A45+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=b5cc151a-5164-4382-b243-7d61ad56d9c1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=UA%3B30; endpage=%7B%22Username%22%3A%22girlscoutshh%22%2C%22FormHash%22%3A%22zwvwccg07ilthj%22%7D',
        'origin': 'https://wonderpaws.wufoo.com',
        'referer': 'https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/',
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

    data = '------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field4"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field5"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field6"\r\n\r\nfield\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field7"\r\n\r\nfield\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field8"\r\n\r\nfield\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field9"\r\n\r\nfield\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field10"\r\n\r\n01326\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field11"\r\n\r\nUnited States\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field12"\r\n\r\n123\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field12-1"\r\n\r\n231\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field12-2"\r\n\r\n2311\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field13"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field58"\r\n\r\n123125412\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field15"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field16"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field17"\r\n\r\n32\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field18"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field19"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field20"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field20"\r\n\r\nOwn\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field22"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field23"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field23"\r\n\r\nYes, someone smokes inside my home\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field24"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field24"\r\n\r\nYes\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field25"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field25"\r\n\r\nIn-person visit\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field27"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field27"\r\n\r\nDog or dogs\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field28"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field56"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field29"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field30"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field30"\r\n\r\nYes\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field31"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field33"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field33"\r\n\r\nExpanding human family (e.g. having a baby)\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field34"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field34"\r\n\r\nExpanding human family (e.g. having a baby)\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field35"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field36"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field37"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field38"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field60"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field40"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field41"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field43"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field43"\r\n\r\nAgree\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field44"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field44"\r\n\r\nAgree\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field45"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field45"\r\n\r\nAgree\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field46"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field46"\r\n\r\nAgree\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field47"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field47"\r\n\r\nAgree\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field48"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field48"\r\n\r\nAgree\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field49"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field49"\r\n\r\nAgree\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field50"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field51"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="Field52"\r\n\r\ntest\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\n6R5IwuBeGScA8ETVwwuBeAJlTtrvpc2deIAwuBegWcE02SEKwuslashkZU=\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":1,"startTime":3567,"endTime":71288,"referer":"https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/"}\r\n------WebKitFormBoundarym1B98aoph9c4GvKR\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarym1B98aoph9c4GvKR--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post(
        'https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/',
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Hello from the Wonde')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
