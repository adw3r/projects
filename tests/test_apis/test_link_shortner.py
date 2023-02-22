import unittest

import requests

from module.apis.links import LinkV2, Link
from module.apis.referrals import get_random_project
from module.apis.targets import get_random_target_pool


class TestLinkShortner(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.target_pool_name = get_random_target_pool()
        cls.referral_to_project = get_random_project()

    def test_link_v2(self):
        self.skipTest('not used anymore')
        shortened_link = LinkV2().get_link(target_pool_name=self.target_pool_name,
                                           referal_to_project=self.referral_to_project)
        response = requests.get(shortened_link)
        self.assertIn(self.referral_to_project, response.text)

    def test_link(self):
        shortened_link = Link().get_link(target_pool_name=self.target_pool_name,
                                         referal_to_project=self.referral_to_project)
        response = requests.get(shortened_link)
        self.assertIn(self.referral_to_project, response.text)
