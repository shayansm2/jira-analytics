from abc import abstractmethod
from typing import final

import pandas as pd


class ReporterInterface(object):
    @final
    def send_report(self, df: pd.DataFrame):
        self.send_message(self.convert_to_message(df))

    @abstractmethod
    def send_message(self, message: str):
        pass

    # todo df convertor?
    def convert_to_message(self, df: pd.DataFrame) -> str:
        df.reset_index()
        return '1'
