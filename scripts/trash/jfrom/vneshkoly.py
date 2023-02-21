from os.path import basename

import requests

from module import Spam

'''
curl 'http://vneshkoly.com.ua/kontakty.html' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: 81f30cf708470b974874c8a96a6bcdb2=f4f0978ed3701308129aa4c719df17ca; _ga=GA1.3.5907056.1676980877; _gid=GA1.3.135630560.1676980877; _gat=1; _ym_uid=1676980878275948611; _ym_d=1676980878; __gads=ID=fff59f08391bdb29-22cef7fef3dc008e:T=1676980877:RT=1676980877:S=ALNI_MbIcGNV_XpjruA72vNtE-pHPEpQTA; __gpi=UID=00000bba048fece9:T=1676980877:RT=1676980877:S=ALNI_MYjyOXRhfk-4crZdi7BCg-GzORIrQ; _ym_isad=2' \
  -H 'Origin: http://vneshkoly.com.ua' \
  -H 'Referer: http://vneshkoly.com.ua/kontakty.html' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36' \
  --data-raw 'jform%5Bcontact_name%5D=name&jform%5Bcontact_email%5D=wezxasqw%40gmail.com&jform%5Bcontact_subject%5D=test&jform%5Bcontact_message%5D=test&jform%5Bcontact_email_copy%5D=1&option=com_contact&task=contact.submit&return=&id=1%3Akontakty&fbe085df30e67f81e7d7df8945f929b0=1' \
  --compressed \
  --insecure
'''
cookies = {
    '81f30cf708470b974874c8a96a6bcdb2': 'f4f0978ed3701308129aa4c719df17ca',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'http://vneshkoly.com.ua',
    'Referer': 'http://vneshkoly.com.ua/kontakty.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            'jform[contact_name]': 'name',
            'jform[contact_email]': target,
            'jform[contact_subject]': self.get_text(),
            'jform[contact_message]': self.get_text(),
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '1:kontakty',
            'fbe085df30e67f81e7d7df8945f929b0': '1',
        }

        response = requests.post('http://vneshkoly.com.ua/kontakty.html', cookies=cookies, headers=headers, data=data,
                                 verify=False, proxies=self.get_proxies())
        print(response.text)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Спасибо за ваше письмо!')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
