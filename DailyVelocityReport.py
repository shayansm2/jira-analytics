from abc import ABC

import pandas as pd

from AbstractSprintReport import AbstractSprintReport
from Enums import Enums
from JQLBuilder import JQLBuilder
from JiraFacade import JiraFacade
from report_utils import get_ticket_developer, get_ticket_state
from Tikcet import Ticket
import daily_reports


class DailyVelocityReport(AbstractSprintReport, ABC):
    def get(self) -> pd.DataFrame:
        df = daily_reports._get_base_data(self.squad_names, self.sprint, self.quarter)

        return df.groupby([Ticket.field_squad_name, Ticket.field_team_name, Ticket.field_developed_by, 'state']).agg(
            {Ticket.field_key: 'count', Ticket.field_dev_estimate: 'sum', Ticket.field_test_effort: 'sum'}).reset_index().rename(
            columns={Ticket.field_key: 'number_of_tickets'}).pivot(
            index=[Ticket.field_team_name, Ticket.field_squad_name, Ticket.field_developed_by], columns=['state'],
            values=[Ticket.field_dev_estimate, Ticket.field_test_effort, 'number_of_tickets']).fillna(0)
