from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'a1kt4cfofq3qkg9ra6m9e65n25',
    '_gcl_au': '1.1.245385593.1677662275',
    '_ga': 'GA1.2.1312175809.1677662275',
    '_gid': 'GA1.2.43300875.1677662275',
    '_gat_gtag_UA_135187500_1': '1',
}

headers = {
    'authority': 'projectupdates.info',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=a1kt4cfofq3qkg9ra6m9e65n25; _gcl_au=1.1.245385593.1677662275; _ga=GA1.2.1312175809.1677662275; _gid=GA1.2.43300875.1677662275; _gat_gtag_UA_135187500_1=1',
    'origin': 'https://projectupdates.info',
    'pragma': 'no-cache',
    'referer': 'https://projectupdates.info/contact.php',
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

params = {
    'action': 'send',
}

s = 'Your message has been sent'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(False)
        data = {
            'contact_type': 'General',
            'name': text,
            'email': target,
            'message': text,
            'datefield': 'OK',
            'submitBtn': 'Send',
        }

        response = requests.post('https://projectupdates.info/contact.php', params=params, cookies=cookies,
                                 headers=headers, data=data)

        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
