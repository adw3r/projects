from unittest import TestCase

from module.apis.targets import TargetServerPool, get_random_target_pool


class TestProxies(TestCase):

    def test_init(self):
        pool_name = 'turk'
        pool = TargetServerPool(pool_name)

        self.assertEqual(pool_name, pool.pool_name)

    def test_get_pool(self):
        self.skipTest('not used')
        pool_name = 'turk'
        pool = TargetServerPool(pool_name)

        pool_list = pool.get_pool()
        self.assertNotEqual(0, len(pool_list))

    def test_pop(self):
        pool_name = 'turk'
        pool = TargetServerPool(pool_name)

        target = pool.pop()
        self.assertIsNotNone(target)

    def test_get_targets_json(self):
        answer = TargetServerPool.get_targets_json()
        self.assertIsNotNone(answer.get('turk'))

    def test_get_random_target_pool(self):
        pool_name = get_random_target_pool()
        pool_instance = TargetServerPool(pool_name)
        pool_info = pool_instance.get_pool_json()
        self.assertIsNotNone(pool_info.get('lang'))
