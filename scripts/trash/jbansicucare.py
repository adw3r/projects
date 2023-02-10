from os.path import basename

import requests

import module


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'http://jbansicucare.com',
            'Referer': 'http://jbansicucare.com/contact.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        text = self.get_text(target=target)
        data = {
            'name': 'name',
            'email': target,
            'phone': '12151634534',
            'subject': text,
            'message': text,
            'yourself': 'on',
            'Submit': 'Send Email',
        }

        response = requests.post(
            'http://jbansicucare.com/contact.php', headers=headers, data=data, verify=False,
            proxies=self.get_proxies(), timeout=30
        )
        return response


def main():
    project_name = basename(__file__)[:-3]
    spam = ConcreteSpam(
        project_name,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(25)


if __name__ == '__main__':
    main()
