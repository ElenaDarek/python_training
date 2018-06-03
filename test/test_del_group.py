# -*- coding: utf-8 -*-

def test_delete_first_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    app.group.delete_first_group()
    app.group.return_to_group_page()
