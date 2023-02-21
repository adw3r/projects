import re
from os.path import basename

import requests

import module
from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'tbeck.wufoo.com',
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
        'https://tbeck.wufoo.com/forms/application-for-tenancy/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'tbeck.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarynYiRZvCe5gEcnGGE',
        'origin': 'https://tbeck.wufoo.com',
        'referer': 'https://tbeck.wufoo.com/forms/application-for-tenancy/',
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

    data = '------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field560"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field1"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field563"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field9"\r\n\r\n132\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field9-1"\r\n\r\n123\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field9-2"\r\n\r\n3212\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field13"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field336"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field337"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field348"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field349"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field346"\r\n\r\ntesttest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field347"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field344"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field345"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field14"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field16"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field21"\r\n\r\n12\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field18"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field19"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field20"\r\n\r\n123\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field20-1"\r\n\r\n321\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field20-2"\r\n\r\n3213\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field228"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field229"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field230"\r\n\r\n213\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field230-1"\r\n\r\n321\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field230-2"\r\n\r\n2132\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field453"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field124"\r\n\r\nStudio/One Bedroom\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field224-1"\r\n\r\n12\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field224-2"\r\n\r\n12\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field224"\r\n\r\n1212\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field226"\r\n\r\nAnnual\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field456"\r\n\r\n\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field456"\r\n\r\nYes\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field457"\r\n\r\n\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field457"\r\n\r\nYes\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field459"\r\n\r\nYes\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="Field451"\r\n\r\ntest\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\ngl9dlKPK2fjUUDwuBeOAbwd6AZRVCDY2FXo79GJsfs0c9s=\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":1,"startTime":1515,"endTime":63583,"referer":"https://tbeck.wufoo.com/forms/application-for-tenancy/"}\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarynYiRZvCe5gEcnGGE--\r\n'

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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thanks ', target_pool_name='alotof')
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
