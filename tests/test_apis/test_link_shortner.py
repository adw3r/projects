from unittest import TestCase

import requests

from module.apis.links import LinkV2, Link
from module.apis.referrals import get_random_project
from module.apis.targets import get_random_target_pool

target_pool_name = get_random_target_pool()
referral_to_project = get_random_project()


class TestLinkShortner(TestCase):

    def test_link_v2(self):
        self.skipTest('not used anymore')
        shortened_link = LinkV2().get_link(target_pool_name=target_pool_name, referal_to_project=referral_to_project)
        response = requests.get(shortened_link)
        response_content = response.text
        self.assertIn(referral_to_project, response_content)

    def test_link(self):
        shortened_link = Link().get_link(target_pool_name=target_pool_name, referal_to_project=referral_to_project)
        response = requests.get(shortened_link)
        response_content = response.text
        self.assertIn(referral_to_project, response_content)
