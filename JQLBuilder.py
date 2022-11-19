from __future__ import annotations


class JQLBuilder(object):
    def __init__(self):
        self.jql = ''

    def set_project(self, project_name: str) -> JQLBuilder:
        self.jql += 'project = ' + project_name
        return self

    def get(self) -> str:
        return self.jql
