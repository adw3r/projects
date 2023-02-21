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
    # 'cookie': 'userReferer=https%3A%2F%2Fsubmit.jotformpro.com%2Fsubmit%2F31895183083965%2F; theme=tile-black; guest=guest_674c83b3ffb68a1a; language=ru-RU; _ga=GA1.2.1084685020.1676981865; _gid=GA1.2.1448339605.1676981865; last_form=30576733176964',
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
        form_id = '51172089377966'
        event_id = f'{timestamp}_{form_id}_{module.generate_text(7)}'
        data = {
            'formID': '51172089377966',
            'q2_associateName2': self.get_text(),
            'q3_associateEmail3': target,
            'q5_directSupervisor5': self.get_text(),
            'q6_directSupervisor6': target,
            'q8_datesFor8': self.get_text(),
            'q10_correctionTo10': self.get_text(),
            'q12_reasonFor12': self.get_text(),
            'website': '',
            'simple_spc': '51172089377966-51172089377966',
            'event_id': event_id,
            'validatedRequiredFieldIDs': '{"id_2":true,"id_3":true,"id_5":true,"id_6":true,"id_8":true,"id_10":true,"id_12":true}',
        }

        response = requests.post('https://submit.jotformpro.com/submit/51172089377966/', headers=headers, data=data,
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
