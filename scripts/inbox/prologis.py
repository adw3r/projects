import requests

from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '_gid': 'GA1.2.1285236203.1676995503',
            'ln_or': 'eyIxMTkwODI4IjoiZCJ9',
            '_fbp': 'fb.1.1676995503484.1085769777',
            '_hjFirstSeen': '1',
            '_hjSession_249255': 'eyJpZCI6IjAzODdkMWZmLWU3NTYtNDRmMi1iOTUyLTRkN2MyNTM0Mzk4MCIsImNyZWF0ZWQiOjE2NzY5OTU1MDM1MDQsImluU2FtcGxlIjp0cnVlfQ==',
            '_hjAbsoluteSessionInProgress': '0',
            'sa-user-id': 's%253A0-e7690bed-ffcc-49d5-4278-134a18fb3e49.x7PxEsMT1ggjLL2ESA1uR2WFtSFPVmiSQpcGO2pPS0Q',
            'sa-user-id-v2': 's%253AcvmX-n9HTTBukk2ijmxTFsK3p_Q.Z3JSdEZjU59BMy2hxQJy%252B7XWmxMF3QKf5Dzm9bLS%252FmI',
            '_hjSessionUser_249255': 'eyJpZCI6IjMyMmQwY2I5LTliYzQtNTdhOS04NzIxLTJkMDJkNzVhY2NhOCIsImNyZWF0ZWQiOjE2NzY5OTU1MDI3NTUsImV4aXN0aW5nIjp0cnVlfQ==',
            '_gat_UA-16258272-1': '1',
            '_gat_UA-16258272-34': '1',
            '_ga': 'GA1.1.847341543.1676995503',
            '_hjIncludedInPageviewSample': '1',
            '_hjIncludedInSessionSample_249255': '1',
            '_ga_VXG97B1CJV': 'GS1.1.1676995503.1.1.1676996127.0.0.0',
        }

        headers = {
            'authority': 'www.prologis.be',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': '_gid=GA1.2.1285236203.1676995503; ln_or=eyIxMTkwODI4IjoiZCJ9; _fbp=fb.1.1676995503484.1085769777; _hjFirstSeen=1; _hjSession_249255=eyJpZCI6IjAzODdkMWZmLWU3NTYtNDRmMi1iOTUyLTRkN2MyNTM0Mzk4MCIsImNyZWF0ZWQiOjE2NzY5OTU1MDM1MDQsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; sa-user-id=s%253A0-e7690bed-ffcc-49d5-4278-134a18fb3e49.x7PxEsMT1ggjLL2ESA1uR2WFtSFPVmiSQpcGO2pPS0Q; sa-user-id-v2=s%253AcvmX-n9HTTBukk2ijmxTFsK3p_Q.Z3JSdEZjU59BMy2hxQJy%252B7XWmxMF3QKf5Dzm9bLS%252FmI; _hjSessionUser_249255=eyJpZCI6IjMyMmQwY2I5LTliYzQtNTdhOS04NzIxLTJkMDJkNzVhY2NhOCIsImNyZWF0ZWQiOjE2NzY5OTU1MDI3NTUsImV4aXN0aW5nIjp0cnVlfQ==; _gat_UA-16258272-1=1; _gat_UA-16258272-34=1; _ga=GA1.1.847341543.1676995503; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample_249255=1; _ga_VXG97B1CJV=GS1.1.1676995503.1.1.1676996127.0.0.0',
            'origin': 'https://www.prologis.be',
            'referer': 'https://www.prologis.be/en/contact-us',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        text = self.get_text()
        data = {
            'subject_of_interest': '656',
            'first_name': 'name',
            'last_name': 'name',
            'email': target,
            'phone': 'text',
            'subject': text,
            'message': text,
            'send_a_copy_to_me': '1',
            'op': 'Submit',
            'antibot_key': 'VvDqPbkc0RHFBKgdVaoYo5Q73KbtSQ30q0gZ2jR6ZYM',
            'form_build_id': 'form-91F8Ry_4T-zKdsxB9mV3XhZjhewTg9cza2jp1jVeU8I',
            'form_id': 'webform_submission_contact_page_node_721_add_form',
            'url': '',
        }

        response = requests.post('https://www.prologis.be/en/contact-us', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
