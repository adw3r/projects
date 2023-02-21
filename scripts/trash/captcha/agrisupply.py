from os.path import basename

import requests

from module import Spam

cookies = {
    'dmi': '638121399632823258',
    'visitor_domain_guid': 'agrisupply.com::www.agrisupply.com::f8b38117-4240-4098-bcf5-1af413e26475',
    'visitor_guid': 'f8b38117-4240-4098-bcf5-1af413e26475',
    '_gcl_au': '1.1.638311683.1676561164',
    '_fbp': 'fb.1.1676561164821.17007157',
    'ASP.NET_SessionId': 'jttotv4eazd0ghgshuthwmtk',
    'cto_bundle': 'mJwRwV9pTWRpVFclMkZZQzEzZ01hU1J0cVR1TGF4WW45JTJCelF2cDBySmJJdU5BUm9uaFY1NGR1V0VVMjlMJTJGYUdvUHloODdQV2ZFZnVMQ01yVjFUdGI1M3F0ZVRZdTNKeXRYU2NSallacW1Mdmp2YTFWNVNUaVhFRGllR2JqVE1YSGRLMVhXSHZnUVRlNVZTWGpGbEJRUkxrWEZENmclM0QlM0Q',
    'AWSALB': 'ao8d2reIxqKGHR2eFEt5MYZGRQ/az1ukR/V2px/HQx+vH5X2uRx/pEC1k+ypgz8x0hfby6SDyr2yPJOk/vdBromOqKfG7D3RZt92s54XOkmGs4NMX43sygmhHbGH',
    'AWSALBCORS': 'ao8d2reIxqKGHR2eFEt5MYZGRQ/az1ukR/V2px/HQx+vH5X2uRx/pEC1k+ypgz8x0hfby6SDyr2yPJOk/vdBromOqKfG7D3RZt92s54XOkmGs4NMX43sygmhHbGH',
    '_gid': 'GA1.2.914992460.1676977271',
    '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2NzY1NjExNjUsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuYWdyaXN1cHBseS5jb20vdGVsbGFmcmllbmRwb3B1cC5hc3B4P3A9MzI2MjUifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2NzY5NzcyNzEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmFncmlzdXBwbHkuY29tL3RlbGxhZnJpZW5kcG9wdXAuYXNweD9wPTMyNjI1In19',
    '_ga_LWZKM7K91Z': 'GS1.1.1676977271.2.0.1676977271.60.0.0',
    '_dc_gtm_UA-2336362-1': '1',
    '_ga': 'GA1.2.446932789.1676561165',
    '_gali': 'tellafriend-fields',
}

headers = {
    'authority': 'www.agrisupply.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'dmi=638121399632823258; visitor_domain_guid=agrisupply.com::www.agrisupply.com::f8b38117-4240-4098-bcf5-1af413e26475; visitor_guid=f8b38117-4240-4098-bcf5-1af413e26475; _gcl_au=1.1.638311683.1676561164; _fbp=fb.1.1676561164821.17007157; ASP.NET_SessionId=jttotv4eazd0ghgshuthwmtk; cto_bundle=mJwRwV9pTWRpVFclMkZZQzEzZ01hU1J0cVR1TGF4WW45JTJCelF2cDBySmJJdU5BUm9uaFY1NGR1V0VVMjlMJTJGYUdvUHloODdQV2ZFZnVMQ01yVjFUdGI1M3F0ZVRZdTNKeXRYU2NSallacW1Mdmp2YTFWNVNUaVhFRGllR2JqVE1YSGRLMVhXSHZnUVRlNVZTWGpGbEJRUkxrWEZENmclM0QlM0Q; AWSALB=ao8d2reIxqKGHR2eFEt5MYZGRQ/az1ukR/V2px/HQx+vH5X2uRx/pEC1k+ypgz8x0hfby6SDyr2yPJOk/vdBromOqKfG7D3RZt92s54XOkmGs4NMX43sygmhHbGH; AWSALBCORS=ao8d2reIxqKGHR2eFEt5MYZGRQ/az1ukR/V2px/HQx+vH5X2uRx/pEC1k+ypgz8x0hfby6SDyr2yPJOk/vdBromOqKfG7D3RZt92s54XOkmGs4NMX43sygmhHbGH; _gid=GA1.2.914992460.1676977271; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2NzY1NjExNjUsInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuYWdyaXN1cHBseS5jb20vdGVsbGFmcmllbmRwb3B1cC5hc3B4P3A9MzI2MjUifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2NzY5NzcyNzEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmFncmlzdXBwbHkuY29tL3RlbGxhZnJpZW5kcG9wdXAuYXNweD9wPTMyNjI1In19; _ga_LWZKM7K91Z=GS1.1.1676977271.2.0.1676977271.60.0.0; _dc_gtm_UA-2336362-1=1; _ga=GA1.2.446932789.1676561165; _gali=tellafriend-fields',
    'origin': 'https://www.agrisupply.com',
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

pageurl = 'https://www.agrisupply.com/tellafriendpopup.aspx?p=32625'
googlekey = '6LeF5dcUAAAAAEePIBPblU6bX2QxCdx8hjBxGzK2'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return

        data = {
            'formName': 'dmiformTellAFriend',
            'MyName': 'test',
            'MyEmail': target,
            'FriendName': self.get_text(),
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
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thank you! An email has been sent to your friend.')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
