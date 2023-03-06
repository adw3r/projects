from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryNxgwK7IHRLEixIIz',
            'Origin': 'https://connuit.com',
            'Pragma': 'no-cache',
            'Referer': 'https://connuit.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data = '------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="text"\r\n\r\ntest\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="name"\r\n\r\nname\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="email-2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="customer[id]"\r\n\r\n\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="customer[email]"\r\n\r\n\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="customer[name]"\r\n\r\n\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="page[title]"\r\n\r\nRefer a Friend\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="page[href]"\r\n\r\nhttps://connuit.com/pages/refer-a-friend\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz\r\nContent-Disposition: form-data; name="_keyLabel"\r\n\r\n{"text":"Your Name","email":"Email","name":"Your Friend\'s Name","email-2":"Your Friend\'s Email"}\r\n------WebKitFormBoundaryNxgwK7IHRLEixIIz--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text(False)).encode()

        response = requests.post('https://form.globosoftware.net//api/front/form/94315/send', headers=headers,
                                 data=data, proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = '{"success":"true"}'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
