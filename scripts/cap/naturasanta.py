from os.path import basename

import requests

from module import CapMonsterSolver, Spam

pageurl = 'https://naturasanta.ch/en/about-us/contact-us/'
googlekey = '6LdockgUAAAAANae8C0Ln0SaW1ZrXRT5rFR9dBMN'
solver = CapMonsterSolver()

cookies = {
    'cookielawinfo-checkbox-necessary': 'yes',
    'cookielawinfo-checkbox-non-necessary': 'yes',
    '_ga': 'GA1.2.1673291390.1675944291',
    '_gid': 'GA1.2.745575637.1675944291',
    '_gat_gtag_UA_118444618_1': '1',
}

headers = {
    'authority': 'naturasanta.ch',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; _ga=GA1.2.1673291390.1675944291; _gid=GA1.2.745575637.1675944291; _gat_gtag_UA_118444618_1=1',
    'origin': 'https://naturasanta.ch',
    'referer': 'https://naturasanta.ch/en/about-us/contact-us/',
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

        cap = solver.solve(googlekey, pageurl)
        if not cap:
            return
        data = {
            'contact_name': self.get_text(),
            'contact_email': target,
            'contact_subject': self.get_text(),
            'contact_message': self.get_text(),
            'contact_email_copy': '1',
            'g-recaptcha-response': cap,
            'submit': '1',
        }
        for _ in range(10):
            try:
                response = requests.post('https://naturasanta.ch/en/about-us/contact-us/', cookies=cookies,
                                         headers=headers,
                                         data=data, proxies=self.get_proxies())
                return response
            except Exception as e:
                print(e)
        return


def main():
    s = 'Your email was sent successfully. Thank you!'
    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
