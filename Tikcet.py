from jira import Issue


class Ticket(object):
    def __init__(self, issue: Issue):
        self.issue = issue

    def get_id(self):
        return self.issue.key

    def get_link(self):
        return self.issue.self

    def get_summary(self):
        return self.issue.get_field('summary')

    def get_status(self):
        return self.issue.get_field('status')

    def get_description(self):
        return self.issue.fields.issuetype.description

    def get_ticket_type(self):
        return self.issue.fields.issuetype.name
