from typing import Optional

import jira.exceptions

from Config import Config
from JQLBuilder import JQLBuilder
from JiraConnection import JiraConnection
from Tikcet import Ticket
from lib.SingletonMeta import SingletonMeta


class JiraFacade(object, metaclass=SingletonMeta):
    def __init__(self):
        username = Config().get('jira.username')
        token = None # Config().get('jira.token')
        if token is None:
            token = Config().get('jira.password')
        try:
            self.connection = JiraConnection(username, token).get()
        except jira.exceptions.JIRAError as exception:
            raise Exception(exception.text)

    def find_ticket_by_key(self, key: str) -> Optional[Ticket]:
        jql = JQLBuilder().set_key(key).get()
        issues = self.connection.search_issues(jql, maxResults=1)
        if issues:
            return Ticket(issues.pop())
        return None

    def get_tickets_from_jql(self, jql: str, max_results=10) -> Optional[list[Ticket]]:
        issues = self.connection.search_issues(jql, maxResults=max_results)
        if issues:
            return list(map(lambda issue: Ticket(issue), issues))
        return None
