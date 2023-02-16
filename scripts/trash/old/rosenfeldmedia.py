import re
from os.path import basename

import requests

from module import Spam


def post(session: requests.Session, idstamp: str, text: str, target: str):
    headers = {
        'authority': 'rosenfeldmedia.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarye4mOrRerIasOTa0g',
        # 'cookie': 'ep201=L5DimjUZWAiFcUPZKvDVH3QJJZs=; ep202=AcXdIWSQ8dT+9GAIUEvOUSQu7AI=; _splunk_rum_sid=%7B%22id%22%3A%22a2ada43e7d6d919f0500fa125a5042f5%22%2C%22startTime%22%3A1676383879354%7D; endpage=%7B%22Username%22%3A%22rosenfeldmedia%22%2C%22FormHash%22%3A%22p1lf6a8x1m49id3%22%7D; submission-rosenfeldmedia-7=submitted; wuentry=x-223-z-250579',
        'origin': 'https://rosenfeldmedia.wufoo.com',
        'referer': 'https://rosenfeldmedia.wufoo.com/forms/?formname=p1lf6a8x1m49id3&embed=1&embedKey=p1lf6a8x1m49id3783581&entsource=wordpress&referrer=',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'formname': 'p1lf6a8x1m49id3',
        'embed': '1',
        'embedKey': 'p1lf6a8x1m49id3783581',
        'entsource': 'wordpress',
        'referrer': '',
    }

    data = '------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="Field3"\r\n\r\nname\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="Field4"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="Field5"\r\n\r\ntest\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="Field6"\r\n\r\ntest\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\n4QZ2O9R2M4IiEKuF6QBXem2A0bWzPo9qVgTC4njTkh8=\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":2486,"endTime":11488,"referer":"https://rosenfeldmedia.com/"}\r\n------WebKitFormBoundarye4mOrRerIasOTa0g\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarye4mOrRerIasOTa0g--\r\n'
    data = data.replace('idstamp_field', idstamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post('https://rosenfeldmedia.wufoo.com/forms/', params=params, headers=headers,
                            data=data.encode())
    return response


def get(session: requests.Session):
    headers = {
        'authority': 'rosenfeldmedia.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://rosenfeldmedia.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'formname': 'm1tpt6r51l42aez',
        'embed': '1',
        'embedKey': 'm1tpt6r51l42aez223663',
        'entsource': 'wordpress',
        'referrer': '',
    }

    response = session.get('https://rosenfeldmedia.wufoo.com/forms/', params=params, headers=headers)
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Your message has been sent successfully',
                        target_pool_name='g11mp2')
    res = spam.send_post()
    if res:
        spam.run_concurrently(100)


if __name__ == '__main__':
    main()
