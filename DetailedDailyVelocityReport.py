import pandas as pd
from abc import ABC

from AbstractSprintReport import AbstractSprintReport
from Tikcet import Ticket
import daily_reports


class DetailedDailyVelocityReport(AbstractSprintReport, ABC):
    def get(self) -> pd.DataFrame:
        df = daily_reports._get_base_data(self.squad_names, self.sprint, self.quarter)

        df['tickets'] = df.apply(lambda x: x[Ticket.field_key] + ' : ' + (x[Ticket.field_summary].replace('|', '').replace('/', '')), axis=1)
        return df.groupby([Ticket.field_squad_name, Ticket.field_team_name, Ticket.field_developed_by, 'state']).agg(
            {
                Ticket.field_key: 'count',
                Ticket.field_dev_estimate: 'sum',
                Ticket.field_test_effort: 'sum',
                'tickets': ' || '.join
            }).reset_index().rename(
            columns={Ticket.field_key: 'number_of_tickets'})