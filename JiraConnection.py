from lib.SingletonMeta import SingletonMeta
from jira import JIRA


class JiraConnection(object, metaclass=SingletonMeta):
    def __init__(self, username: str, password: str):
        server = 'https://dkjira.digikala.com'
        self.connector = JIRA(basic_auth=(username, password), options={'server': server})

    def get(self) -> JIRA:
        return self.connector
