import pandas as pd

from DailyVelocityReport import DailyVelocityReport
from Tikcet import Ticket


class DetailedDailyVelocityReport(DailyVelocityReport):
    def get(self) -> pd.DataFrame:
        df = super()._prepare_data()

        df['tickets'] = df.apply(lambda x: x[Ticket.field_key] + ' : ' + (x[Ticket.field_summary].replace('|', '').replace('/', '')), axis=1)
        return df.groupby([Ticket.field_squad_name, Ticket.field_team_name, Ticket.field_developed_by, 'state']).agg(
            {
                Ticket.field_key: 'count',
                Ticket.field_dev_estimate: 'sum',
                Ticket.field_test_effort: 'sum',
                'tickets': ' || '.join
            }).reset_index().rename(
            columns={Ticket.field_key: 'number_of_tickets'})