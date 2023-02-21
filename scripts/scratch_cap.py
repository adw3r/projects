from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        pageurl = ''
        googlekey = ''
        cap = self.solve_captcha(pageurl, googlekey)
        if not cap:
            return
        return


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'))
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
