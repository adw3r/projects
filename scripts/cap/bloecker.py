from os.path import basename

import requests

from module import Spam

pageurl = 'https://www.bloecker.com/en/contact/'
googlekey = '6LcPx_AaAAAAAHS5ha0RTDc-jYruzxLND1Sba7Wt'

cookies = {
    'wp-wpml_current_language': 'en',
    '_ga': 'GA1.2.1383952794.1677056020',
    '_gid': 'GA1.2.601939935.1677056020',
    '_gat_gtag_UA_237970_2': '1',
}

headers = {
    'authority': 'www.bloecker.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'wp-wpml_current_language=en; _ga=GA1.2.1383952794.1677056020; _gid=GA1.2.601939935.1677056020; _gat_gtag_UA_237970_2=1',
    'origin': 'https://www.bloecker.com',
    'referer': 'https://www.bloecker.com/en/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        data = {
            'frm_action': 'create',
            'form_id': '10',
            'frm_hide_fields_10': '',
            'form_key': 'n37n7u22',
            'item_meta[0]': '',
            'frm_submit_entry_10': '158c6f3556',
            '_wp_http_referer': '/en/contact/',
            'item_meta[120]': self.get_text(),
            'item_meta[123]': 'Company',
            'item_meta[125]': self.get_text(),
            'item_meta[127]': self.get_text(),
            'item_meta[135]': target,
            'item_meta[137]': 'test',
            'item_meta[141][]': 'Send copy to me',
            'item_meta[133]': 'Bangladesh',
            'item_meta[143]': 'test',
            'item_meta[147][]': 'I agree that my data from this form will be collected and processed to answer my request for quotation. The data will be deleted within the legal retention periods.Note: You can revoke your consent at any time for the future by e-mail to <a href="mailto:info@bloecker.com">info@bloecker.com</a>.You can find detailed information on the handling of user data in our <a href="https://www.bloecker.com/en/privacy-policy/" target="_blank">Privacy Policy</a>.',
            'g-recaptcha-response': cap,
            'item_key': '',
            'frm_state': 'zsehzgB7f5w3SHOzdxKWlQa7APFgdF1ZBuDsH8rIBdc=',
            'action': 'frm_entries_create',
            'nonce': 'c63ce51fce',
        }

        response = requests.post('https://www.bloecker.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), '"errors":[]')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
