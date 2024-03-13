from abc import ABC

import pandas as pd

from AbstractSprintReport import AbstractSprintReport
from Enums import Enums
from JQLBuilder import JQLBuilder
from JiraFacade import JiraFacade
from report_utils import get_ticket_developer, get_ticket_state
from Tikcet import Ticket


class DailyVelocityReport(AbstractSprintReport, ABC):
    def get(self) -> pd.DataFrame:
        df = self._prepare_data()

        return df.groupby([Ticket.field_squad_name, Ticket.field_team_name, Ticket.field_developed_by, 'state']).agg(
            {Ticket.field_key: 'count', Ticket.field_dev_estimate: 'sum', Ticket.field_test_effort: 'sum'}).reset_index().rename(
            columns={Ticket.field_key: 'number_of_tickets'}).pivot(
            index=[Ticket.field_team_name, Ticket.field_squad_name, Ticket.field_developed_by], columns=['state'],
            values=[Ticket.field_dev_estimate, Ticket.field_test_effort, 'number_of_tickets']).fillna(0)

    def _prepare_data(self) -> pd.DataFrame:
        jql = JQLBuilder().set_project(Enums.project_shopping).set_sprints_from_squads(squad_names=self.squad_names,
                                                                                       sprint=self.sprint,
                                                                                       quarter=self.quarter).get()
        df = JiraFacade().get_df_from_jql(jql, 200)

        df[Ticket.field_developed_by] = df.apply(
            lambda x: get_ticket_developer(x[Ticket.field_assigned_to], x[Ticket.field_status], x[Ticket.field_developed_by]),
            axis=1)

        df['state'] = df.apply(lambda x: get_ticket_state(x[Ticket.field_status]), axis=1)
        return df
