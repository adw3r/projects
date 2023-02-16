import json
import re
from multiprocessing import Process
from os.path import basename
from threading import Lock
from time import sleep

import requests

from module import Spam

lock = Lock()


def set_email_receiver(s, target):
    cookies = {
        'ep202': 'dsIIpL0lwuMNvJqjw+KG4xBhNGc=',
        'wuConfirmPage': '1',
        '_ga': 'GA1.2.1459898289.1676391314',
        '_gcl_au': '1.1.882066834.1676391315',
        '_fbp': 'fb.1.1676391314559.341238326',
        'gdpr_consent': 'true',
        '_gid': 'GA1.2.85613651.1676537907',
        'ep201': 'Old4Az2c2QswpZglfMxu5cgbxa0=',
        'wutm': 'dXRtX3NvdXJjZT1nb29nbGUmdXRtX21lZGl1bT1jJnV0bV9jYW1wYWlnbj0yMF9XdWZvb19XRl9CUl9ST1dfRU5fQ29yZV9QaHJhc2VfWCZ1dG1fY29udGVudD1XRl9CUl9ST1dfRU5fQ29yZV9YJnV0bV90ZXJtPSUyQnd1Zm9vJnNlYXJjaF9lbmdpbmU9R29vZ2xl',
        '_gac_UA-621688-1': '1.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB',
        '_gcl_aw': 'GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB',
        '_gcl_dc': 'GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB',
        'apex__wid': '0Kd6T0Zj2JLyTzRVVzYNVVOVhCwIvBv_2F1lVLyE7CJY9BmaUpwX_2FiJVNqkLrDP7mLMaVDmHSLuFyo4z_2B0VxI7wcQZ96zS04_2FvjIiMtRA_2FB_2FWTyzqEbokg24jlhHKLapRURe09J14DBAZs76eLKfMmzvqQjmTxgd48R37SqDXhfN7JvHpgR509iotCV3c_2B8PhtUE60S_2BdkPPilGI9yGEz4hbbtcgkpHQBs3x4vBV5PAOI_3D',
        'cfu': 'UserID%3D4078596',
        'wuSecureCookie': '%10%16%82%CA%23%BD%0D%18ltX%21%AA%BD%8A%E7',
        'wuSignup': '3',
        'wufooPricing': 'wezxasqw_17_annual',
        '_splunk_rum_sid': '%7B%22id%22%3A%22cfda314788c3f55fdbdfc19b6d431a1f%22%2C%22startTime%22%3A1676553743111%7D',
        'wuNewFormRedirect': '%7B%7D',
        'endpage': '%7B%22Username%22%3A%22wezxasqw%22%2C%22FormHash%22%3A%22zdewxk6035ie0b%22%7D',
        'submission-wezxasqw-1': 'submitted',
        'wuentry': 'z-120-x-428',
        'mp_8bd87105f3c26c252ac6f6cb83860a26_mixpanel': '%7B%22distinct_id%22%3A%20%223806406%22%2C%22%24device_id%22%3A%20%221865a63cc003f8-0b39e08f8b80c7-26031951-1fa400-1865a63cc011554%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsecure.wufoo.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22secure.wufoo.com%22%2C%22%24user_id%22%3A%20%223806406%22%2C%22Profile%20ID%22%3A%203806406%2C%22User%20ID%22%3A%204078596%2C%22Plan%20Type%22%3A%20%22Free%22%2C%22Plan%20ID%22%3A%2017%2C%22Billing%20Frequency%22%3A%201%7D',
        'PHPSESSID': 'ot24tsnk7hed4aalknhrhbuqu2h43q0j',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Feb+16+2023+15%3A40%3A38+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=b5cc151a-5164-4382-b243-7d61ad56d9c1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=UA%3B30',
        'OptanonAlertBoxClosed': '2023-02-16T13:40:38.504Z',
        '_uetsid': '138ac000add811eda7ea7dca5a7dfa7c',
        '_uetvid': 'cf777bd0ac7411edaa97494ab2e8e1e5',
    }

    headers = {
        'authority': 'wezxasqw.wufoo.com',
        'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'ep202=dsIIpL0lwuMNvJqjw+KG4xBhNGc=; wuConfirmPage=1; _ga=GA1.2.1459898289.1676391314; _gcl_au=1.1.882066834.1676391315; _fbp=fb.1.1676391314559.341238326; gdpr_consent=true; _gid=GA1.2.85613651.1676537907; ep201=Old4Az2c2QswpZglfMxu5cgbxa0=; wutm=dXRtX3NvdXJjZT1nb29nbGUmdXRtX21lZGl1bT1jJnV0bV9jYW1wYWlnbj0yMF9XdWZvb19XRl9CUl9ST1dfRU5fQ29yZV9QaHJhc2VfWCZ1dG1fY29udGVudD1XRl9CUl9ST1dfRU5fQ29yZV9YJnV0bV90ZXJtPSUyQnd1Zm9vJnNlYXJjaF9lbmdpbmU9R29vZ2xl; _gac_UA-621688-1=1.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; _gcl_aw=GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; _gcl_dc=GCL.1676553718.Cj0KCQiAxbefBhDfARIsAL4XLRq1cRi3P2hiBwNZ3PS3td81GicIuUKqS7lYE6sBsFKWFUFx-kKPPGoaAqO8EALw_wcB; apex__wid=0Kd6T0Zj2JLyTzRVVzYNVVOVhCwIvBv_2F1lVLyE7CJY9BmaUpwX_2FiJVNqkLrDP7mLMaVDmHSLuFyo4z_2B0VxI7wcQZ96zS04_2FvjIiMtRA_2FB_2FWTyzqEbokg24jlhHKLapRURe09J14DBAZs76eLKfMmzvqQjmTxgd48R37SqDXhfN7JvHpgR509iotCV3c_2B8PhtUE60S_2BdkPPilGI9yGEz4hbbtcgkpHQBs3x4vBV5PAOI_3D; cfu=UserID%3D4078596; wuSecureCookie=%10%16%82%CA%23%BD%0D%18ltX%21%AA%BD%8A%E7; wuSignup=3; wufooPricing=wezxasqw_17_annual; _splunk_rum_sid=%7B%22id%22%3A%22cfda314788c3f55fdbdfc19b6d431a1f%22%2C%22startTime%22%3A1676553743111%7D; wuNewFormRedirect=%7B%7D; endpage=%7B%22Username%22%3A%22wezxasqw%22%2C%22FormHash%22%3A%22zdewxk6035ie0b%22%7D; submission-wezxasqw-1=submitted; wuentry=z-120-x-428; mp_8bd87105f3c26c252ac6f6cb83860a26_mixpanel=%7B%22distinct_id%22%3A%20%223806406%22%2C%22%24device_id%22%3A%20%221865a63cc003f8-0b39e08f8b80c7-26031951-1fa400-1865a63cc011554%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsecure.wufoo.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22secure.wufoo.com%22%2C%22%24user_id%22%3A%20%223806406%22%2C%22Profile%20ID%22%3A%203806406%2C%22User%20ID%22%3A%204078596%2C%22Plan%20Type%22%3A%20%22Free%22%2C%22Plan%20ID%22%3A%2017%2C%22Billing%20Frequency%22%3A%201%7D; PHPSESSID=ot24tsnk7hed4aalknhrhbuqu2h43q0j; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+16+2023+15%3A40%3A38+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=b5cc151a-5164-4382-b243-7d61ad56d9c1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=UA%3B30; OptanonAlertBoxClosed=2023-02-16T13:40:38.504Z; _uetsid=138ac000add811eda7ea7dca5a7dfa7c; _uetvid=cf777bd0ac7411edaa97494ab2e8e1e5',
        'origin': 'https://wezxasqw.wufoo.com',
        'referer': 'https://wezxasqw.wufoo.com/notifications/form',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-a625813e2c29d0659b35e3953e9c1ea9-2d6e1ac39a1a705b-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-newrelic-id': 'VQIHUVRTABAFV1dQDgYEV1c=',
        'x-prototype-version': '1.7.2',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'inbox',
        'formname': 'form',
        'form': json.dumps(
            {"Email": target, "ReplyTo": "1", "EmailNewEntries": "1", "EmailNewComments": "1",
             "ConfirmationFromAddress": "Wufoo", "NotifyCcTo": target, "NotifyBccTo": target,
             "ConfirmationSubject": "TAKE YOUR CASH!", "PlainText": "0"}),
    }

    response = requests.post('https://wezxasqw.wufoo.com/notifications/index.html', cookies=cookies, headers=headers,
                             data=data)
    return response


