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
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary0JTjQRaFxzBARnD0',
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

        data = '------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="formID"\r\n\r\n82314594184965\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q32_name[first]"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q32_name[last]"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q33_email33"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q34_phoneNumber[area]"\r\n\r\n123\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q34_phoneNumber[phone]"\r\n\r\n123123123\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q6_birthdate[month]"\r\n\r\n02\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q6_birthdate[day]"\r\n\r\n15\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q6_birthdate[year]"\r\n\r\n2023\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q16_areYou"\r\n\r\nYes\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q17_areYou17"\r\n\r\nYes\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q18_areYou18"\r\n\r\nYes\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q20_areYou20"\r\n\r\nYes\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q12_whatExcited"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q30_whyAre30"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q21_describeHow"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q22_explainHow"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q23_howHave"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q24_describeWhat"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q26_describeYour26"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q27_whatAre"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="q28_isThere"\r\n\r\ntest\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="website"\r\n\r\n\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="simple_spc"\r\n\r\n82314594184965-82314594184965\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="event_id"\r\n\r\n1676982680135_82314594184965_umXQAHl\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="temp_upload_folder"\r\n\r\n82314594184965_63f4b9984a1de\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0\r\nContent-Disposition: form-data; name="validatedRequiredFieldIDs"\r\n\r\n{"id_32":true,"id_33":true,"id_34":true,"id_6":true,"id_16":true,"id_17":true,"id_18":true,"id_20":true,"id_12":true,"id_30":true,"id_21":true,"id_22":true,"id_23":true,"id_24":true,"id_26":true,"id_27":true,"id_28":true}\r\n------WebKitFormBoundary0JTjQRaFxzBARnD0--\r\n'
        data = data.replace('1676982680135_82314594184965_umXQAHl', event_id)
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post('https://submit.jotformpro.com/submit/82314594184965/',
                                 headers=headers, data=data.encode(), proxies=self.get_proxies(), timeout=10,
                                 verify=False)

        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you!')

    with ThreadPoolExecutor(10) as worker:
        results = worker.map(spam.send_post, ['wezxasqw@gmail.com' for _ in range(15)])
    # if any(results):
    #     spam.run_concurrently(60)


if __name__ == '__main__':
    main()
