from os.path import basename

import requests

from module import Spam

cookies = {
    '__atssc': 'google%3B1',
    '_ga': 'GA1.2.931871789.1677077210',
    '_gid': 'GA1.2.1569508652.1677077210',
    'PHPSESSID': 'e557a97a78bcab02b26ab43bbf7792a2',
    '_gat_gtag_UA_17230904_1': '1',
    '_gat_gtag_UA_234481925_1': '1',
    '__atuvc': '3%7C8',
    '__atuvs': '63f62ad80b478588002',
}

headers = {
    'authority': 'afterschoolpathfinder.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__atssc=google%3B1; _ga=GA1.2.931871789.1677077210; _gid=GA1.2.1569508652.1677077210; PHPSESSID=e557a97a78bcab02b26ab43bbf7792a2; _gat_gtag_UA_17230904_1=1; _gat_gtag_UA_234481925_1=1; __atuvc=3%7C8; __atuvs=63f62ad80b478588002',
    'origin': 'https://afterschoolpathfinder.org',
    'referer': 'https://afterschoolpathfinder.org/contact/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = {
            '_acf_screen': 'acf_form',
            '_acf_post_id': 'new_post',
            '_acf_validation': '1',
            '_acf_form': 'djZObGZyMVBEUFdHbFI0NDlEeU1ybHBvN3B3aW42bVZTU3N2WlgrUmpIc1d3SVlZcHBBalhYNm4wVm9vY0JJeHBkaFN2WUJZT0Z6NTJrMVg1NUh3eVI0dGN1M1h4ZmgzN2ttNzdXM0pIdTFGaWV0Z0dHakZOV2hVVlh3ekJ4UmY1WkhqY0F6aVpsRTBwR3o0UzJoeE1pZGZFM0FQc3R4bVUxRzF5OGVJQmd1YXpvZGttVFRMbi9JV0ZtaGI4M3NlZHMyNUhlRnFTUnRuR2lsUHB1MTAzZDErQ2E4b0p2ekNxV1dsQzNUN25XVUR6eUo2d3Z5RmpGTk1mU0ZRa3huRmY4ZEN2eEZsWWZFa3Jpdm9zZ3FkU2lQemI3elY3YmhMUDVaUzlsZDdKbVg2SVlPLzdTOWdjTjBTSFVYczQ1bDVxVit4aHFmOXBESVNiellwK0UrSWUrZWM4dlVqZFUrTXZxcThjUVdKSzVqTjhORGJleHh1eVVPVTNrME1EeEh4NUVhOUNhU0JqblRicnNyRmtLalFEd0NCOUJsaHdWWWt0NXhEdGNIdjRRdk0wUW9wY3NSaGViNUQ3cGhGY1p1SlJEVm5HNml2dlN5bXNSekY3bHhtRWMxVXdnV0VnZTF1cElTUzVzVjJZSElaeW5kUlJPZ3N6WWlXSThqcDMzeHB1bXFJQWZlMjlLa0d3ZDQ1M0YrZWRaS0d2UUVsWkVPSTZmc05jNXRCMGhKeVA2dStNZHRSZWl1N25OM2lhQ29rUFkrTVQ2MVRTM2IzVlpYYVVud1VUNkVTQnM5RmIvQXoyNzJZTVlRbFlkNEZ5MXZucys4OVJTUWpXa0loeHFRRjNRek9LdHNUOVp1SllLdVlWRHpvcmlJMEljSlZqK2NsNVhnTnRiVTRtQjM0eVhzaTJqcFZoV3Vjb2FGa3Z5alhJaTNyc3dCeUZ4dWhselhROXh1dW5UVmozNU9qS1UvMmkzOHRzRVROSi9NSGRVVG9QZ1gwY2U5S2s4eFVIMGZYZE1YMmFyYkg3cUJiVTJ2dGRuZzdRVnplVVA2bUZsMVZsZGRJR2lOVmhlc09ZcTFxSEpwUFhlREtpaVYvaVJQZjJhZFBwbkp2RnU5bXpQZ05rMFZSVzhLQVcxWkdQRjRYcGduNDBudktESk1rY1dOVHJZWEoxRFVYcStJK2U4cjc2b21teVFNa2NOTUdhSzBFM05McW9XOTkvd3IyQ283KzZ5TnUycXhuaVI4S1IzNG1vSXZrTi9XRjNRbmdQTGlrbkp0K0lqb3hrNFFLQlNKMGRjeFlIRzlhYnczbytYVVFmSC80TWszZm5RdEptR0V1YVhrRHJSZXpmWHFsaEJEYk4xcHRXM0RKakdKRGxvSGZlaDViMERFSFF3aFpDajFpTlRUa2xhZmlPUG0rcjV2aFAzZUh0cVZ2MXJlRWdOd09yUlRhUURESC82K1pDVDhOSmpRdG1DNzM2aUlOOFRCUGdrQU1HeUdta0VXaDdDWXBEc1V4c2s0bVpQajcya2ttaVYrOVFJZDkvWHdnK3JkeU5qRm5kak5oUWJpRGZveGRpZGsyNGIxdVJ2eEdKQmpoOTVQbExOaCtwQ0RyNHZ4cDo6UxGMbQK8DtoX0NJLiuvnGw==',
            '_acf_nonce': 'aa64db39aa',
            '_acf_changed': '1',
            'contact_us_email': 'contact_us_email',
            'acf[field_617fa93560f29]': self.get_text(),  # Name
            'acf[field_617fa95b60f2a]': target,
            'acf[field_617fa96f60f2b]': 'DO NOT LOSE YOUR FREESPINS!',
            'acf[field_617fa97c60f2c]': [
                '',
                '62',
            ],
            'acf[field_617fa9b260f2d]': self.get_text(),  # message
            'acf[field_61fa129812f86]': '',
            'acf[field_61fa129812f86][]': 'Send yourself a copy',
            'acf[_validate_email]': '',
        }

        response = requests.post('https://afterschoolpathfinder.org/contact/', cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())
        return response


def main():
    s = 'Your message has been sent.'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
