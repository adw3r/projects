from unittest import TestCase

from module.apis.captcha_solvers import CapMonsterSolver


class TestCapMonsterSolver(TestCase):

    def test_solving(self):
        self.skipTest('not needed')
        solver: CapMonsterSolver = CapMonsterSolver()

        googlesitekey = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'
        pageurl = 'https://www.google.com/recaptcha/api2/demo'
        result: str | None = solver.solve(googlekey=googlesitekey, pageurl=pageurl, time_limit=10, version='v2')
        self.assertIn('03A', result)
