from os.path import basename

import requests

from module import Spam

headers = {
    'authority': 'civis3i.univ-amu.fr',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary2771DGMXclGednXQ',
    'origin': 'https://civis3i.univ-amu.fr',
    'referer': 'https://civis3i.univ-amu.fr/en/form/contact',
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
        data = '------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="email"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="your_current_or_last_affiliation_whatever_applies_to_you_"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="subject"\r\n\r\nContact your chosen advisor\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="advisor_university"\r\n\r\nAMU\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="advisor_name"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="advisor_lab_or_research_group"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="tentative_title"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="project_ideas"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="preferred_university_"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="scientific_domain_"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="tentative_title_for_your_research"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="key_words"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="briefly_describe_your_project_ideas"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="bio"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="cv[fids]"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="other_optional_documents[fids]"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="optional_links_to_your_website_or_research_profiles"\r\n\r\ntest\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="send_yourself_a_copy"\r\n\r\n1\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="op"\r\n\r\nSend message\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="form_build_id"\r\n\r\nform-sDWMIE_-LhrtVPWBDGBDMzPhIqERjSmUfWAYLV_f1cU\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="form_id"\r\n\r\nwebform_submission_contact_add_form\r\n------WebKitFormBoundary2771DGMXclGednXQ\r\nContent-Disposition: form-data; name="homepage"\r\n\r\n\r\n------WebKitFormBoundary2771DGMXclGednXQ--\r\n'
        data = data.replace('wezxasqw@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post('https://civis3i.univ-amu.fr/en/form/contact', headers=headers, data=data.encode(),
                                 proxies=self.get_proxies())
        return response


def main():
    s = 'Thanks'
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
