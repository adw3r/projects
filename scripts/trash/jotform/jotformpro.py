from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.1526548327.1676892382',
    '_gid': 'GA1.2.1929890254.1676892382',
    '_gat': '1',
    '_gat_gtag_UA_1170872_23': '1',
}

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
        text = self.get_text()
        data = {
            'formID': '80532280738962',
            'q3_input3[first]': text,
            'q3_input3[last]': text,
            'q13_bn': text,
            'q4_eposta': text,
            'q11_birSoru11': text,
            'q12_input12': text,
            'q8_birSoru': 'ЦЕНТРАЛЬНЫЕ ХОЛОДИЛЬНЫЕ УСТАНОВКИ',
            'q9_input9': 'ПРОМЫШЛЕННАЯ ВЫПАРНЫЕ',
            'q10_birSoru10': text,
            'website': '',
            'simple_spc': '80532280738962-80532280738962',
            'event_id': '1676892396039_80532280738962_F7YEGG5',
            'validatedRequiredFieldIDs': '"No validated required fields"',
        }

        response = requests.post('https://submit.jotformpro.com/submit/80532280738962/', cookies=cookies,
                                 headers=headers, data=data)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'registered')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
