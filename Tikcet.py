from jira import Issue

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

    def get_description(self) -> str:
        return self.issue.fields.issuetype.description

    def get_type(self) -> str:
        return self.issue.fields.issuetype.name

    def get_assigned_to(self) -> str:
        if self.issue.fields.assignee is None:
            return ''
        return self.issue.fields.assignee.name

    def get_reported_by(self) -> str:
        return self.issue.fields.reporter.name

    def get_developed_by(self) -> str:  # todo
        return ''

    def get_labels(self) -> list:
        return self.issue.fields.labels

    def get_squad_name(self) -> str:
        if self.issue.get_field(Enums.field_squad_name) is None:
            return ''
        return self.issue.get_field(Enums.field_squad_name).value

    def get_estimation(self) -> int:
        return self.issue.get_field(Enums.field_estimation)

    def get_sprint(self) -> str:
        return ''  # todo self.issue.get_field(Enums.field_sprint).name

    def get_as_dict(self) -> dict:
        return {
            'key': self.get_key(),
            'link': self.get_link(),
            'summary': self.get_summary(),
            'status': self.get_status(),
            'description': self.get_description(),
            'type': self.get_type(),
            'assigned_to': self.get_assigned_to(),
            'reported_by': self.get_reported_by(),
            'developed_by': self.get_developed_by(),
            'labels': self.get_labels(),
            'estimate': self.get_estimation(),
            'sprint': self.get_sprint(),
            'squad_name': self.get_squad_name(),
        }

    # todo epic_link, priority, start_at, end_at, blocked_at, 