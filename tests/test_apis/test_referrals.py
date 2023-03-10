from unittest import TestCase

from module.apis.referrals import Referrals, get_random_project


class TestReferrals(TestCase):

    def test_get_response(self):
        referrals = Referrals()
        resp: dict = referrals.get_referrals_json()
        self.assertIsNotNone(resp.get('WG casino'))

    def test_get_random_project(self):
        referrals = Referrals()
        project = get_random_project()
        resp: dict = referrals.get_referrals_json()
        self.assertIsNotNone(resp.get(project))
