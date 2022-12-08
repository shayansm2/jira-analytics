from typing import Optional
import pandas as pd

import jira.exceptions

from Config import Config
from JiraConnection import JiraConnection
from Tikcet import Ticket
from lib.SingletonMeta import SingletonMeta


class JiraFacade(object, metaclass=SingletonMeta):
    def __init__(self):
        username = Config().get('jira.username')
        token = None  # Config().get('jira.token') todo fix this, why tokens do not work?
        if token is None:
            token = Config().get('jira.password')
        try:
            self.connection = JiraConnection(username, token).get()
        except jira.exceptions.JIRAError as exception:
            raise Exception(exception.text)

    def find_ticket_by_key(self, key: str) -> Optional[Ticket]:
        issue = self.connection.issue(key)
        if issue:
            return Ticket(issue)
        return None

    def get_tickets_from_jql(self, jql: str, max_results=10) -> Optional[list[Ticket]]:
        issues = self.connection.search_issues(jql, maxResults=max_results)
        if issues:
            return list(map(lambda issue: Ticket(issue), issues))
        return None

    def get_df_from_jql(self, jql: str, max_results=10) -> pd.DataFrame:
        tickets = self.get_tickets_from_jql(jql, max_results)
        return pd.DataFrame(list(map(lambda ticket: ticket.get_as_dict(), tickets)))
