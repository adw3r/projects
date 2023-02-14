from os.path import basename

import requests

from module import CapMonsterSolver
from module import Spam

pageurl = 'https://workshops.frostart.co.uk/hosting-workshops/'

googlekey = '6LfY3SwUAAAAACk5mqpgqgCgY8kvHc8f0FN8tH7Y'

cookies = {
    'mtsnb_lastvisited': '1675331091',
    'tk_or': '%22https%3A%2F%2Fwww.google.com%2F%22',
    'cookielawinfo-checkbox-necessary': 'yes',
    'cookielawinfo-checkbox-non-necessary': 'yes',
    '_ga': 'GA1.3.1455084866.1675331097',
    'mtsnb_lastvisit_posts': '%5B743%2C6%5D',
    'tk_r3d': '%22https%3A%2F%2Fwww.google.com%2F%22',
    '_gid': 'GA1.3.1434732423.1675935211',
    'tk_lr': '%22%22',
    '_gat_gtag_UA_1245207_2': '1',
}

headers = {
    'authority': 'workshops.frostart.co.uk',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'mtsnb_lastvisited=1675331091; tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; _ga=GA1.3.1455084866.1675331097; mtsnb_lastvisit_posts=%5B743%2C6%5D; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; _gid=GA1.3.1434732423.1675935211; tk_lr=%22%22; _gat_gtag_UA_1245207_2=1',
    'origin': 'https://workshops.frostart.co.uk',
    'referer': 'https://workshops.frostart.co.uk/hosting-workshops/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
solver = CapMonsterSolver()


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        cap = solver.solve(googlekey, pageurl)
        if not cap:
            return
        data = 'action=nf_ajax_submit&security=086331cfe3&formData=%7B%22id%22%3A%223%22%2C%22fields%22%3A%7B%2220%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A20%7D%2C%2221%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A21%7D%2C%2222%22%3A%7B%22value%22%3A%22wezxasqw%40gmail.com%22%2C%22id%22%3A22%7D%2C%2231%22%3A%7B%22value%22%3A%22%22%2C%22id%22%3A31%7D%2C%2232%22%3A%7B%22value%22%3A%2212%22%2C%22id%22%3A32%7D%2C%2233%22%3A%7B%22value%22%3A%5B%22adults%22%5D%2C%22id%22%3A33%7D%2C%2234%22%3A%7B%22value%22%3A%5B%22College+or+University%22%5D%2C%22id%22%3A34%7D%2C%2235%22%3A%7B%22value%22%3A%22%22%2C%22id%22%3A35%7D%2C%2236%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A36%7D%2C%2237%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A37%7D%2C%2238%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A38%7D%2C%2239%22%3A%7B%22value%22%3A%22UA%22%2C%22id%22%3A39%7D%2C%2240%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A40%7D%2C%2241%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A41%7D%2C%2290%22%3A%7B%22value%22%3A%5B%22Yes%22%5D%2C%22id%22%3A90%7D%2C%2292%22%3A%7B%22value%22%3A%5B%22one-day%22%5D%2C%22id%22%3A92%7D%2C%2293%22%3A%7B%22value%22%3A%5B%22spring%22%5D%2C%22id%22%3A93%7D%2C%2295%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A95%7D%2C%2296%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A96%7D%2C%22404%22%3A%7B%22value%22%3A%22yes%22%2C%22id%22%3A404%7D%2C%22406%22%3A%7B%22value%22%3A%22yes%22%2C%22id%22%3A406%7D%2C%22407%22%3A%7B%22value%22%3A%5B%22yes%22%5D%2C%22id%22%3A407%7D%2C%22470%22%3A%7B%22value%22%3A%22cap_que%22%2C%22id%22%3A470%7D%7D%2C%22settings%22%3A%7B%22objectType%22%3A%22Form+Setting%22%2C%22editActive%22%3Atrue%2C%22title%22%3A%22Hosting+Workshops%22%2C%22created_at%22%3A%222019-01-20+22%3A14%3A05%22%2C%22form_title%22%3A%22Questionnaire%22%2C%22default_label_pos%22%3A%22above%22%2C%22show_title%22%3A0%2C%22clear_complete%22%3A%221%22%2C%22hide_complete%22%3A%221%22%2C%22logged_in%22%3A%220%22%2C%22drawerDisabled%22%3Afalse%2C%22calculations%22%3A%5B%5D%2C%22sub_limit_msg%22%3A%22The+form+has+reached+its+submission+limit.%22%2C%22not_logged_in_msg%22%3A%22%22%2C%22currency%22%3A%22%22%2C%22unique_field_error%22%3A%22A+form+with+this+value+has+already+been+submitted.%22%2C%22key%22%3A%22%22%2C%22add_submit%22%3A%221%22%2C%22element_class%22%3A%22%22%2C%22wrapper_class%22%3A%22%22%2C%22changeEmailErrorMsg%22%3A%22Please+enter+a+valid+email+address!%22%2C%22changeDateErrorMsg%22%3A%22Please+enter+a+valid+date!%22%2C%22confirmFieldErrorMsg%22%3A%22These+fields+must+match!%22%2C%22fieldNumberNumMinError%22%3A%22Number+Min+Error%22%2C%22fieldNumberNumMaxError%22%3A%22Number+Max+Error%22%2C%22fieldNumberIncrementBy%22%3A%22Please+increment+by+%22%2C%22formErrorsCorrectErrors%22%3A%22Please+correct+errors+before+submitting+this+form.%22%2C%22validateRequiredField%22%3A%22This+is+a+required+field.%22%2C%22honeypotHoneypotError%22%3A%22Honeypot+Error%22%2C%22fieldsMarkedRequired%22%3A%22+%22%2C%22container_styles_show_advanced_css%22%3A0%2C%22title_styles_show_advanced_css%22%3A0%2C%22row_styles_show_advanced_css%22%3A0%2C%22row-odd_styles_show_advanced_css%22%3A0%2C%22success-msg_styles_show_advanced_css%22%3A0%2C%22error_msg_styles_show_advanced_css%22%3A0%2C%22mp_breadcrumb%22%3A1%2C%22mp_progress_bar%22%3A1%2C%22mp_display_titles%22%3A0%2C%22breadcrumb_container_styles_show_advanced_css%22%3A0%2C%22breadcrumb_buttons_styles_show_advanced_css%22%3A0%2C%22breadcrumb_button_hover_styles_show_advanced_css%22%3A0%2C%22breadcrumb_active_button_styles_show_advanced_css%22%3A0%2C%22progress_bar_container_styles_show_advanced_css%22%3A0%2C%22progress_bar_fill_styles_show_advanced_css%22%3A0%2C%22part_titles_styles_show_advanced_css%22%3A0%2C%22navigation_container_styles_show_advanced_css%22%3A0%2C%22previous_button_styles_show_advanced_css%22%3A0%2C%22next_button_styles_show_advanced_css%22%3A0%2C%22navigation_hover_styles_show_advanced_css%22%3A0%2C%22container_styles_border%22%3A%22%22%2C%22container_styles_height%22%3A%22%22%2C%22container_styles_margin%22%3A%22%22%2C%22container_styles_padding%22%3A%22%22%2C%22container_styles_float%22%3A%22%22%2C%22title_styles_border%22%3A%22%22%2C%22title_styles_height%22%3A%22%22%2C%22title_styles_width%22%3A%22%22%2C%22title_styles_font-size%22%3A%22%22%2C%22title_styles_margin%22%3A%22%22%2C%22title_styles_padding%22%3A%22%22%2C%22title_styles_float%22%3A%22%22%2C%22row_styles_border%22%3A%22%22%2C%22row_styles_width%22%3A%22%22%2C%22row_styles_font-size%22%3A%22%22%2C%22row_styles_margin%22%3A%22%22%2C%22row_styles_padding%22%3A%22%22%2C%22row-odd_styles_border%22%3A%22%22%2C%22row-odd_styles_height%22%3A%22%22%2C%22row-odd_styles_width%22%3A%22%22%2C%22row-odd_styles_font-size%22%3A%22%22%2C%22row-odd_styles_margin%22%3A%22%22%2C%22row-odd_styles_padding%22%3A%22%22%2C%22success-msg_styles_border%22%3A%22%22%2C%22success-msg_styles_height%22%3A%22%22%2C%22success-msg_styles_width%22%3A%22%22%2C%22success-msg_styles_font-size%22%3A%22%22%2C%22success-msg_styles_margin%22%3A%22%22%2C%22success-msg_styles_padding%22%3A%22%22%2C%22error_msg_styles_border%22%3A%22%22%2C%22error_msg_styles_width%22%3A%22%22%2C%22error_msg_styles_font-size%22%3A%22%22%2C%22error_msg_styles_margin%22%3A%22%22%2C%22error_msg_styles_padding%22%3A%22%22%2C%22mp_prev_label%22%3A%22%22%2C%22mp_next_label%22%3A%22%22%2C%22allow_public_link%22%3A0%2C%22embed_form%22%3A%22%22%2C%22ninjaForms%22%3A%22Ninja+Forms%22%2C%22fieldTextareaRTEInsertLink%22%3A%22Insert+Link%22%2C%22fieldTextareaRTEInsertMedia%22%3A%22Insert+Media%22%2C%22fieldTextareaRTESelectAFile%22%3A%22Select+a+file%22%2C%22formHoneypot%22%3A%22If+you+are+a+human+seeing+this+field%2C+please+leave+it+empty.%22%2C%22fileUploadOldCodeFileUploadInProgress%22%3A%22File+Upload+in+Progress.%22%2C%22fileUploadOldCodeFileUpload%22%3A%22FILE+UPLOAD%22%2C%22currencySymbol%22%3A%22%26pound%3B%22%2C%22thousands_sep%22%3A%22%2C%22%2C%22decimal_point%22%3A%22.%22%2C%22siteLocale%22%3A%22en_GB%22%2C%22dateFormat%22%3A%22d%2Fm%2FY%22%2C%22startOfWeek%22%3A%221%22%2C%22of%22%3A%22of%22%2C%22previousMonth%22%3A%22Previous+Month%22%2C%22nextMonth%22%3A%22Next+Month%22%2C%22months%22%3A%5B%22January%22%2C%22February%22%2C%22March%22%2C%22April%22%2C%22May%22%2C%22June%22%2C%22July%22%2C%22August%22%2C%22September%22%2C%22October%22%2C%22November%22%2C%22December%22%5D%2C%22monthsShort%22%3A%5B%22Jan%22%2C%22Feb%22%2C%22Mar%22%2C%22Apr%22%2C%22May%22%2C%22Jun%22%2C%22Jul%22%2C%22Aug%22%2C%22Sep%22%2C%22Oct%22%2C%22Nov%22%2C%22Dec%22%5D%2C%22weekdays%22%3A%5B%22Sunday%22%2C%22Monday%22%2C%22Tuesday%22%2C%22Wednesday%22%2C%22Thursday%22%2C%22Friday%22%2C%22Saturday%22%5D%2C%22weekdaysShort%22%3A%5B%22Sun%22%2C%22Mon%22%2C%22Tue%22%2C%22Wed%22%2C%22Thu%22%2C%22Fri%22%2C%22Sat%22%5D%2C%22weekdaysMin%22%3A%5B%22Su%22%2C%22Mo%22%2C%22Tu%22%2C%22We%22%2C%22Th%22%2C%22Fr%22%2C%22Sa%22%5D%2C%22recaptchaConsentMissing%22%3A%22reCapctha+validation+couldn%26%23039%3Bt+load.%22%2C%22recaptchaMissingCookie%22%3A%22reCaptcha+v3+validation+couldn%26%23039%3Bt+load+the+cookie+needed+to+submit+the+form.%22%2C%22recaptchaConsentEvent%22%3A%22Accept+reCaptcha+cookies+before+sending+the+form.%22%2C%22currency_symbol%22%3A%22%22%2C%22beforeForm%22%3A%22%22%2C%22beforeFields%22%3A%22%22%2C%22afterFields%22%3A%22%22%2C%22afterForm%22%3A%22%22%7D%2C%22extra%22%3A%7B%7D%7D'
        data = data.replace('cap_que', cap).replace('wezxasqw%40gmail.com', target).replace('test', self.get_text())
        for _ in range(10):
            try:
                response = requests.post('https://workshops.frostart.co.uk/wp-admin/admin-ajax.php', cookies=cookies,
                                         headers=headers, data=data.encode(), proxies=self.get_proxies())
                return response
            except Exception as e:
                print(e)
        return


def main():
    s = 'Your form has been successfully submitted.'
    spam = ConcreteSpam(basename(__file__)[:-3], s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()


if __name__ == '__main__':
    main()
