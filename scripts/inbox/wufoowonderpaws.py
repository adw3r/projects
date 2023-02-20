import re
from os.path import basename

import requests

import module
from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'wonderpaws.wufoo.com',
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
        'https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/',
        headers=headers
    )
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'wonderpaws.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarymjPEnmABBZhMcOAM',
        'origin': 'https://wonderpaws.wufoo.com',
        'referer': 'https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/',
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

    data = '------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field2"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field4"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field5"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field6"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field7"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field8"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field9"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field10"\r\n\r\n12345\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field11"\r\n\r\nUnited States\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field12"\r\n\r\n123\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field12-1"\r\n\r\n123\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field12-2"\r\n\r\n4121\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field13"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field58"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field15"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field16"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field17"\r\n\r\n24\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field18"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field19"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field20"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field20"\r\n\r\nOwn\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field22"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field23"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field23"\r\n\r\nYes, someone smokes inside my home\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field24"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field24"\r\n\r\nYes\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field25"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field25"\r\n\r\nIn-person visit\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field27"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field27"\r\n\r\nDog or dogs\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field28"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field56"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field29"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field30"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field30"\r\n\r\nYes\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field31"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field33"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field33"\r\n\r\nExpanding human family (e.g. having a baby)\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field34"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field34"\r\n\r\nExpanding human family (e.g. having a baby)\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field35"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field36"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field37"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field38"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field60"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field40"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field41"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field43"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field43"\r\n\r\nAgree\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field44"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field44"\r\n\r\nAgree\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field45"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field45"\r\n\r\nAgree\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field46"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field46"\r\n\r\nAgree\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field47"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field47"\r\n\r\nAgree\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field48"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field48"\r\n\r\nAgree\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field49"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field49"\r\n\r\nAgree\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field50"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field51"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="Field52"\r\n\r\ntest\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\n6R5IwuBeGScA8ETVwwuBeAJlTtrvpc2deIAwuBegWcE02SEKwuslashkZU=\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":16544,"endTime":49121,"referer":null}\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundarymjPEnmABBZhMcOAM--\r\n'

    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target)

    response = session.post(
        'https://wonderpaws.wufoo.com/forms/we0ek1z0ax9oa8/',
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you')
    res = spam.send_post(f'wezxasqw+{module.generate_text()}@gmail.com')
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
