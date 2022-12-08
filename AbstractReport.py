from abc import abstractmethod
from typing import Optional

import pandas as pd


class AbstractReport(object):
    developed_statuses = ['Ready To Test', 'Testing', 'Test Passed', 'Ready To Deploy', 'Deployed', 'Done']
    not_started_statuses = ['Sprint Backlog']
    in_progress_statuses = ['In Progress', 'Code Review', 'Revision']
    invalid_statuses = ['Analysis', 'Product Backlog', 'Blocked', 'Closed']

    def __init__(self, squad_names: str | list, sprint: str, quarter: str):
        self.squad_names = squad_names
        self.sprint = sprint
        self.quarter = quarter

    @abstractmethod
    def get(self) -> pd.DataFrame:
        pass

    @classmethod
    def _get_developer(cls, assigned_to: str, status: str, developed_by: Optional[str]):
        if developed_by:
            return developed_by

        if status in cls.not_started_statuses + cls.in_progress_statuses:
            return assigned_to

        return 'unknown'

    @classmethod
    def _get_state(cls, status: str):
        if status in cls.developed_statuses:
            return 'developed'
        if status in cls.not_started_statuses:
            return 'not_started'
        if status in cls.in_progress_statuses:
            return 'in_progress'
        if status in cls.invalid_statuses:
            return 'invalid_ticket'
        return status
