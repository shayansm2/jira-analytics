import pandas as pd
from JQLBuilder import JQLBuilder
from Enums import Enums
from JiraFacade import JiraFacade
from Tikcet import Ticket
from report_utils import get_ticket_developer, get_ticket_state

def _get_base_data(squad_names: str | list, sprint: str, quarter: str) -> pd.DataFrame:
        jql = JQLBuilder().set_project(Enums.project_shopping).set_sprints_from_squads(squad_names=squad_names,
                                                                                       sprint=sprint,
                                                                                       quarter=quarter).get()
        df = JiraFacade().get_df_from_jql(jql, 200)

        df[Ticket.field_developed_by] = df.apply(
            lambda x: get_ticket_developer(x[Ticket.field_assigned_to], x[Ticket.field_status], x[Ticket.field_developed_by]),
            axis=1)

        df['state'] = df.apply(lambda x: get_ticket_state(x[Ticket.field_status]), axis=1)
        return df