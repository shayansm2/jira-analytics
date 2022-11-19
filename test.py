import unittest

import jira

import Tikcet
from Config import Config
from Enums import Enums
from JQLBuilder import JQLBuilder
from JiraConnection import JiraConnection
from JiraFacade import JiraFacade


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

        self.assertEqual(
            JQLBuilder().set_project('shopping').set_key('SHOP-123').get(),
            'project = shopping AND key = SHOP-123'
        )

    def test_jira_search_issues(self):
        username = Config().get('jira.username')
        password = Config().get('jira.password')
        connection = JiraConnection(username, password).get()
        jql = JQLBuilder().set_project(Enums.project_shopping).get()
        issues = connection.search_issues(jql_str=jql, maxResults=1)
        self.assertIsInstance(issues, jira.client.ResultList)
        issue = issues.pop()
        self.assertIsInstance(issue, jira.Issue)

    def test_jira_facade_ticket_getters(self):
        jira = JiraFacade()
        ticket = jira.find_ticket_by_id('SHOP-2119')
        self.assertIsInstance(ticket, Tikcet.Ticket)
        self.assertEqual(ticket.get_id(), 'SHOP-2119')
        self.assertEqual(ticket.get_ticket_type(), 'Bug')

        jql = JQLBuilder().set_project(Enums.project_shopping).get()
        tickets = jira.get_tickets_from_jql(jql, 3)
        self.assertIsInstance(tickets, list)
