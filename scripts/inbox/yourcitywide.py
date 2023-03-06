from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'fm_cookie_0e03f9161744001271408a1707738c95': '0e03f9161744001271408a1707738c95',
            '_gcl_au': '1.1.2062797127.1678103416',
            '_gid': 'GA1.2.1685666589.1678103417',
            '_fbp': 'fb.1.1678103417853.1041013547',
            'st_ChatWidgetStatus': '2|1|0',
            '_gat': '1',
            '_ga': 'GA1.2.955025094.1678103416',
            '_ga_EQY0L7HQPH': 'GS1.1.1678103416.1.1.1678103627.35.0.0',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryt0rANfYAscVthcax',
            # 'Cookie': 'fm_cookie_0e03f9161744001271408a1707738c95=0e03f9161744001271408a1707738c95; _gcl_au=1.1.2062797127.1678103416; _gid=GA1.2.1685666589.1678103417; _fbp=fb.1.1678103417853.1041013547; st_ChatWidgetStatus=2|1|0; _gat=1; _ga=GA1.2.955025094.1678103416; _ga_EQY0L7HQPH=GS1.1.1678103416.1.1.1678103627.35.0.0',
            'Origin': 'https://www.yourcitywide.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.yourcitywide.com/refer-a-friend/',
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
            'action': 'fm_submit_form',
            'current_id': '8',
            'formType': 'embedded',
        }

        data = '------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="fm_page_id8"\r\n\r\n1231\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="fm_current_post_type8"\r\n\r\npage\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="counter8"\r\n\r\n6\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="Itemid8"\r\n\r\n\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="fm_shake8"\r\n\r\n1\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="fm_empty_field_validation8"\r\n\r\nbd736efb144d599cf463541431fbf5c4\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="wdform_2_element_first8"\r\n\r\ntest\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="wdform_2_element_last8"\r\n\r\ntest\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="wdform_4_element8"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="wdform_3_element_first8"\r\n\r\ntest\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="wdform_3_element_last8"\r\n\r\ntest\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="wdform_5_element8"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="fm-current-page"\r\n\r\nhttps://www.yourcitywide.com/refer-a-friend/\r\n------WebKitFormBoundaryt0rANfYAscVthcax\r\nContent-Disposition: form-data; name="save_or_submit8"\r\n\r\nsubmit\r\n------WebKitFormBoundaryt0rANfYAscVthcax--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post(
            'https://www.yourcitywide.com/wp-admin/admin-ajax.php',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = 'Thank you'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
