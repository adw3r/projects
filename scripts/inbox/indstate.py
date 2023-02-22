from os.path import basename

import requests

from module import Spam

cookies = {
    'f5_cspm': '1234',
    'f5avraaaaaaaaaaaaaaaa_session_': 'JJNCGIFJGMDBCJDGPHOKLOJNOLMOELJMOKKAJOBLHFCFJBIKFNLMMHKADDNJDOJNHHJDJNCEPNFHOILNIKGALIPEJAOJFOJNNPCNCOGGBPAMBLALMLEGNIIOOGBMJBBA',
    'BIGipServerwww_cms_prod_pool_http': '1041196683.20480.0000',
    'cookie-agreed-version': '1.0.0',
    '_ga': 'GA1.2.764533075.1677067811',
    '_gid': 'GA1.2.1417662864.1677067811',
    'mtc_id': '900149',
    'mtc_sid': '6b524x2lk8tiqkahmb7onq3',
    'mautic_device_id': '6b524x2lk8tiqkahmb7onq3',
    'webform-17593[1677067899]': '1677067899',
    '_gat': '1',
    '_dc_gtm_UA-3112389-6': '1',
    'f5avr1797694601aaaaaaaaaaaaaaaa_cspm_': 'FMGNPNFLOPDPKPJGFBDJPBJNPKPDINJMECKMLOALGFCFJBIKFNLMMPKADDLIDOJNHHJCJNCEHKDEIHNOIKGALIPEABBPEOGLACGEJDKGBPAMBLBLIKPNBLIOOGBMJBBA',
    '_gali': 'webform-client-form-17593',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'f5_cspm=1234; f5avraaaaaaaaaaaaaaaa_session_=JJNCGIFJGMDBCJDGPHOKLOJNOLMOELJMOKKAJOBLHFCFJBIKFNLMMHKADDNJDOJNHHJDJNCEPNFHOILNIKGALIPEJAOJFOJNNPCNCOGGBPAMBLALMLEGNIIOOGBMJBBA; BIGipServerwww_cms_prod_pool_http=1041196683.20480.0000; cookie-agreed-version=1.0.0; _ga=GA1.2.764533075.1677067811; _gid=GA1.2.1417662864.1677067811; f5avraaaaaaaaaaaaaaaa_session_=MBBNGNBLJKPNFCBEPKDLKCCIPONOFGCFIBBJGOMEBDMHMPFLEBPHHNDJNLANKGIPANHDHENKLFMCCIMGLKJADMNLNANAOALKGOCBNGMHCOPNJAKNEAKAGCLIHHKHPPJI; mtc_id=900149; mtc_sid=6b524x2lk8tiqkahmb7onq3; mautic_device_id=6b524x2lk8tiqkahmb7onq3; webform-17593[1677067899]=1677067899; _gat=1; _dc_gtm_UA-3112389-6=1; f5avr1797694601aaaaaaaaaaaaaaaa_cspm_=FMGNPNFLOPDPKPJGFBDJPBJNPKPDINJMECKMLOALGFCFJBIKFNLMMPKADDLIDOJNHHJCJNCEHKDEIHNOIKGALIPEABBPEOGLACGEJDKGBPAMBLBLIKPNBLIOOGBMJBBA; _gali=webform-client-form-17593',
    'Origin': 'https://www.indstate.edu',
    'Referer': 'https://www.indstate.edu/ips/contact-form',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

s = 'Thank you, your submission has been received.'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = f'🔥Use  40 FS for a take a part on AllRight by following the ➡️ {self.promo_link} ⬅️ below Rush! This stock is limited!🔥'  # 128
        data = {
            'submitted[your_name]': 'test',
            'submitted[your_e_mail_address]': target,
            'submitted[subject]': text,
            'submitted[message]': text,
            'submitted[send_yourself_a_copy][1]': '1',
            'details[sid]': '',
            'details[page_num]': '1',
            'details[page_count]': '1',
            'details[finished]': '0',
            'form_build_id': 'form-qKVs43sD9usnGhe2zT871TIzEcJ_8Z96yqO82a-rqZQ',
            'form_id': 'webform_client_form_17593',
            'honeypot_time': 'js_token:23849296|O47Y-dk6wjdKxO2Q1n1tyKcLztC0k4TISQJW8dZAhXI|8',
            'url': '',
            'op': 'Submit',
        }

        response = requests.post('https://www.indstate.edu/ips/contact-form', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s, target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
