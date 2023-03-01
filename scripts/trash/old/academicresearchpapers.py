from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '7pi1mqiv4cb4ddl53i865gusm6',
    'comm100_visitorguid_155184': '1cdc0bb3-4224-4ead-97c6-8e671b9142e3',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=7pi1mqiv4cb4ddl53i865gusm6; comm100_visitorguid_155184=1cdc0bb3-4224-4ead-97c6-8e671b9142e3',
    'Origin': 'http://academicresearchpapers.org',
    'Referer': 'http://academicresearchpapers.org/Contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        return response.status_code < 400

    def post(self, target) -> requests.Response | None:
        text = self.get_text(False)
        data = {
            'validationType': 'php',
            'firstname': 'name',
            'email': target,
            'subject': text,
            'message': text,
            'submit': 'SEND',
            'check': 'YES',
        }

        response = requests.post(
            'http://academicresearchpapers.org/sendMessage.php',
            cookies=cookies,
            headers=headers,
            data=data,
            verify=False, proxies=self.get_proxies(), timeout=10
        )
        return response


def main():
    s = ''
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
