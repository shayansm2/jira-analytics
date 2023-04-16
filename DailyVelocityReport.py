from abc import ABC

import pandas as pd

from AbstractSprintReport import AbstractSprintReport
from Enums import Enums
from JQLBuilder import JQLBuilder
from JiraFacade import JiraFacade
from report_utils import get_ticket_developer, get_ticket_state


class DailyVelocityReport(AbstractSprintReport, ABC):
    def get(self) -> pd.DataFrame:
        df = self._prepare_data()

        return df.groupby(['squad_name', 'team_name', 'developer', 'state']).agg(
            {'key': 'count', 'estimate': 'sum'}).reset_index().rename(
            columns={'key': 'number_of_tickets', 'estimate': 'story_point'}).pivot(
            index=['team_name', 'squad_name', 'developer'], columns=['state'],
            values=['story_point', 'number_of_tickets']).fillna(0)

    def _prepare_data(self) -> pd.DataFrame:
        jql = JQLBuilder().set_project(Enums.project_shopping).set_sprints_from_squads(squad_names=self.squad_names,
                                                                                       sprint=self.sprint,
                                                                                       quarter=self.quarter).get()
        df = JiraFacade().get_df_from_jql(jql, 200)

        df['developer'] = df.apply(
            lambda x: get_ticket_developer(x['assigned_to'], x['status'], x['developed_by']),
            axis=1)

        df['state'] = df.apply(lambda x: get_ticket_state(x['status']), axis=1)
        return df
