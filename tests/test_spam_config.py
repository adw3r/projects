import os
from pathlib import Path
from unittest import TestCase

from module.config import CONFIGS_FOLDER
from module.spam_config import SpamConfig


class TestSpamConfig(TestCase):

    def test_init(self):
        testproject = 'testproject'
        path_to_test_config = Path(CONFIGS_FOLDER, f'{testproject}.json')
        if path_to_test_config.exists():
            print('path_to_test_config removed')
            os.remove(path_to_test_config)
        spam = SpamConfig(testproject)
        self.assertIsNotNone(spam.project_name)
        self.assertIsNotNone(spam.success_message)
        self.assertIsNotNone(spam.ref_name)
        self.assertIsNotNone(spam.proxy_pool_name)
        self.assertIsNotNone(spam.target_pool_name)
        self.assertIsNotNone(spam.promo_link)
        self.assertIsNotNone(spam.lang)
        self.assertIsNotNone(spam.text)
        self.assertIsNotNone(spam.spins)
        self.assertIsNotNone(spam.text_instance)
        self.assertIsNotNone(spam.proxy_instance)
        self.assertIsNotNone(spam.target_instance)
        self.assertIsNotNone(spam.captcha_solver)
        self.assertIsNotNone(spam.project_controller)
