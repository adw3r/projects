import datetime
import random
import unittest

from module.apis.project_controller import ProjectServerController, ProjectServerControllerCached, get_current_time, \
    ProjectControllerOnRedis


class TestProjectServerController(unittest.TestCase):

    def test_attributes(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'FortuneClock'
        target_database = 'alotof'

        projects = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                           targets_base=target_database)
        self.assertEqual(projects.name, name)
        self.assertEqual(projects.prom_link, prom_link)

    def test_statusIsTrue(self):
        prom_link = 'bit.ly/3yi2UXW'
        name = 'teststatus'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)
        status = project.get_status()
        self.assertTrue(status)

    def test_statusIsFalse(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = ''
        project_name = 'FortuneClock'
        target_database = 'alotof'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)
        status = project.get_status()
        self.assertFalse(status)

    def test_false_status_in_loop(self):
        self.skipTest('relies on other service')

        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)
        results = []
        for i in range(210):
            result = project.get_status()
            print(result, i)
            results.append(result)
            project.send_count(0)
        self.assertTrue(False in results)

    def test_random_status_in_loop(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)
        results = []
        for _ in range(10):
            status = project.get_status()
            print(status)
            results.append(status)
            choice = random.choice([True, False])
            if choice:
                project.send_count(1)
            else:
                project.send_count(0)

        self.assertNotIn(False, results)

    def test_retrieve_attached_link(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)

        project.get_status()

        attached_link = project.retrieve_attached_link()
        self.assertEqual(prom_link, attached_link)


class TestCachedController(unittest.TestCase):

    def test_get_time(self):
        now = get_current_time()
        self.assertIsNotNone(now)
        self.assertIsInstance(now, str)

    def test_init(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        controller = ProjectServerControllerCached(
            name=name, prom_link=prom_link, project_name=project_name,
            targets_base=target_database
        )

        # checking that on init status is None
        status_dict = controller._load_status()
        self.assertEqual(status_dict['status'], None)

        # checking dump method
        controller._dump_status(False)
        status_dict = controller._load_status()
        self.assertEqual(status_dict['status'], False)

        # status is not expired coz taken now
        status_expired: bool = controller._check_status_is_not_expired(str(datetime.datetime.now()))  # True
        self.assertTrue(status_expired)

        # status is expired coz it was taken in 2022
        status_expired: bool = controller._check_status_is_not_expired('2022-12-20 12:31:27.016684')  # False
        self.assertFalse(status_expired)

    def test_expired_timestamp(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'testnotexpired'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        controller = ProjectServerControllerCached(
            name=name, prom_link=prom_link, project_name=project_name,
            targets_base=target_database
        )
        expired_timestamp = '2022-12-20 12:31:27.016684'
        controller._dump_status(True, expired_timestamp)
        status_dict = controller._load_status()
        controller_status_timestamp_loaded = status_dict['timestamp']
        status_expired: bool = controller._check_status_is_not_expired(controller_status_timestamp_loaded)  # False
        self.assertFalse(status_expired)

    def test_not_expired_timestamp(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'testexpired'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        controller = ProjectServerControllerCached(
            name=name, prom_link=prom_link, project_name=project_name,
            targets_base=target_database
        )
        controller._dump_status()
        status_dict = controller._load_status()
        controller_status_timestamp_loaded = status_dict['timestamp']
        status_expired: bool = controller._check_status_is_not_expired(controller_status_timestamp_loaded)  # False
        self.assertTrue(status_expired)

    def test_status(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'FortuneClock'
        target_database = 'alotof'
        controller = ProjectServerControllerCached(
            name=name, prom_link=prom_link, project_name=project_name,
            targets_base=target_database
        )

        # takes status from cache
        controller._dump_status(True)
        status = controller.get_status()
        self.assertTrue(status)

        # retrieves status form server
        expired_timestamp = '2022-12-20 12:31:27.016684'
        controller._dump_status(True, expired_timestamp)
        controller.get_status()
        cached_status = controller._load_status()
        timestamp = cached_status['timestamp']
        status = controller._check_status_is_not_expired(timestamp)
        self.assertTrue(status)


class TestProjectControllerOnRedis(unittest.TestCase):

    def test_init(self):
        self.skipTest('not implemented yet!')
        prom_link = 'bit.ly/3JIBDnW'
        name = 'drvolojw'
        project_name = 'FortuneClock'
        target_database = 'g11mp2'
        controller = ProjectControllerOnRedis(
            name=name, prom_link=prom_link, project_name=project_name,
            targets_base=target_database
        )

        status = controller.get_status()
        print(status)
