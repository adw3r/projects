from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.424172082.1675781170',
    '_gat_gtag_UA_173591793_1': '1',
    '__gads': 'ID=b438ab35d5517c6e-22d4e1a9a2db00f3:T=1675781170:RT=1675781170:S=ALNI_MbtLtlLtV9ygApLMbHOSgwGRSiafQ',
    '__gpi': 'UID=00000bb14d00b61d:T=1675781170:RT=1675781170:S=ALNI_MbOdla08kMtiRTI1s8Les4I784YCA',
    '_ga_VKJQ6JH26K': 'GS1.1.1675781170.1.1.1675781181.0.0.0',
    '_ga': 'GA1.1.766031384.1675781170',
    'FCNEC': '%5B%5B%22AKsRol-IhSt3g0XhgiTXvpMl1TDNg9MQhb3jW07Y-B0krXX0pvBzVF9Z53nC9fsWNyiyJrmSurvhJ7FolTCooIoGwavAKN5MgmIXoRvsKPX0YSQlLtEJISmVurKYQvwUHtnxODlDxqmFI6DpnlpOKpJh6T7Swg3JRQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
}
headers = {
    'authority': 'yazoolife.com',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryCoA3WslZIg1RO6Zr',
    # 'cookie': '_gid=GA1.2.424172082.1675781170; _gat_gtag_UA_173591793_1=1; __gads=ID=b438ab35d5517c6e-22d4e1a9a2db00f3:T=1675781170:RT=1675781170:S=ALNI_MbtLtlLtV9ygApLMbHOSgwGRSiafQ; __gpi=UID=00000bb14d00b61d:T=1675781170:RT=1675781170:S=ALNI_MbOdla08kMtiRTI1s8Les4I784YCA; _ga_VKJQ6JH26K=GS1.1.1675781170.1.1.1675781181.0.0.0; _ga=GA1.1.766031384.1675781170; FCNEC=%5B%5B%22AKsRol-IhSt3g0XhgiTXvpMl1TDNg9MQhb3jW07Y-B0krXX0pvBzVF9Z53nC9fsWNyiyJrmSurvhJ7FolTCooIoGwavAKN5MgmIXoRvsKPX0YSQlLtEJISmVurKYQvwUHtnxODlDxqmFI6DpnlpOKpJh6T7Swg3JRQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
    'origin': 'https://yazoolife.com',
    'referer': 'https://yazoolife.com/contact',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n14\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.7.3\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f14-p12-o1\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n12\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest https://yazoolife.com/contact\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="tel"\r\n\r\ntest https://yazoolife.com/contact\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest https://yazoolife.com/contact\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7_ak_hp_textarea"\r\n\r\n\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="_wpcf7_ak_js"\r\n\r\n1675781181312\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bib"\r\n\r\n1675781183436\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bfs"\r\n\r\n1675781196397\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bkpc"\r\n\r\n32\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bkp"\r\n\r\n128;207,64;192,23;135,113;112,57;127,161;47,112;208,25;72,88;87,113;480;151,56;112,64;81;112;119,33;64,192;128,16;96,80;80,72;96,48;72,72;96,440;64,136;88,16;64,56;72,128;32,248;129,192;72,143;87,121;104,79;\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bmc"\r\n\r\n79;78,2707;80,752;88,376;104,264;79,6097;53,2516;\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bmcc"\r\n\r\n7\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bmk"\r\n\r\n21\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bck"\r\n\r\n7;27\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bmmc"\r\n\r\n3\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_btmc"\r\n\r\n0\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bsc"\r\n\r\n3\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bte"\r\n\r\n\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_btec"\r\n\r\n0\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr\r\nContent-Disposition: form-data; name="ak_bmm"\r\n\r\n1660,235;1439,155;2800,2017;\r\n------WebKitFormBoundaryCoA3WslZIg1RO6Zr--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text(target=target))
        response = requests.post(
            'https://yazoolife.com/wp-json/contact-form-7/v1/contact-forms/14/feedback',
            cookies=cookies,
            headers=headers,
            data=data.encode(), proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'mail_sent')
    res = spam.send_post()
    if res:
        spam.run_concurrently(2)


if __name__ == '__main__':
    main()
