from os.path import basename

import requests

import module
from module import CapMonsterSolver
from module import Spam

pageurl = 'https://www.schedur.com/en/users'

goolekey = '6LfTwfsSAAAAALRwwCIOC9DVRkQ_E8O_ULGcAM2H'

cookies = {
    '_ga': 'GA1.2.1592672414.1675943069',
    '_gid': 'GA1.2.768380611.1675943069',
    '_schedulemailer_session': 'T2dSWXlhcEFPanlwQ0kyeGE5a09rT2pTeHdhcTJRWkprb3FCQmVmSHkxMWkvNzFJRXRUbUZaRXFHTVdKTEZVb1g2MXBLWHVSY0l6RkZOZmNKMm1vZ3IwQUoxeWxyVklmUVdJSXhtVEMxMHZ2V2IzcUN0YkJHYlJwbkVIelBLNTMvRmF1UXFLVStVYWFpdzNBOWtsOGpTZUpPZE5LNmxUdWx1VTFkd3ZSTHNkRTNQTE9vUDNpMCtJdUV1Q2IrM2FoTjhiTTg5Wkl0U25mYmZkRFo3ME42THRTVXFuLzB0Y3o0eDhINFZNRVhETDFOeGF0cW5NVEgwUUxmYlhnbCs0NmszMDNRUGlWQXd4WnM2d0xVd0VSWVpEYWZKM05jV01Xa0cyWEdBV1cwcXNqdnd0UG44WGlzbm5nRWlsNVJQODl0TEsxaVRSY1VwZ2Ivc242RjcvTnFRPT0tLU52NHN3VTFNSDJ3NDNSbjNQeEJyQ3c9PQ%3D%3D--6472bf07cdfcfccebf22f875a94eb792005b5a9e',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.1592672414.1675943069; _gid=GA1.2.768380611.1675943069; _schedulemailer_session=T2dSWXlhcEFPanlwQ0kyeGE5a09rT2pTeHdhcTJRWkprb3FCQmVmSHkxMWkvNzFJRXRUbUZaRXFHTVdKTEZVb1g2MXBLWHVSY0l6RkZOZmNKMm1vZ3IwQUoxeWxyVklmUVdJSXhtVEMxMHZ2V2IzcUN0YkJHYlJwbkVIelBLNTMvRmF1UXFLVStVYWFpdzNBOWtsOGpTZUpPZE5LNmxUdWx1VTFkd3ZSTHNkRTNQTE9vUDNpMCtJdUV1Q2IrM2FoTjhiTTg5Wkl0U25mYmZkRFo3ME42THRTVXFuLzB0Y3o0eDhINFZNRVhETDFOeGF0cW5NVEgwUUxmYlhnbCs0NmszMDNRUGlWQXd4WnM2d0xVd0VSWVpEYWZKM05jV01Xa0cyWEdBV1cwcXNqdnd0UG44WGlzbm5nRWlsNVJQODl0TEsxaVRSY1VwZ2Ivc242RjcvTnFRPT0tLU52NHN3VTFNSDJ3NDNSbjNQeEJyQ3c9PQ%3D%3D--6472bf07cdfcfccebf22f875a94eb792005b5a9e',
    'Origin': 'https://www.schedur.com',
    'Referer': 'https://www.schedur.com/en/signup',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

solver = CapMonsterSolver()


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = solver.solve(goolekey, pageurl)
        if not cap:
            return
        data = {
            'utf8': '✓',
            'authenticity_token': '5yP8fxdffChsPt8mrI+WvekkVPavARQR8HdtniZcws1Q/74LvrUzK6HAwQVrgIsVq5wOibuZYkO+t3yV91gmEw==',
            'user[name]': self.get_text(),
            'user[email]': target,
            'user[password]': 'ASdqwr125hjfyj',
            'user[password_confirmation]': 'ASdqwr125hjfyj',
            'g-recaptcha-response': cap,
            'user[terms_of_service]': [
                '0',
                '1',
            ],
            'commit': 'Create account',
        }
        for _ in range(10):
            try:
                response = requests.post('https://www.schedur.com/en/users', cookies=cookies, headers=headers,
                                         data=data, proxies=self.get_proxies())
                return response
            except Exception as e:
                print(e)
        return


def main():
    s = 'you have received a confirmation email'
    spam = ConcreteSpam(basename(__file__)[:-3], s)
    target = f'wezxasqw+{module.generate_text(10)}@gmail.com'
    res = spam.send_post(target)
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
