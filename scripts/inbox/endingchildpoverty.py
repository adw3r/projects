from os.path import basename

import requests

from module import Spam
import requests

cookies = {
    '_gcl_au': '1.1.324156097.1677577008',
    '_gid': 'GA1.2.1453622989.1677577008',
    '_clck': '5k7c0f|1|f9i|0',
    '_ga': 'GA1.2.1968346152.1677577008',
    '_gat_UA-210964651-5': '1',
    '_clsk': '1w0y8ek|1677577223626|4|1|w.clarity.ms/collect',
    '_ga_41V22BS2J2': 'GS1.1.1677577008.1.1.1677577233.60.0.0',
}

headers = {
    'authority': 'endingchildpoverty.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarynumpVnCBhHVmKfp3',
    # 'cookie': '_gcl_au=1.1.324156097.1677577008; _gid=GA1.2.1453622989.1677577008; _clck=5k7c0f|1|f9i|0; _ga=GA1.2.1968346152.1677577008; _gat_UA-210964651-5=1; _clsk=1w0y8ek|1677577223626|4|1|w.clarity.ms/collect; _ga_41V22BS2J2=GS1.1.1677577008.1.1.1677577233.60.0.0',
    'origin': 'https://endingchildpoverty.org',
    'pragma': 'no-cache',
    'referer': 'https://endingchildpoverty.org/contact/',
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
        data = '------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="input_3"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="input_6.1"\r\n\r\nYes\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="input_7"\r\n\r\ntest\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="input_4"\r\n\r\ntest\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="is_submit_2"\r\n\r\n1\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n2\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="state_2"\r\n\r\nWyJbXSIsIjUwMWY5ODEwNTdhMDMyMTIzYzQxOTI3MzQ0NWJkZWRmIl0=\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="gform_target_page_number_2"\r\n\r\n0\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="gform_source_page_number_2"\r\n\r\n1\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\n6e91993b56dae9914c813e786f507a69\r\n------WebKitFormBoundarynumpVnCBhHVmKfp3--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post('https://endingchildpoverty.org/contact/', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())

        return response


def main():
    s = 'Thank You'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='pobcasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
