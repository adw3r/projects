from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            'fe_typo_user': 'eedef1d04e77571ed91da2eb2811ec3e',
            '__ss': '1678096144665',
            '_ga': 'GA1.2.677342392.1678096145',
            '_gid': 'GA1.2.992084098.1678096145',
            '__ss_tk': '202303%7C6405b712474f79385a136b3b',
            '_gat_UA-69558560-1': '1',
            '__ss_referrer': 'https%3A//us.index-traub.com/en_us/company/contact/',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryjbgaD1FgyTN1fzIS',
            # 'Cookie': 'fe_typo_user=eedef1d04e77571ed91da2eb2811ec3e; __ss=1678096144665; _ga=GA1.2.677342392.1678096145; _gid=GA1.2.992084098.1678096145; __ss_tk=202303%7C6405b712474f79385a136b3b; _gat_UA-69558560-1=1; __ss_referrer=https%3A//us.index-traub.com/en_us/company/contact/',
            'Origin': 'https://us.index-traub.com',
            'Pragma': 'no-cache',
            'Referer': 'https://us.index-traub.com/en_us/company/contact/',
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

        params = {
            'tx_form_formframework[action]': 'perform',
            'tx_form_formframework[controller]': 'FormFrontend',
            'cHash': 'b4c586543103567e9554a0f5d547c9ec',
        }

        data = '------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][__state]"\r\n\r\nTzozOToiVFlQTzNcQ01TXEZvcm1cRG9tYWluXFJ1bnRpbWVcRm9ybVN0YXRlIjoyOntzOjI1OiIAKgBsYXN0RGlzcGxheWVkUGFnZUluZGV4IjtpOjA7czoxMzoiACoAZm9ybVZhbHVlcyI7YTowOnt9fQ==480bb591d10d4bc88e22201dfb330ee480b93eea\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[__trustedProperties]"\r\n\r\n{"contactEN-68354":{"singleselect-1":1,"hidden-1":1,"singleselect-2":1,"text-1":1,"Gfi6h4cO1YP0AoSDIbNdq5Xe":1,"text-3":1,"text-2":1,"text-4":1,"countries-1":1,"text-5":1,"text-6":1,"telephone-1":1,"email-1":1,"checkbox-1":1,"linkcheckbox-1":1,"textarea-1":1,"__currentPage":1}}5eab2dbe692fdac74f3b8c824a8dcde982c303b7\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][singleselect-1]"\r\n\r\nmachine\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][hidden-1]"\r\n\r\n\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][singleselect-2]"\r\n\r\nmale\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][text-1]"\r\n\r\ntest\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][Gfi6h4cO1YP0AoSDIbNdq5Xe]"\r\n\r\n\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][text-3]"\r\n\r\ntest\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][text-2]"\r\n\r\ntest\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][text-4]"\r\n\r\n12311\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][countries-1]"\r\n\r\n\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][text-5]"\r\n\r\ntest\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][text-6]"\r\n\r\ntest\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][telephone-1]"\r\n\r\n123123\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][email-1]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][checkbox-1]"\r\n\r\n\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][checkbox-1]"\r\n\r\n1\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][linkcheckbox-1]"\r\n\r\n\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][linkcheckbox-1]"\r\n\r\n1\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][textarea-1]"\r\n\r\ntest\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-68354][__currentPage]"\r\n\r\n1\r\n------WebKitFormBoundaryjbgaD1FgyTN1fzIS--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post(
            'https://us.index-traub.com/en_us/company/contact',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = 'Thank You'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
