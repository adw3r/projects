from os.path import basename

import requests

from module import Spam

cookies = {
    'csrftoken': 'XrMsRd2aTVJDC0gSOi6gaogzubdBsWvn3SYcCW2lrN9KXoDpSsmxgrBIKIeGGH6y',
    'sessionid': 'zvwr8lld1oagmknl2oetb5uaunucjdxg',
    '_ga': 'GA1.2.705604525.1677061859',
    '_gid': 'GA1.2.1902081697.1677061859',
    'MCPopupSubscribed': 'yes',
    'MCPopupClosed': 'yes',
    '_gat_gtag_UA_33482653_1': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryLmhjGm6EnBZiv9Ux',
    # 'Cookie': 'csrftoken=XrMsRd2aTVJDC0gSOi6gaogzubdBsWvn3SYcCW2lrN9KXoDpSsmxgrBIKIeGGH6y; sessionid=zvwr8lld1oagmknl2oetb5uaunucjdxg; _ga=GA1.2.705604525.1677061859; _gid=GA1.2.1902081697.1677061859; MCPopupSubscribed=yes; MCPopupClosed=yes; _gat_gtag_UA_33482653_1=1',
    'Origin': 'https://www.scotlime.org',
    'Referer': 'https://www.scotlime.org/contact-page/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'connection': 'keep-alive'

}

s = 'Thank you'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="csrfmiddlewaretoken"\r\n\r\nxbMk8N8hbdGZ665Rb9qBjRAvIETynf2ZDCY4Tw8sJ566rusofjGSpUVEYbUDB0Da\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="email_address"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="confirm_email_address"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="phone"\r\n\r\ntest\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="company"\r\n\r\ntest\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="i_am"\r\n\r\nA contractor\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="address"\r\n\r\ntest\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="post_town"\r\n\r\ntest\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="post_code"\r\n\r\ntest\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="message"\r\n\r\ntest\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="please_upload_any_pictures_for_us_to_help_you_with_your_enquiry_file1"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="please_upload_any_pictures_for_us_to_help_you_with_your_enquiry_file2"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="please_upload_any_pictures_for_us_to_help_you_with_your_enquiry_file3"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="please_upload_any_pictures_for_us_to_help_you_with_your_enquiry_file4"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="email_me_a_copy_of_the_message"\r\n\r\non\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux\r\nContent-Disposition: form-data; name="company_name"\r\n\r\n\r\n------WebKitFormBoundaryLmhjGm6EnBZiv9Ux--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post('https://www.scotlime.org/contact-page/', cookies=cookies, headers=headers,
                                 data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