def get(session: requests.Session):
    headers = {
        'authority': 'wezxasqw.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'referer': 'https://wezxasqw.wufoo.com/forms/form/',
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

    response = session.get('https://wezxasqw.wufoo.com/forms/form/', headers=headers)
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'wezxasqw.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary6M9hByIi7ztUbLOD',
        'origin': 'https://wezxasqw.wufoo.com',
        'referer': 'https://wezxasqw.wufoo.com/forms/untitled-form/',
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
    data = '------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="Field3"\r\n\r\ntest\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="Field1"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nLmfEVaD0K870Y1zSxeQUR36b3wuBeLKa8rJ19wuslash7VWrHwQw=\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":40295,"endTime":48112,"referer":"https://wezxasqw.wufoo.com/forms/form/"}\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundary6M9hByIi7ztUbLOD--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post('https://wezxasqw.wufoo.com/forms/form/', headers=headers,
                            data=data.encode())
    return response


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        s.proxies = self.get_proxies()
        set_email_receiver(s, target)
        get_resp = get(s)
        pattern = re.compile('(?<=name="idstamp" value=").*(?=" >)')
        idstamp = pattern.findall(get_resp.text)
        if not idstamp:
            return
        text = self.get_text()
        post_resp = post(s, idstamp[0], text, target)
        return post_resp


