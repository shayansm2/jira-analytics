import unittest

import jira.exceptions

from Config import Config
from JQLBuilder import JQLBuilder
from JiraConnection import JiraConnection


class Test(unittest.TestCase):
    def test_config_singleton(self):
        a = Config()
        b = Config()
        self.assertEqual(a, b)

    def test_jira_config_exists(self):
        self.assertIsNotNone(Config().get('jira.username'))
        self.assertIsNotNone(Config().get('jira.password'))

    def test_jira_connection_exists(self):
        username = Config().get('jira.username')
        password = Config().get('jira.password')

        try:
            JiraConnection(username, password).get()
        except jira.exceptions.JIRAError:
            self.assertTrue(False)

        self.assertTrue(True)

    def test_jira_connection_singleton(self):
        username = Config().get('jira.username')
        password = Config().get('jira.password')
        a = JiraConnection(username, password).get()
        b = JiraConnection(username, password).get()
        self.assertEqual(a, b)

    def test_jql_builder(self):
        self.assertEqual(
            JQLBuilder().set_project('shopping').get(),
            'project = shopping'
        )