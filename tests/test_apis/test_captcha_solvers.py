from unittest import TestCase

from module.apis.captcha_solvers import CapMonsterSolver


class TestCapMonsterSolver(TestCase):

    def test_solving(self):
        solver: CapMonsterSolver = CapMonsterSolver()
        googlekey = '6LcPudEjAAAAAHiEiPG17P7u3yFumpmj60UjLA9U'
        pageurl = 'https://app.txtwizard.com/registration'
        result: str | None = solver.solve(googlekey=googlekey, pageurl=pageurl)
        self.assertIn('03A', result)
