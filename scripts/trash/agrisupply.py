from os.path import basename

import requests

from module import Spam

pageurl = 'https://www.agrisupply.com/tellafriendpopup.aspx?p=32625'
googlekey = '6LeF5dcUAAAAAEePIBPblU6bX2QxCdx8hjBxGzK2'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        cookies = {
            'dmi': '638121399632823258',
            'visitor_domain_guid': 'agrisupply.com::www.agrisupply.com::f8b38117-4240-4098-bcf5-1af413e26475',
            'visitor_guid': 'f8b38117-4240-4098-bcf5-1af413e26475',
            '_gcl_au': '1.1.638311683.1676561164',
            '_fbp': 'fb.1.1676561164821.17007157',
            'ASP.NET_SessionId': '4gk01sxmcrnqslbqpxlhp3fg',
            'cto_bundle': 'oIPp419pTWRpVFclMkZZQzEzZ01hU1J0cVR1TFklMkZzakt1RUVkM09ycEdCeXpEYkRpY0VSc09Ed0hpdXYlMkZENEFOOVIwSTdWS3QzbWxlYUxvRHpqV2lNcFBGNldDR3JWVlJ0OTZnenclMkZkbSUyRm81MUhRSnZLcW9JaDhnbHlmUiUyQm4xRG9NbzRCZ1lIMFB2cmpqJTJGYTVOY21ldnZEJTJCZjZ3JTNEJTNE',
            '_ga_LWZKM7K91Z': 'GS1.1.1677773148.8.0.1677773148.60.0.0',
            '_ga': 'GA1.2.446932789.1676561165',
            '_gid': 'GA1.2.273049103.1677773148',
            '_dc_gtm_UA-2336362-1': '1',
            '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2NzY1NjExNjUsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuYWdyaXN1cHBseS5jb20vdGVsbGFmcmllbmRwb3B1cC5hc3B4P3A9MzI2MjUifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2Nzc3NzMxNDgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmFncmlzdXBwbHkuY29tL3RlbGxhZnJpZW5kcG9wdXAuYXNweD9wPTMyNjI1In19',
            'AWSALB': '4jIuMC0S2DnMJpX7PU7gMY9rN06pihuhL8CHIBlaDMXyRM4q/Q0kwgsT91r254kWFCWh10Gky8MZUuc4Mp0LiEbHlgNvYsXT3+E5RfM3hBT5KUR5Jxb4zz/kV05h',
            'AWSALBCORS': '4jIuMC0S2DnMJpX7PU7gMY9rN06pihuhL8CHIBlaDMXyRM4q/Q0kwgsT91r254kWFCWh10Gky8MZUuc4Mp0LiEbHlgNvYsXT3+E5RfM3hBT5KUR5Jxb4zz/kV05h',
            '_gali': 'tellafriend-fields',
        }

        headers = {
            'authority': 'www.agrisupply.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'origin': 'https://www.agrisupply.com',
            'pragma': 'no-cache',
            'referer': 'https://www.agrisupply.com/tellafriendpopup.aspx?p=32625',
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

        params = {
            'p': '32625',
        }

        data = {
            'formName': 'dmiformTellAFriend',
            'MyName': 'name',
            'MyEmail': target,
            'FriendName': 'name',
            'FriendEmail': target,
            'Message': self.get_text(),
            'g-recaptcha-response': cap,
        }

        response = requests.post(
            'https://www.agrisupply.com/tellafriendpopup.aspx',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        return response


def main():
    s = 'Thank you! An email has been sent to your friend.'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
