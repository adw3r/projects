import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'divisions.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    response = session.get(
        'https://divisions.wufoo.com/forms/m1ysp6l51qpaygw/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'divisions.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarygYkpNKwyshtY6Cu4',
        'origin': 'https://divisions.wufoo.com',
        'referer': 'https://divisions.wufoo.com/forms/m1ysp6l51qpaygw/',
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

    data = '------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field322"\r\n\r\n12\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field323"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field324"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field325"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field3"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field332"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field333"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field334"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field335"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field336"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field337"\r\n\r\nAustralia\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field328"\r\n\r\n\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field328"\r\n\r\nMember ($10)\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field339"\r\n\r\n\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field339"\r\n\r\nYes\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field340"\r\n\r\n\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field340"\r\n\r\nMember ($10)\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field10"\r\n\r\nNo refunds are allowed for registration. Division 44 may record the Webinar. \r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="Field8"\r\n\r\ntest\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\no7CcRwuBePPth8qWiICzI1eEBRmYycBk87rCkuM0WLnnF0=\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":5229,"endTime":30950,"referer":null}\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarygYkpNKwyshtY6Cu4--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post(
        headers['referer'],
        headers=headers,
        data=data.encode(),
    )
    return response


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        s.proxies = self.get_proxies()
        get_resp = get(s)
        pattern = re.compile('(?<=name="idstamp" value=").*(?=" >)')
        idstamp = pattern.findall(get_resp.text)
        if not idstamp:
            return
        text = self.get_text()
        post_resp = post(s, idstamp[0], text, target)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thanks!')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
