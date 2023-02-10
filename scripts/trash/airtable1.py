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

    response = s.get('https://airtable.com/shrdWpC8lS0p04YPG', headers=headers)
    return response


def post(s, request_id, csrf, target, text):
    headers = {
        'authority': 'airtable.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'brw=brwlyqBDPE4UoyHxu; _gcl_au=1.1.883751192.1675691956; optimizelyEndUserId=oeu1675691956065r0.44241685422052823; _mkto_trk=id:458-JHQ-131&token:_mch-airtable.com-1675691956429-83839; mv=eyJzdGFydFRpbWUiOiIyMDIzLTAyLTA4VDE2OjEzOjEzLjEwOFoiLCJsb2NhdGlvbiI6Imh0dHBzOi8vYWlydGFibGUuY29tL3NoclJFREFDVEVEMDAwMDAwIiwiaW50ZXJuYWxUcmFjZUlkIjoidHJjdEVlQ3RiM3Z0cDhkcmMifQ==; amplitude_id_01c5c9182d4beaee719619af5db39310airtable.com=eyJkZXZpY2VJZCI6Ijg0ZjA5NDczLTJkMmUtNDY5Yy05MzNkLWVjMmFkOWVhOGExOFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NTg3MjgxMjM5MSwibGFzdEV2ZW50VGltZSI6MTY3NTg3MjgxMjM5MiwiZXZlbnRJZCI6MiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjJ9; pxcts=89baa4b7-a7cb-11ed-87a4-52734d796d58; _pxvid=89ba979f-a7cb-11ed-87a4-52734d796d58; _pxff_fp=1; _px3=a3c51b37387c4ecc1d968ab4fa60b93043ebf4ea3d003551fac363e56df0bcdd:5yNqQYLtU1vSWs8yPAR5MNZQDu3r1Bmvl3Qlm/hjTdUgROjuKgfCkmfT9z+EqdwTUj3ZmO6EQZBTK2bBLo/tYQ==:1000:M7ZMDeQ1MNGtyHzpqjtCHd5S6eyLSolzBr79SfMC+SMHxn32cQwxqJmKcN1qfawWcpft50ZT9MerxczNfS99Ynh5gSHDs78SJ59GI76SXv+sf5r1WQZKZfvP4gMPOECocLQ+23AGYpwLbj12R8Y//HkfH0lcUR9bv1WIfiu5Z3aOUGBnBrfNtsK58T77SNxNyu42HbSlXzvYfftsEtMwJQ==; login-status-p=1; localePref=auto; userSignature=usrvgYwOGDFbzGoDQ2023-02-08T16:13:40.000Z; userSignature.sig=FFRiT6y5nQnoxAJPE87dQOmV_YVJGbQKom27QrcXWVo; __Host-airtable-session=eyJzZXNzaW9uSWQiOiJzZXNub1gyZXpTN3NqbUtHMSIsImNzcmZTZWNyZXQiOiJ5R1dWWHJvMXdTOFdsXzV1TElCc28yamYiLCJoaWdoU2VjdXJpdHlNb2RlRW5hYmxlZFRpbWUiOjE2NzU4NzI4MjcxOTIsInVzZXJJZCI6InVzcnZnWXdPR0RGYnpHb0RRIiwibG9nZ2VkSW5UaW1lIjoiMjAyMy0wMi0wOFQxNjoxMzo0Ny4yMzJaIn0=; __Host-airtable-session.sig=Bw_IuU2fh-pSQxqcHeWG5nfk66X_Injp-9uVI25bPak; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Feb+08+2023+18%3A13%3A49+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=c0401062-9294-43a1-bdb0-4381f22fc04d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false; AWSALB=VCQ5WZkRI+nj0xPbV2IPCHVRFaMvgn54o4Pf/1hHoFx2tG00ZfAatagioqa8duNMsMLP9EU0MWK1CBJ5A1RqFKA9HXHn5TCUIZ61Jcce0IR7AMlvintK41UJYm4N; AWSALBCORS=VCQ5WZkRI+nj0xPbV2IPCHVRFaMvgn54o4Pf/1hHoFx2tG00ZfAatagioqa8duNMsMLP9EU0MWK1CBJ5A1RqFKA9HXHn5TCUIZ61Jcce0IR7AMlvintK41UJYm4N; mbpg=2024-02-08T16:14:12.559ZusrvgYwOGDFbzGoDQpro; mbpg.sig=7PiEINEKjhVaRdECHUl6bAPzktuDVEC0ky2Kd65TGmk',
        'dnt': '1',
        'origin': 'https://airtable.com',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-airtable-application-id': 'appM8yk3pNsXzZA8b',
        'x-airtable-client-queue-time': '4.399999976158142',
        'x-airtable-inter-service-client': 'webClient',
        'x-airtable-inter-service-client-code-version': 'cb4c7f95baa0cb87e96ea315913db88ec54764f7',
        'x-airtable-page-load-id': 'pglnk8wzwXI9vPT2g',
        'x-requested-with': 'XMLHttpRequest',
        'x-time-zone': 'Europe/Kiev',
        'x-user-locale': 'en',
    }

    data = {
        'stringifiedObjectParams': '{"rowId":"recsKOBqGqjhEj2qm","cellValuesByColumnId":{"fldZcf4N3hJv1YpCq":"test"},"userEmailForCopyOfFormSubmission":"wezxasqw@gmail.com"}'.replace(
            'wezxasqw@gmail.com', target).replace('test', text),
        'requestId': request_id,
        'accessPolicy': '{"allowedActions":[{"modelClassName":"view","modelIdSelector":"viwlU5NHONRdoqW28","action":"readSharedFormData"},{"modelClassName":"view","modelIdSelector":"viwlU5NHONRdoqW28","action":"submitSharedForm"},{"modelClassName":"application","modelIdSelector":"app0SYsNkT1fwUhQz","action":"createAttachmentUploadS3Policies"}],"shareId":"shrdWpC8lS0p04YPG","applicationId":"app0SYsNkT1fwUhQz","generationNumber":0,"expires":"2023-03-02T00:00:00.000Z","signature":"6bc53aa9f48b84d4097600d4b2728e838bc276d8af7437072bca37652c9654cd"}',
        '_csrf': csrf,
    }
    response = s.post(
        'https://airtable.com/v0.3/view/viwJzRAEN9363f4kf/submitSharedForm',
        headers=headers,
        data=data,
    )
    return response


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        get_proxies = self.get_proxies()
        s.proxies = get_proxies
        get_resp = get(s)
        csrf = csrf_pattern.search(get_resp.text)
        request_id = request_id_pattern.search(get_resp.text)
        post_resp = post(s, request_id, csrf, target, self.get_text(target=target))
        return post_resp


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], '"msg":"SUCCESS"', target_pool_name='turk')
    res = spam.send_post()
    if res:
        spam.run_concurrently(80)


if __name__ == '__main__':
    main()
