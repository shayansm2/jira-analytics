from typing import Optional

developed_statuses = ['Ready To Test', 'Testing', 'Test Passed', 'Ready To Deploy', 'Deployed', 'Done']
not_started_statuses = ['Sprint Backlog']
in_progress_statuses = ['In Progress', 'Revision']
code_review_statuses = ['Code Review']
invalid_statuses = ['Analysis', 'Product Backlog', 'Blocked', 'Closed']


def get_ticket_state(status: str):
    if status in developed_statuses:
        return 'developed'
    if status in not_started_statuses:
        return 'not_started'
    if status in in_progress_statuses:
        return 'in_progress'
    if status in invalid_statuses:
        return 'invalid_ticket'
    return status


def get_ticket_developer(assigned_to: str, status: str, developed_by: Optional[str]):
    if developed_by:
        return developed_by

    if status in not_started_statuses + in_progress_statuses:
        return assigned_to

    return 'unknown'
