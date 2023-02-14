from os.path import basename

import requests

from module import Spam

cookies = {
    '_pk_id.1.5aa0': 'b69d74a9d6f96049.1675947867.',
    '_gid': 'GA1.2.972665954.1675947867',
    '_pk_ref.1.5aa0': '%5B%22%22%2C%22%22%2C1675954756%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.1.5aa0': '1',
    '_ga_WZ12NGFK8M': 'GS1.1.1675954756.2.0.1675954756.0.0.0',
    '_ga': 'GA1.2.251408673.1675947866',
    '_gat_gtag_UA_191882951_1': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://www.vast-project.eu',
    'Referer': 'https://www.vast-project.eu/contact/',
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
        cap = self.captcha_solver.solve('6Lf9AhEeAAAAAHOaEJ8K3UohXMP0XI0iDD3SdXNr',
                                        'https://www.vast-project.eu/contact/')
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
                response = requests.post('https://www.vast-project.eu/contact/', cookies=cookies, headers=headers,
                                         data=data)
                return response
            except Exception as e:
                print(e)
        return


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Your email was sent successfully. Thank you!')
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
