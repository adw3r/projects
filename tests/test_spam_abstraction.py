import os
from unittest import TestCase

os.environ['LOGGING_LEVEL'] = '10'


class TestSpamAbstraction(TestCase):

    def test_init(self):
        ...
