class Enums(object):
    # projects
    project_shopping = 'SHOP'
    project_ds = 'Digistyle'

    # jira custom fields
    field_squad_name = 'customfield_10600'
    field_development_estimation = 'customfield_10106'
    field_sprint = 'customfield_10101'
    field_developed_by = 'customfield_10202'
    field_epic_ticket = 'customfield_10102'
    field_test_effort = 'customfield_11200'

    # squad names
    squad_name_promotion = 'Promotion'
    squad_name_omc = 'OMC'
    squad_name_discovery = 'Discovery'
    squad_name_magnet = 'Magnet'
    squad_name_um = 'UM'
    squad_name_b2b = 'B2B'
    squad_name_plus = 'Plus'

    squads_shopping = [
        # squad_name_promotion,
        squad_name_omc,
        squad_name_discovery,
        squad_name_magnet,
        squad_name_um,
        squad_name_b2b,
        squad_name_plus,
    ]

    # statuses
    status_analysis = 'Analysis'
    status_product_backlog = 'Product Backlog'
    status_sprint_backlog = 'Sprint Backlog'
    status_in_progress = 'In Progress'
    status_code_review = 'Code Review'
    status_ready_to_test = 'Ready To Test'
    status_testing = 'Testing'
    status_test_passed = 'Test Passed'
    status_revision = 'Revision'
    status_ready_to_deploy = 'Ready To Deploy'
    status_deployed = 'Deployed'
    status_done = 'Done'
    status_blocked = 'Blocked'
    status_closed = 'Closed'

    # labels
    label_out_of_plan = 'OutOfPlan'
    label_front_end = 'Front-End'
    label_back_end = 'Back-End'
    label_design = 'Design'
    label_app = 'App'

    #types
    type_epic = 'Epic'
    type_bug = 'Bug'
    type_feature = 'Feature'
    type_improvement = 'Improvement'
