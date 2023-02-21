from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.869619279.1676366446',
    'wiki_en_session': '0mkqdlr0itgul17um18iep633mersr4p',
    '_gid': 'GA1.2.245324328.1676978624',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.869619279.1676366446; wiki_en_session=0mkqdlr0itgul17um18iep633mersr4p; _gid=GA1.2.245324328.1676978624; _gat=1',
    'Origin': 'http://en.opasnet.org',
    'Referer': 'http://en.opasnet.org/w/Special:Contact',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}
pageurl = 'http://en.opasnet.org/w/Special:Contact'
googlekey = '6Ld-lO4SAAAAACqCXBlT5yfEffErzKktUWe_g4cE'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        data = {
            'wpFromName': 'test',
            'wpFromAddress': target,
            'wpSubject': 'text',
            'wpText': self.get_text(),
            'wpCCme': '1',
            'g-recaptcha-response': cap,
            'wpEditToken': '+\\',
            'title': 'text',
            'wpFormType': '',
        }

        response = requests.post('http://en.opasnet.org/w/Special:Contact', cookies=cookies, headers=headers, data=data,
                                 verify=False, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Your email message has been sent.')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
