from pathlib import Path
from unittest import TestCase

import dotenv

from module import config


class TestEnv(TestCase):

    def test_env_file_exists(self):
        path_to_env_file = dotenv.find_dotenv()
        self.assertTrue(Path(path_to_env_file).exists())

    def test_all_enviromental_variables_is_not_empty(self):
        self.assertIsNotNone(config.TARGETS_HOST)
        self.assertIsNotNone(config.CONFIG_FILE)
        self.assertIsNotNone(config.PROXIES_HOST)
        self.assertIsNotNone(config.TEXTS_HOST)
        self.assertIsNotNone(config.LINKS_HOST)
        self.assertIsNotNone(config.REFERRALS_HOST)
        self.assertIsNotNone(config.LOGGING_LEVEL)
        self.assertIsNotNone(config.THREADS_LIMIT)
        self.assertIsNotNone(config.SCRIPTS_FOLDER)
        self.assertIsNotNone(config.PROXIES)
        self.assertIsNotNone(config.START)
        self.assertIsNotNone(config.TEST_TARGET)
