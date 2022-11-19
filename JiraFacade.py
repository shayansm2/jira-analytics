from typing import Optional

from Config import Config
from JQLBuilder import JQLBuilder
from JiraConnection import JiraConnection
from Tikcet import Ticket
from lib.SingletonMeta import SingletonMeta


class JiraFacade(object, metaclass=SingletonMeta):
    def __init__(self):
        username = Config().get('jira.username')
        password = Config().get('jira.passowrd')
        self.connection = JiraConnection(username, password).get()

    def find_ticket_by_id(self, id: str) -> Optional[Ticket]:
        jql = JQLBuilder().set_key(id).get()
        issues = self.connection.search_issues(jql, maxResults=1)
        if issues:
            return Ticket(issues.pop())
        return None

    def get_tickets_from_jql(self, jql: str, max_results=10) -> Optional[list[Ticket]]:
        issues = self.connection.search_issues(jql, maxResults=max_results)
        if issues:
            return list(map(lambda issue: Ticket(issue), issues))
        return None
