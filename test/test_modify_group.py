# -*- coding: utf-8! -*-
from model.group import Group

def test_modify_group_name(app):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))
    app.group.return_to_group_page()


def test_modify_group_header(app):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New header"))
    app.group.return_to_group_page()
