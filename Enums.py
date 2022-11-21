class Enums(object):
    project_shopping = 'SHOP'

    field_squad_name = 'customfield_10600'
    field_estimation = 'customfield_10521'
    field_sprint = 'customfield_10101'

    squad_name_promotion = 'Promotions'
    squad_name_omc = 'OMC'
    squad_name_discovery = 'Discovery'
    squad_name_magnet = 'Magnet'
    squad_name_um = 'User Management'
    squad_name_b2b = 'B2B'
    squad_name_plus = 'Plus'
    squad_name_ds = 'Digistyle'

    squads_shopping_core = [
        squad_name_omc,
        squad_name_discovery,
        squad_name_plus,
    ]

    squads_shopping = [
        squad_name_promotion,
        squad_name_omc,
        squad_name_discovery,
        squad_name_magnet,
        squad_name_um,
        squad_name_b2b,
        squad_name_plus,
        squad_name_ds,
    ]

    status_analysis = 'Analysis'
    status_product_backlog = '"Product Backlog"'
    status_sprint_backlog = '"Sprint Backlog"'
    status_in_progress = '"In Progress"'
    status_code_review = '"Code Review"'
    status_ready_to_test = '"Ready To Test"'
    status_testing = 'Testing'
    status_test_passed = '"Test Passed"'
    status_revision = 'Revision'
    status_ready_to_deploy = '"Ready To Deploy"'
    status_deployed = 'Deployed'
    status_done = 'Done'
    status_blocked = 'Blocked'
    status_closed = 'Closed'

    label_out_of_plan = 'OutOfPlan'
