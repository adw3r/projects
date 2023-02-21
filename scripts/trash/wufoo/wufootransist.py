import re
from os.path import basename

import requests

import module
from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'transist.wufoo.com',
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
        'https://transist.wufoo.com/forms/p1u1c2m506y7mhk/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'transist.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryTRkRiFIIR63uLeSW',
        # 'cookie': 'ep202=dsIIpL0lwuMNvJqjw+KG4xBhNGc=; wuConfirmPage=1; _ga=GA1.2.1459898289.1676391314; _gcl_au=1.1.882066834.1676391315; _fbp=fb.1.1676391314559.341238326; gdpr_consent=true; wutm=dXRtX3NvdXJjZT1nb29nbGUmdXRtX21lZGl1bT1jJnV0bV9jYW1wYWlnbj0yMF9XdWZvb19XRl9CUl9ST1dfRU5fQ29yZV9QaHJhc2VfWCZ1dG1fY29udGVudD1XRl9CUl9ST1dfRU5fQ29yZV9YJnV0bV90ZXJtPSUyQnd1Zm9vJnNlYXJjaF9lbmdpbmU9R29vZ2xl; _gac_UA-621688-1=1.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; _gcl_aw=GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; _gcl_dc=GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; apex__wid=0Kd6T0Zj2JLyTzRVVzYNVVOVhCwIvBv_2F1lVLyE7CJY9BmaUpwX_2FiJVNqkLrDP7mLMaVDmHSLuFyo4z_2B0VxI7wcQZ96zS04_2FvjIiMtRA_2FB_2FWTyzqEbokg24jlhHKLapRURe09J14DBAZs76eLKfMmzvqQjmTxgd48R37SqDXhfN7JvHpgR509iotCV3c_2B8PhtUE60S_2BdkPPilGI9yGEz4hbbtcgkpHQBs3x4vBV5PAOI_3D; cfu=UserID%3D4078596; wuSecureCookie=%10%16%82%CA%23%BD%0D%18ltX%21%AA%BD%8A%E7; wuSignup=3; wufooPricing=wezxasqw_17_annual; mp_8bd87105f3c26c252ac6f6cb83860a26_mixpanel=%7B%22distinct_id%22%3A%20%223806406%22%2C%22%24device_id%22%3A%20%221865a63cc003f8-0b39e08f8b80c7-26031951-1fa400-1865a63cc011554%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsecure.wufoo.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22secure.wufoo.com%22%2C%22%24user_id%22%3A%20%223806406%22%2C%22Profile%20ID%22%3A%203806406%2C%22User%20ID%22%3A%204078596%2C%22Plan%20Type%22%3A%20%22Free%22%2C%22Plan%20ID%22%3A%2017%2C%22Billing%20Frequency%22%3A%201%7D; _gid=GA1.2.219761003.1676894115; ep201=3/o2enI8csnW42cj6FHWpeEC+7E=; PHPSESSID=jg7e7ulf9posus2fg6batksusuctt74v; submission-submitoffernow-1=submitted; submission-cojctn-7=submitted; submission-kissmetricsfeedback-20=submitted; _splunk_rum_sid=%7B%22id%22%3A%229e621acd36bdce36ea10767714be3044%22%2C%22startTime%22%3A1676970197813%7D; submission-modelicc-19=submitted; submission-cpsu-3=submitted; submission-newpaltz-1761=submitted; submission-transist-75=submitted; wuentry=f-1382-c-2666; OptanonAlertBoxClosed=2023-02-21T09:08:14.645Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+21+2023+11%3A08%3A15+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=b5cc151a-5164-4382-b243-7d61ad56d9c1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=UA%3B30; _uetsid=706758f0b11511ed9c8cf9868bf7d7ff; _uetvid=cf777bd0ac7411edaa97494ab2e8e1e5; endpage=%7B%22Username%22%3A%22tbeck%22%2C%22FormHash%22%3A%22ziv28de1fjg60t%22%7D; submission-tbeck-15=submitted',
        'origin': 'https://transist.wufoo.com',
        'referer': 'https://transist.wufoo.com/forms/p1u1c2m506y7mhk/',
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

    data = '------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field430"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field466"\r\n\r\n123213321213\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field468"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field482"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field483"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field268"\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field268"\r\n\r\n第一期 Batch I：06/30/14 - 09/30/14\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field242"\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field242"\r\n\r\n我希望留在现居城市继续项目开发 I\'d like to stay in my original city\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field479"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field590"\r\n\r\n移动互联创新：利用现有移动及互联网技术而挖掘的相关市场需求的方案、产品、服务; Solutions that leverage China’s mobile infrastructure to provide access to energy\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field417"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field805"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field802"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field236"\r\n\r\n自己 Personal Savings\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field689"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field418"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field421"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field808"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field807"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field697"\r\n\r\n5\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field698"\r\n\r\n5\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field699"\r\n\r\n5\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field700"\r\n\r\n5\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field701"\r\n\r\n5\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field702"\r\n\r\n5\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field693"\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field693"\r\n\r\n电子邮件 Email\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field693_other_他人推荐或其他，请说明 Others"\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="Field810"\r\n\r\ntest\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nYBhBLBLxy7XUlZLcVEqyZ5wuslashg0n5EKjDwwuslashXVntNoFaFU=\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\n提交 Submit\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":1,"startTime":2549,"endTime":36580,"referer":"https://transist.wufoo.com/forms/p1u1c2m506y7mhk/"}\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryTRkRiFIIR63uLeSW--\r\n'

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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thanks')
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    if res:
        spam.run_concurrently(80)


if __name__ == '__main__':
    main()