def delete():
    headers = {
        'authority': 'api.wufoo.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NzY1NTU1NDEsInN1Yl9kb21haW4iOiJ3ZXp4YXNxdyIsInJlbW90ZV9hZGRyIjoiODQuMjM5LjE0LjE1NCwgNjQuMjUyLjgyLjUyIiwiYWRtaW5fYWNjZXNzIjoxLCJzdWIiOiI0MDc4NTk2IiwiZW1haWwiOiJ3ZXp4YXNxd0BnbWFpbC5jb20iLCJleHAiOjE2NzY2NDE5NDEsInByb2ZpbGVfZGF0YWhvc3QiOiJkYmNvcmUxNSIsInByb2ZpbGVfZGJfbmFtZSI6IkMwMzgwNjQwNiIsInVzZXJfYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXRcLzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZVwvMTEwLjAuMC4wIFNhZmFyaVwvNTM3LjM2IiwicHJvZmlsZV9pZCI6IjM4MDY0MDYifQ.tJc5B0B04QyndmY9lhymL6mRgAzZVSVtqiAScD-ZaOaBPpAL0eSOlcJZsFKMeEsYaVMMBawCQyT-jemdadAr1Q',
        'origin': 'https://app.wufoo.com',
        'referer': 'https://app.wufoo.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'conditions': 'date_created.>=.2023/h02/h16 00:00:00-date_created.<=.2023/h02/h16 23:59:59',
    }

    response = requests.delete('https://api.wufoo.com/api/v4/forms/1/entries', params=params, headers=headers)
    return response


def main_delete():
    while True:
        print(delete().text)
        sleep(10)


def main():
    Process(target=main_delete).start()
    print('starting spam')
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thanks')
    res = spam.send_post()
    if res:
        spam.run_concurrently(150)


if __name__ == '__main__':
    main()
