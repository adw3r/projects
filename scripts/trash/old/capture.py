import json
from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'capture-api.ap3prod.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.freely.me',
    'referer': 'https://www.freely.me/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

s = 'Thank you!'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(False)
        data = json.dumps({"s": "AGPuTNABHY88HFcBAGPuTNC_qPIO8f4ACVrTVf0nItR104-W_Q", "c": None, "ei": None,
                           "cw": {"widget_id": "6271f68bb2bb499d92003a83", "type": "widget_form_submitted",
                                  "shown_on_url": "https://www.freely.me/au/freely-referral", "attributes": [
                                   {"field_id": "str:cm:referral-email", "value": target,
                                    "merge_strategy": "override"},
                                   {"field_id": "str:cm:referral-first-name", "value": text,
                                    "merge_strategy": "override"},
                                   {"field_id": "str::email", "value": target,
                                    "merge_strategy": "override"},
                                   {"field_id": "str::first", "value": text, "merge_strategy": "override"}]},
                           "e": target, "p": None, "first": text, "last": None,
                           "h": "YIDEuo6eGE7_9AluZnJlZWx5", "u": "https://www.freely.me/au/freely-referral",
                           "t": "Freely Referral", "r": "", "l": "ru-RU", "sx": 1920, "sy": 1080, "sr": 1, "pl": None,
                           "v": 0, "ts": False, "ag": True, "tk": False, "ottlk": ""})

        response = requests.post('https://capture-api.ap3prod.com/-/events/cw-event', headers=headers, data=data)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
