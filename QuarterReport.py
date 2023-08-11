import pandas as pd

from Enums import Enums
from JQLBuilder import JQLBuilder
from JiraFacade import JiraFacade
from report_utils import get_ticket_state


class QuarterReport(object):
    def __init__(self, squad_name: str, quarter: str, year: str):
        self.squad_name = squad_name
        self.sprints = [squad_name + '-' + year + 'Q' + quarter + 'S0' + str(i) for i in range(1, 7)]

    def get(self):  # -> pd.DataFrame
        jql = JQLBuilder(). \
            set_project(Enums.project_shopping). \
            set_squad_name(self.squad_name). \
            set_sprints(self.sprints). \
            get()

        df = JiraFacade().get_df_from_jql(jql, 500)

        df['state'] = df.apply(lambda x: get_ticket_state(x['status']), axis=1)
        # df = df[df['state'] != 'invalid_ticket']

        epic_tickets = df['epic_ticket'].dropna().loc[lambda x: x != ''].unique().tolist()

        epic_jql = JQLBuilder(). \
            set_project(Enums.project_shopping). \
            set_type(Enums.type_epic). \
            set_keys(epic_tickets). \
            get()

        epic_df = JiraFacade().get_df_from_jql(epic_jql, 100)

        epic_df = epic_df[['key', 'summary', 'link']]
        epic_df.rename(columns={'key': 'epic_key', 'summary': 'epic_summary', 'link': 'epic_link'}, inplace=True)

        quarter_tickets_df = pd.merge(df, epic_df, left_on='epic_ticket', right_on='epic_key', how='inner')

        return quarter_tickets_df
