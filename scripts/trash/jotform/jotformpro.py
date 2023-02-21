from concurrent.futures import ThreadPoolExecutor
import datetime
from os.path import basename

import requests
from faker import Faker

import module
from module import Spam

headers = {
    'authority': 'submit.jotformpro.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://form.jotformpro.com',
    'referer': 'https://form.jotformpro.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response | None:
        headers['user-agent'] = Faker().chrome()

        text = self.get_text()
        timestamp = str(datetime.datetime.now().timestamp()).replace(".", "")[:-3]
        data = {
            'formID': '31895183083965',
            'q9_date9[month]': '02',
            'q9_date9[day]': '20',
            'q9_date9[year]': '2023',
            'q4_referredBy': text,
            'q10_parentsguardians[first]': text,
            'q10_parentsguardians[last]': text,
            'q19_parentsguardians19[first]': text,
            'q19_parentsguardians19[last]': text,
            'q11_1Childs[first]': text,
            'q11_1Childs[last]': text,
            'q20_2Childs[first]': text,
            'q20_2Childs[last]': text,
            'q21_3Childs[first]': text,
            'q21_3Childs[last]': text,
            'q12_1Childs12[month]': 'February',
            'q12_1Childs12[day]': '1',
            'q12_1Childs12[year]': '2021',
            'q23_2Childs23[month]': 'January',
            'q23_2Childs23[day]': '2',
            'q23_2Childs23[year]': '2021',
            'q22_3Childs22[month]': 'January',
            'q22_3Childs22[day]': '1',
            'q22_3Childs22[year]': '2021',
            'q5_1Childs5': text,
            'q25_2Childs25': text,
            'q24_3Childs24': text,
            'q6_1Childs6': text,
            'q26_2Childs26': text,
            'q27_3Childs27': text,
            'q13_address13[addr_line1]': text,
            'q13_address13[addr_line2]': text,
            'q13_address13[city]': text,
            'q13_address13[state]': text,
            'q13_address13[postal]': text,
            'q13_address13[country]': 'United States',
            'q14_mobilePhone[area]': text,
            'q14_mobilePhone[phone]': text,
            'q7_isThere7': text,
            'q15_homePhone[area]': text,
            'q15_homePhone[phone]': text,
            'q16_childsInterestsneeds16': text,
            'q17_pleaseShare': text,
            'q30_1Child[first]': text,
            'q30_1Child[last]': text,
            'q31_2Child[first]': text,
            'q31_2Child[last]': text,
            'q32_3Child[first]': text,
            'q32_3Child[last]': text,
            'q33_parentguardian[first]': text,
            'q33_parentguardian[last]': text,
            'q34_parentguardian34[first]': text,
            'q34_parentguardian34[last]': text,
            'q35_phoneNumber35[area]': text,
            'q35_phoneNumber35[phone]': text,
            'q36_email36': target,
            'q38_netPay': text,
            'q39_childTax': text,
            'q40_maintenanceSupport': text,
            'q41_annualTax': text,
            'q42_insurance': text,
            'q43_pension': text,
            'q44_assets': text,
            'q45_other': text,
            'q47_food': text,
            'q48_entertainment': text,
            'q49_fuel': text,
            'q50_medications': text,
            'q52_rentmortgage': text,
            'q53_heat': text,
            'q54_hydro': text,
            'q55_internetcable': text,
            'q56_insurance56': text,
            'q57_watersewage': text,
            'q58_homePhone58': text,
            'q59_cellPhone': text,
            'q60_carRepairsexpenses': text,
            'q61_daycare': text,
            'q62_kidsActivities': text,
            'q63_medicalExpenses': text,
            'q65_loan': text,
            'q66_loan66': text,
            'q67_loan67': text,
            'website': '',
            'validatedRequiredFieldIDs': '"No validated required fields"',
            'simple_spc': '31895183083965-31895183083965',
            'event_id': f'{timestamp}_31895183083965_{module.generate_text(7)}',
        }

        response = requests.post('https://submit.jotformpro.com/submit/31895183083965/', headers=headers, data=data,
                                 proxies=self.get_proxies(), timeout=10, verify=False
                                 )
        return response


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'), 'Your submission has been received.',
                        proxy_pool_name='parsed')

    with ThreadPoolExecutor(10) as worker:
        results = worker.map(spam.send_post, ['wezxasqw@gmail.com' for _ in range(10)])
    if any(results):
        spam.run_concurrently(60)


if __name__ == '__main__':
    main()
