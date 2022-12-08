import pandas as pd

from DailyVelocityReport import DailyVelocityReport


class DetailedDailyVelocityReport(DailyVelocityReport):
    def get(self) -> pd.DataFrame:
        df = super()._prepare_data()

        df['tickets'] = df.apply(lambda x: x['key'] + ' : ' + (x['summary'].replace('|', '').replace('/', '')), axis=1)
        return df.groupby(['squad_name', 'team_name', 'developer', 'state']).agg(
            {'key': 'count', 'estimate': 'sum', 'tickets': ' || '.join}).reset_index().rename(
            columns={'key': 'number_of_tickets', 'estimate': 'story_point'})