from os.path import basename

import requests

from module import Spam

cookies = {
    'NSC_JOwksol2ewlhc5se3isuc1ehdvgzmb3': 'ffffffff090c69aa45525d5f4f58455e445a4a423660',
    '_ga': 'GA1.2.2089433658.1676898772',
    '_gid': 'GA1.2.1779150686.1676898772',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary2B4E9RWPT4t5T2Uq',
    # 'Cookie': 'NSC_JOwksol2ewlhc5se3isuc1ehdvgzmb3=ffffffff090c69aa45525d5f4f58455e445a4a423660; _ga=GA1.2.2089433658.1676898772; _gid=GA1.2.1779150686.1676898772; _gat=1',
    'Origin': 'https://sharc-research.org',
    'Referer': 'https://sharc-research.org/training/professional-development-program-pdp/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_1"\r\n\r\ntest\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_4"\r\n\r\ntest\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_12"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_5"\r\n\r\nCompleted\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n131072000\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_6"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n131072000\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_7"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_8.4"\r\n\r\nFlorida Cohort Group\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_10"\r\n\r\nMACS/WIHS Writing Group\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="input_11"\r\n\r\nYes\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="is_submit_19"\r\n\r\n1\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n19\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="state_19"\r\n\r\nWyJ7XCI1XCI6W1wiZTkyMzA1MjlkOTUzNmQ5ZDhlMmMxNWRlMGU1ZTFlYmFcIixcImUwYzYxYWJjMzhjMGU2MzlmM2FjODk1ODk5ZDQ5MDQxXCIsXCJlMjI1OWY0NTUxZTRjOTBlZTgwNWNiYjZjZjMxODUxY1wiLFwiODgyMzg2ODZkZGYxNGViOTY0ZTNmNjk5NmM2MDFkN2VcIl0sXCIxMFwiOltcIjA4MmMwMjE1NDMxZTE2NmJhMDcyYzYxZDVkNGQxMDJmXCIsXCI5ODQwMDEyYjMwNDcxOTk4MDEyZTAzYjAzYjMxYjdkMlwiLFwiMGIxYzg4ZDE4MzhhMDM2NTIwM2VlZjAzMTY1MmE5MWZcIixcImQwNDYyZTZhYjA2NGM4ZjlkNjRhNDNkNGMyMzJiZTg3XCIsXCI1NjhjMDIwMjFmZmE4MjljOTdlZjJiMTFjMWM3Yjg3MFwiLFwiNjc3MDk3ZTE5YTU0ZGE4NWZiNzRlYjE0NTgyMTIzN2VcIixcIjIwZjJmMDljMzlhOGUyM2ZkMzQ2Y2MwOWVjOTdlMTEwXCIsXCJlNWI0ZDg2MjkyZmM4Y2Y2MzExNDNmZTdkODY5NGQ4MVwiLFwiMWJiMjA5ZDI4NGZmNTRlZjMwMjVjMTE5ZjUzZGJlZDlcIixcImY3OGFjNGNkMjlmMzY1MWY4ZWJiYThlMjAxZTk4NzlhXCIsXCI1YWQ4ZGJiYWQ4ZWQ0OTAwYmE3YmVlZTM4YzNmMmM5MVwiXSxcIjExXCI6W1wiNzNlNDM0YzQxZjBmYTg4MzU3ZDE2M2EzZGZlZjIxMjRcIixcImVkYmJmNjRhZTQxZGJjOWJlZmFiNjg3MWI3OTZmMzc4XCJdfSIsIjY3OGFhODQ3YzAyMTAxZmNlNGY4NWY0NjI5ZGM5OWQ4Il0=\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="gform_target_page_number_19"\r\n\r\n0\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="gform_source_page_number_19"\r\n\r\n1\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundary2B4E9RWPT4t5T2Uq--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())
        response = requests.post(
            'https://sharc-research.org/training/professional-development-program-pdp/',
            cookies=cookies,
            headers=headers,
            data=data.encode(), proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Thanks')
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
