from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.1764815705.1676281889',
    '_fbp': 'fb.1.1676281889247.1901913783',
    'gopcookie': 'true',
    '_ga_DL0NLZXCNJ': 'GS1.1.1676281889.1.1.1676281946.0.0.0',
    '_ga': 'GA1.2.572744717.1676281889',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_gid=GA1.2.1764815705.1676281889; _fbp=fb.1.1676281889247.1901913783; gopcookie=true; _ga_DL0NLZXCNJ=GS1.1.1676281889.1.1.1676281946.0.0.0; _ga=GA1.2.572744717.1676281889',
    'Origin': 'https://www.variete.de',
    'Referer': 'https://www.variete.de/informationen/newsletter',
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
        data = {
            'action': 'setUpMail',
            'gender': 'f',
            'firstname': self.get_text(),
            'lastname': self.get_text(),
            'email': target,
            'city_nl[]': '1064057',
            'absenden': 'Subscribe now',
        }

        response = requests.post('https://www.variete.de/typo3conf/ext/qgop/typoNLBridge.php', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'success'
    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
