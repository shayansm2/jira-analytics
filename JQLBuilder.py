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

    def set_squad_name(self, squad_name: str) -> JQLBuilder:
        self.conditions.append('"Shopping Area" = ' + squad_name)
        return self

    def set_squad_names(self, squad_names: list) -> JQLBuilder:
        self.conditions.append('status IN (' + ','.join(squad_names) + ')')
        return self

    def set_sprint(self, sprint_name: str) -> JQLBuilder:
        self.conditions.append('Sprint = ' + sprint_name)
        return self

    def set_sprints(self, sprint_names: list) -> JQLBuilder:
        self.conditions.append('Sprint IN (' + ','.join(sprint_names) + ')')
        return self

    def set_sprints_from_squads(self, squad_names: list, sprint: str, quarter: str, year: str = '01') -> JQLBuilder:
        suffix = '-' + year + 'Q' + quarter + 'S' + sprint
        sprint_names = [squad_name + suffix for squad_name in squad_names]
        return self.set_sprints(sprint_names)

    def set_status(self, status: str) -> JQLBuilder:
        self.conditions.append('status = ' + status)
        return self

    def set_statuses(self, statuses: list) -> JQLBuilder:
        self.conditions.append('status IN (' + ','.join(statuses) + ')')
        return self

    def get(self) -> str:
        return ' AND '.join(self.conditions)
