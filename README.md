# Jira Analytics

> please before working with this repo, change the configs.yaml and use your own username, password and tokens.

there are many ways you can use this repo in order to extract data from jira and use the data for your analytics

1. get ticket by its key

```python
from JiraFacade import JiraFacade

ticket = JiraFacade().find_ticket_by_key('SHOP-1234')
print(ticket.get_developed_by())
print(ticket.get_sprint())
print(ticket.get_team_name())
print(ticket.get_status())
print(ticket.get_estimation())
```

2. search tickets 

- create a JQL (Jira Query Language) with JQL Builder
```python
from JQLBuilder import JQLBuilder

jql = JQLBuilder()\
    .set_project('SHOP')\
    .set_sprints_from_squads(
        squad_names=['Discovery', 'OMC'],
        sprint='04',
        quarter='3')\
    .get()
```
  - search and get the pandas dataframe
```python
from JiraFacade import JiraFacade

df = JiraFacade().get_df_from_jql(jql, max_results=100)
```