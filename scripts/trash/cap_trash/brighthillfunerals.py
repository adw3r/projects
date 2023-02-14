from os.path import basename

import requests

import module

googlekey = '6Lc2WPQUAAAAAPoVILNKCP10K5Usx8by6RbKgyOV'

pageurl = 'https://www.brighthillfunerals.co.uk/contact/'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey, version='v3')
        if not cap:
            return
        import requests

        cookies = {
            '_ga': 'GA1.1.1036394823.1674812574',
            '_ga_RLKD56SB8P': 'GS1.1.1675267056.2.0.1675267056.0.0.0',
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySvcFDzABVcZMZ6qJ',
            # 'Cookie': '_ga=GA1.1.1036394823.1674812574; _ga_RLKD56SB8P=GS1.1.1675267056.2.0.1675267056.0.0.0',
            'Origin': 'https://www.brighthillfunerals.co.uk',
            'Referer': 'https://www.brighthillfunerals.co.uk/contact/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = '------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[fields][0][first]"\r\n\r\ntest https://www.brighthillfunerals.co.uk/contact/\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[fields][0][last]"\r\n\r\ntest https://www.brighthillfunerals.co.uk/contact/\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[fields][1]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[fields][2]"\r\n\r\ntest https://www.brighthillfunerals.co.uk/contact/\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[recaptcha]"\r\n\r\ncap_que\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[id]"\r\n\r\n374\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[author]"\r\n\r\n0\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[post_id]"\r\n\r\n40\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="wpforms[token]"\r\n\r\n2e97ea70ccd5b97ac11c214d99ecdd68\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="action"\r\n\r\nwpforms_submit\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="page_url"\r\n\r\nhttps://www.brighthillfunerals.co.uk/contact/\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="page_title"\r\n\r\nContact\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ\r\nContent-Disposition: form-data; name="page_id"\r\n\r\n40\r\n------WebKitFormBoundarySvcFDzABVcZMZ6qJ--\r\n'.replace(
            'cap_que', cap)

        response = requests.post(
            'https://www.brighthillfunerals.co.uk/wp-admin/admin-ajax.php',
            cookies=cookies,
            headers=headers,
            data=data.encode(),
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Your email was sent successfully. Thank you!')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
