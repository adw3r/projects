from os.path import basename
from string import digits

import requests
from faker import Faker

import module
from module import Spam

headers = {
    'authority': 'submit.jotformeu.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
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
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers['user-agent'] = Faker().chrome()
        cookies = {
            'theme': 'tile-black',
            'guest': 'guest_e93e2267fa0bbca2',
            'userReferer': 'https%3A%2F%2Fform.jotformpro.com%2F',
            'language': 'ru-RU',
        }

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
            'event_id': f'{module.generate_text(13, digits)}_70802650701952_{module.generate_text(7)}',
            # 1676909260594_{formID}_VgWw7id
            'validatedRequiredFieldIDs': '{"id_3":true,"id_4":true,"id_5":true,"id_6":true,"id_10":true}',
        }

        response = requests.post('https://submit.jotformeu.com/submit/70802650701952/', headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=10,
                                 cookies=cookies
                                 )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'),
                        'https://www.bangor.ac.uk/management_centre/payment%20portal/Bafa%20Conference%20105.php.en',
                        proxy_pool_name='west_checked')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(5)


if __name__ == '__main__':
    main()
