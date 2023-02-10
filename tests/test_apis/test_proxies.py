from unittest import TestCase

from module.apis.proxies import ProxyServerPool


class TestProxies(TestCase):

    def test_init(self):
        pool_name = 'west'
        pool = ProxyServerPool(pool_name)

        self.assertEqual(pool_name, pool.pool_name)

    def test_get_pool(self):
        pool_name = 'west'
        pool = ProxyServerPool(pool_name)

        pool_list = pool.get_pool()
        self.assertNotEqual(0, len(pool_list))

    def test_pop(self):
        pool_name = 'west'
        pool = ProxyServerPool(pool_name)

        proxy = pool.pop()
        self.assertIsNotNone(proxy)
