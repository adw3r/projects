from os.path import basename

import faker
import requests

import module

pageurl = 'https://workroutes.co.uk/sign-up-page/'
url = 'https://hxuevil4.paperform.co/api/v1/form/5f7c65ec1d47c23a5635a8b5/submit'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        headers = {
            'user-agent': faker.Faker().chrome(),
        }
        text = self.get_text(target=target)
        json_data = {
            'data': [
                {
                    'key': '3pj7t',
                    'value': text,
                },
                {
                    'key': 'etpf0',
                    'value': text,
                },
                {
                    'key': 'a90bi',
                    'value': '12121212111',
                },
                {
                    'key': 'gtqe',
                    'value': target,
                },
                {
                    'key': 'bu23o',
                    'value': text,
                },
                {
                    'key': '699oa',
                    'value': 'Yes',
                },
            ],
            'payment': None,
            'cap': None,
            'score': False,
            'partialSubmissionId': 'cld0fu1rq0000356tn6p2emz2',
            'deviceId': 'cld0fu1rr0001356tn1mf7iwj',
        }

        response = requests.post(url, headers=headers, json=json_data,
                                 proxies=self.get_proxies(), timeout=10
                                 )
        return response


def main():
    success_message = '"errors":null'

    spam = ConcreteSpam(
        basename(__file__)[:-3], success_message,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
