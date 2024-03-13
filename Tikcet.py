from jira import Issue
import re

from History import History
from Enums import Enums


class Ticket(object):
    field_key = 'key'
    field_link = 'link'
    field_summary = 'summary'
    field_status = 'status'
    field_type = 'type'
    field_assigned_to = 'assigned_to'
    field_reported_by = 'reported_by'
    field_labels = 'labels'
    field_dev_estimate = 'dev_estimate'
    field_test_effort = 'test_effort'
    field_sprint = 'sprint'
    field_squad_name = 'squad_name'
    field_is_out_of_plan = 'is_out_of_plan'
    field_team_name = 'team_name'
    field_priority = 'priority'
    field_developed_by = 'developed_by'
    field_tester = 'tester'
    field_epic_ticket = 'epic_ticket'
    field_test_count = 'test_count'


    def __init__(self, issue: Issue):
        self.issue = issue

    def get_key(self) -> str:
        return self.issue.key

    def get_link(self) -> str:
        return self.issue.self

    def get_summary(self) -> str:
        return self.issue.get_field('summary')

    def get_status(self) -> str:
        return self.issue.fields.status.name

    def get_type(self) -> str:
        return self.issue.fields.issuetype.name

    def get_assigned_to(self) -> str:
        if self.issue.fields.assignee is None:
            return ''
        return self.issue.fields.assignee.name

    def get_reported_by(self) -> str:
        return self.issue.fields.reporter.name

    def get_developed_by(self) -> str:
        if self.issue.get_field(Enums.field_developed_by) is None:
            return ''
        return self.issue.get_field(Enums.field_developed_by).name
    
    def get_tester(self) -> str:
        if self.issue.get_field(Enums.field_tester) is None:
            return ''
        return self.issue.get_field(Enums.field_tester).name

    def get_epic_ticket(self) -> str:
        epic_ticket = self.issue.get_field(Enums.field_epic_ticket)
        return epic_ticket if epic_ticket is not None else ''

    def get_labels(self) -> list:
        return self.issue.fields.labels

    def get_squad_name(self) -> str:
        if self.issue.get_field(Enums.field_squad_name) is None:
            return ''
        return self.issue.get_field(Enums.field_squad_name).value

    def get_development_estimation(self) -> int:
        return self.issue.get_field(Enums.field_development_estimation)
    
    def get_test_effort(self) -> int:
        return self.issue.get_field(Enums.field_test_effort)

    def get_sprint(self) -> str:
        sprint = self.issue.get_field(Enums.field_sprint)
        if sprint is None:
            return ''
        sprint = sprint.pop()
        sprint_name = re.findall('name=(.*?),', sprint)
        if sprint_name is None:
            return ''
        return sprint_name.pop()

    def is_out_of_plan(self) -> bool:
        return Enums.label_out_of_plan in self.get_labels()

    def get_issue(self) -> Issue:
        return self.issue

    def get_team_name(self) -> str:
        labels = self.get_labels()
        if Enums.label_front_end in labels:
            return 'frontend'
        if Enums.label_back_end in labels:
            return 'backend'
        if Enums.label_design in labels:
            return 'design'
        if Enums.label_app in labels:
            return 'app'
        return ''

    def get_priority(self) -> str:
        return self.issue.get_field('priority').name
    
    def get_history(self) -> History:
        return History(self.issue)
    
    def get_test_count(self) -> int:
        result = 0
        for change in self.get_history().get('status'):
            if change['to'] == Enums.status_ready_to_test:
                result += 1
        return result 

    def get_as_dict(self) -> dict:
        return {
            self.field_key: self.get_key(),
            self.field_link: self.get_link(),
            self.field_summary: self.get_summary(),
            self.field_status: self.get_status(),
            self.field_type: self.get_type(),
            self.field_assigned_to: self.get_assigned_to(),
            self.field_reported_by: self.get_reported_by(),
            self.field_labels: self.get_labels(),
            self.field_dev_estimate: self.get_development_estimation(),
            self.field_test_effort: self.get_test_effort(),
            self.field_sprint: self.get_sprint(),
            self.field_squad_name: self.get_squad_name(),
            self.field_is_out_of_plan: self.is_out_of_plan(),
            self.field_team_name: self.get_team_name(),
            self.field_priority: self.get_priority(),
            self.field_developed_by: self.get_developed_by(),
            self.field_tester: self.get_tester(),
            self.field_epic_ticket: self.get_epic_ticket(),
            self.field_test_count: self.get_test_count(),
        }

    # todo epic_link, start_at, end_at, blocked_at,
