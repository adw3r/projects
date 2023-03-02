from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers = {
            'authority': 'youribiza.es',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarywVApi1gbO8SgCu7N',
            'origin': 'https://youribiza.es',
            'referer': 'https://youribiza.es/ru/favorites/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = '------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n716\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_id"\r\n\r\n4757a80\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="referer_title"\r\n\r\nVillas in Ibiza - Favorites page\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="queried_id"\r\n\r\n716\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_fields[name]"\r\n\r\ntest\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_fields[email]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_fields[destinated]"\r\n\r\nTo my friend\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_fields[friend]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_fields[friend2]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_fields[friend3]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="form_fields[messagefriend]"\r\n\r\ntest\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="action"\r\n\r\nelementor_pro_forms_send_form\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttps://youribiza.es/ru/favorites/\r\n------WebKitFormBoundarywVApi1gbO8SgCu7N--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())
        response = requests.post('https://youribiza.es/wp-admin/admin-ajax.php', headers=headers, data=data.encode(),
                                 proxies=self.get_proxies(), timeout=10)
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3])
    res = spam.send_post()
    if res:
        spam.run_concurrently(30)


if __name__ == '__main__':
    main()
