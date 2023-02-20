from os.path import basename

import requests

import module

cookies = {
    'PHPSESSID': '4f91b9fc3f4941514b5a4c537bd9dec3',
    '_ga': 'GA1.2.1962055330.1674812590',
    '_gid': 'GA1.2.1573071965.1674812590',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=4f91b9fc3f4941514b5a4c537bd9dec3; _ga=GA1.2.1962055330.1674812590; _gid=GA1.2.1573071965.1674812590',
    'Origin': 'https://www.marshfieldutilities.org',
    'Referer': 'https://www.marshfieldutilities.org/about-us/contact-form.php?contact=general-questions',
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
    'contact': 'general-questions',
}
key = '6LdglcQZAAAAAM7pn8YyO-MIyrgZGZhhqd25YZjH'
url = 'https://www.marshfieldutilities.org/about-us/contact-form.php?contact=general-questions'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        captcha = self.solve_captcha(url, key)
        if not captcha:
            return
        data = {
            'full_name': self.get_text(),
            'email': target,
            'subject': self.get_text(),
            'questions_comments': self.get_text(),
            'send_copy': '1',
            'g-recaptcha-response': captcha,
            'contact': 'general-questions',
        }

        response = requests.post(
            'https://www.marshfieldutilities.org/about-us/contact-form.php',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data, proxies=self.get_proxies(), timeout=10
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Your message has been sent!')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
