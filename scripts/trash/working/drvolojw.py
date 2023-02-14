from os.path import basename

import faker
import requests

import module

url = 'https://yyefqkhj.paperform.co/api/v1/form/608be2ebef9d880f44129961/submit'  # https://yesldn.org/refer/


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
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
                    'value': '12211221222',
                },
                {
                    'key': 'gtqe',
                    'value': target,
                },
                {
                    'key': 'bu23o',
                    'value': text,
                },
            ],
            'payment': None,
            'cap': None,
            'score': False,
            'partialSubmissionId': 'clb3h409t00002v6u88bsju2z',
            'deviceId': 'clb3h3djy00012v6ur4l2q1wn',
        }

        response = requests.post(url, headers=headers, json=json_data,
                                 proxies=self.get_proxies(), timeout=10
                                 )
        return response


def main():
    project_name = basename(__file__)[:-3]
    s = '"errors":null'
    spam = ConcreteSpam(
        project_name, s,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
