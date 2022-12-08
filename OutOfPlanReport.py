from abc import ABC

import pandas as pd

from AbstractReport import AbstractReport
from Enums import Enums
from JQLBuilder import JQLBuilder
from JiraFacade import JiraFacade


class OutOfPlanReport(AbstractReport, ABC):
    def get(self) -> pd.DataFrame:
        jql = JQLBuilder() \
            .set_project(Enums.project_shopping) \
            .set_sprints_from_squads(squad_names=self.squad_names, sprint=self.sprint, quarter=self.quarter) \
            .get()

        df = JiraFacade().get_df_from_jql(jql, 100)

        out_of_plan_report = df.groupby(['team_name', 'is_out_of_plan']).agg(
            {'estimate': 'sum', 'squad_name': 'count'}).reset_index()

        out_of_plan_report.rename(columns={'estimate': 'story point', 'squad_name': 'number of tickets'}, inplace=True)
        return out_of_plan_report
