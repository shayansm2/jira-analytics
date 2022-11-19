from __future__ import annotations


class JQLBuilder(object):
    def __init__(self):
        self.conditions = []

    def set_project(self, project_name: str) -> JQLBuilder:
        self.conditions.append('project = ' + project_name)
        return self

    def set_key(self, key: str) -> JQLBuilder:
        self.conditions.append('key = ' + key)
        return self

    def get(self) -> str:
        return ' AND '.join(self.conditions)
