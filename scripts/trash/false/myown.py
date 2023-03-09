from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cookies = {
            '_ym_uid': '1678181857723578279',
            '_ym_d': '1678181857',
            '_ym_isad': '2',
            'ci_session': 'BzNROAQ1AjlWeAJ3DmhSPg4%2FB2sGJlwvVmEAcAYpVT5WOwJuBg9Sa1NiUyIPMgx%2BXTJWYw9hB2AKKQZhAjZSYQBkV2FTO1BmAmNSMQNmVDMHYVE0BGcCZVZiAjMOa1I%2FDjYHMAYzXDhWMQA6BjxVZVY2AjQGZVIwUzRTIg8yDH5dMlZhD2MHYAopBjkCcFINADNXMFNrUCACZVIjAyZUJgdpUXEEOAIyVjECPg5wUjcOOwd%2FBjVca1YqADcGYlV5VmUCMAZhUiBTPVNzDzMMPF04VmoPcQcvCngGNQJyUg0AM1czU2pQPAJ0UnIDblR3B2hRMwQzAjJWOQImDh9SYA51BzgGaFwwVmUALAZvVXlWZAIgBnhSVVNvU24PbQxiXX9WIw9zBxQKXwZwAjFSYgB8V2RTNFByAldSOQM7VDIHZlE5BCICe1Y1AjAOe1IvDk4HIQZ0XDBWYQBUBj9VNVYfAmkGJFItUzNTMw8%2BDCNdO1ZmD3MHcgpABhgCVFIfAB5XeFMvUD4CaVI7AzBUJAcVUWcEYQJoVmwCLQ5yUkwOZwcjBmtcMVZhACwGa1VmVmQCLgZgUixTNlMuDzkMLV1bVjEPNQc7CnkGOQIvUmcAYVdjUyFQYQI2UnIDblR3B2hRMwQxAjlWIQJoDjNSfA57Bw4GZVw%2FVnAAagYsVT5WIAJ5BnJSOVNvUzoPOAw7XT9WaA9iB2IKOQZhAjNSZQBpVydTNVBrAjpScgMgVHcHN1FwBF0CZ1ZiAnAOM1ItDjQHIgY%2BXGxWPgAhBnhVbFYnAjoGYVIyUzxTIg98DH5dbVYiDz8HNQpsBjcCZVI2AHBXb1NmUGgCMFJrAyZUPgdjUToEOAIhVm8CZQ4hUnsOUAcwBmdcKFZtAHUGM1UjVi0CXwYgUnBTY1N2DysMNl1hVmoPYgdsCjwGaAIxUmoAY1dsUzZQYQI7Ui0%3D',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            # 'Cookie': '_ym_uid=1678181857723578279; _ym_d=1678181857; _ym_isad=2; ci_session=BzNROAQ1AjlWeAJ3DmhSPg4%2FB2sGJlwvVmEAcAYpVT5WOwJuBg9Sa1NiUyIPMgx%2BXTJWYw9hB2AKKQZhAjZSYQBkV2FTO1BmAmNSMQNmVDMHYVE0BGcCZVZiAjMOa1I%2FDjYHMAYzXDhWMQA6BjxVZVY2AjQGZVIwUzRTIg8yDH5dMlZhD2MHYAopBjkCcFINADNXMFNrUCACZVIjAyZUJgdpUXEEOAIyVjECPg5wUjcOOwd%2FBjVca1YqADcGYlV5VmUCMAZhUiBTPVNzDzMMPF04VmoPcQcvCngGNQJyUg0AM1czU2pQPAJ0UnIDblR3B2hRMwQzAjJWOQImDh9SYA51BzgGaFwwVmUALAZvVXlWZAIgBnhSVVNvU24PbQxiXX9WIw9zBxQKXwZwAjFSYgB8V2RTNFByAldSOQM7VDIHZlE5BCICe1Y1AjAOe1IvDk4HIQZ0XDBWYQBUBj9VNVYfAmkGJFItUzNTMw8%2BDCNdO1ZmD3MHcgpABhgCVFIfAB5XeFMvUD4CaVI7AzBUJAcVUWcEYQJoVmwCLQ5yUkwOZwcjBmtcMVZhACwGa1VmVmQCLgZgUixTNlMuDzkMLV1bVjEPNQc7CnkGOQIvUmcAYVdjUyFQYQI2UnIDblR3B2hRMwQxAjlWIQJoDjNSfA57Bw4GZVw%2FVnAAagYsVT5WIAJ5BnJSOVNvUzoPOAw7XT9WaA9iB2IKOQZhAjNSZQBpVydTNVBrAjpScgMgVHcHN1FwBF0CZ1ZiAnAOM1ItDjQHIgY%2BXGxWPgAhBnhVbFYnAjoGYVIyUzxTIg98DH5dbVYiDz8HNQpsBjcCZVI2AHBXb1NmUGgCMFJrAyZUPgdjUToEOAIhVm8CZQ4hUnsOUAcwBmdcKFZtAHUGM1UjVi0CXwYgUnBTY1N2DysMNl1hVmoPYgdsCjwGaAIxUmoAY1dsUzZQYQI7Ui0%3D',
            'Origin': 'http://myown.by',
            'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://myown.by/contact',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        data = {
            'forms_session': '1636544ca3736efa7909a7d59f2b4522',
            'forms_antispam1': '2952',
            'forms_antispam2': '1530',
            'forms_antispam': '5',
            'forms_name': 'name',
            'forms_email': target,
            'forms_fields[subject]': 'Добавить сайт в каталог',
            'forms_fields[0]': 'http://myown.by/contact',
            'forms_fields[1]': '123123',
            'forms_fields[2]': self.get_text(False)[:100],
            'forms_subscribe': '',
            'forms_submit': '',
        }

        response = requests.post('http://myown.by/contact', cookies=cookies, headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies(), timeout=20)
        return response


def main():
    s = 'отправлено'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
