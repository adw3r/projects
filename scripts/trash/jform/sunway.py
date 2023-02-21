from os.path import basename

import requests

from module import Spam
import requests

cookies = {
    'f3921aef6a5c0fe9e9ce2ebcf0adbfba': 'df1on8e9028pf1bg0ocarpbbg5',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'http://sunway-network.com',
    'Referer': 'http://sunway-network.com/contact',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'jform[contact_name]': 'test',
            'jform[contact_email]': target,
            'jform[contact_subject]': self.get_text(),
            'jform[contact_message]': self.get_text(),
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '1:contact',
            'e531b990fc5fdd27a60613a8e59ae7a7': '1',
        }

        response = requests.post('http://sunway-network.com/contact', cookies=cookies, headers=headers, data=data,
                                 verify=False, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you for your email.')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(5)


if __name__ == '__main__':
    main()
