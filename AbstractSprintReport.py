from abc import abstractmethod
from typing import Optional

import pandas as pd


class AbstractSprintReport(object):
    def __init__(self, squad_names: str | list, sprint: str, quarter: str):
        self.squad_names = squad_names
        self.sprint = sprint
        self.quarter = quarter

    @abstractmethod
    def get(self) -> pd.DataFrame:
        pass
