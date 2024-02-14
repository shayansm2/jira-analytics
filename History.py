from jira import Issue
import pandas as pd

class History(object):
    def __init__(self, issue: Issue) -> None:
        self.issue = issue

    def get(self, field_name: str = None) -> list:
        result = []
        for history in self.issue.changelog.histories:
            for item in history.items:
                if field_name is not None and item.field != field_name:
                    continue

                result.append({
                    'field': item.field,
                    'from': item.fromString,
                    'to': item.toString,
                })
        
        return result
    
    def get_as_df(self, field_name: str = None) -> pd.DataFrame:
        return pd.DataFrame(self.get())