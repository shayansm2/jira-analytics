from jira import Issue
import re

from Enums import Enums


class Ticket(object):
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

    def get_epic_ticket(self) -> str:
        epic_ticket = self.issue.get_field(Enums.field_epic_ticket)
        return epic_ticket if epic_ticket is not None else ''

    def get_labels(self) -> list:
        return self.issue.fields.labels

    def get_squad_name(self) -> str:
        if self.issue.get_field(Enums.field_squad_name) is None:
            return ''
        return self.issue.get_field(Enums.field_squad_name).value

    def get_estimation(self) -> int:
        return self.issue.get_field(Enums.field_development_estimation)

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

    def get_as_dict(self) -> dict:
        return {
            'key': self.get_key(),
            'link': self.get_link(),
            'summary': self.get_summary(),
            'status': self.get_status(),
            'type': self.get_type(),
            'assigned_to': self.get_assigned_to(),
            'reported_by': self.get_reported_by(),
            'labels': self.get_labels(),
            'estimate': self.get_estimation(),
            'sprint': self.get_sprint(),
            'squad_name': self.get_squad_name(),
            'is_out_of_plan': self.is_out_of_plan(),
            'team_name': self.get_team_name(),
            'priority': self.get_priority(),
            'developed_by': self.get_developed_by(),
            'epic_ticket': self.get_epic_ticket(),
        }

    # todo epic_link, start_at, end_at, blocked_at,
