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


def post(session, token, target, text):
    headers = {
        'authority': 'www.gulftalent.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary52fODfyeC22who2O',
        'origin': 'https://www.gulftalent.com',
        'referer': 'https://www.gulftalent.com/Register',
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
    data = '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="candidate[firstname]"\r\n\r\ntest \r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="candidate[surname]"\r\n\r\ntest \r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="candidate[CanLoc_location_current]"\r\n\r\n90229302000000\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="candidate[curr_jobpos]"\r\n\r\nRPA Developer\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="candidate[username]"\r\n\r\nwezxasqw+test@gmail.com\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="candidate[plainPassword]"\r\n\r\nLnJpJZE7yyhfW86\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="candidate[cv_file]"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="facebook_id"\r\n\r\n\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="google_id"\r\n\r\n\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="registration_path"\r\n\r\njoin\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="mailing[MailpoolPermissionTypeTwo]"\r\n\r\nYES\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="mailing[MailpoolPermissionTypeThree]"\r\n\r\nYES\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O\r\nContent-Disposition: form-data; name="mailing[_token]"\r\n\r\nmailing_token\r\n' \
           '------WebKitFormBoundary52fODfyeC22who2O--\r\n'
    data = data.replace('wezxasqw+test@gmail.com', target)
    data = data.replace('mailing_token', token)
    data = data.replace('test', text)

    response = session.post('https://www.gulftalent.com/register', headers=headers, data=data.encode(), timeout=10)
    return response


pattern = re.compile('(?<=value=").*(?=" />)')


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        s.proxies = self.get_proxies()
        get_resp = get(s)
        if not get_resp.ok:
            return
        token = pattern.findall(get_resp.text)
        if not token:
            self.logger.info(get_resp.text)
            self.logger.info(token)
            return
        post_resp = post(s, token[-1], target, self.get_text())
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Please fill out your personal information')
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
