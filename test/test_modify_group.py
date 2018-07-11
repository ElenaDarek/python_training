# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    group = Group(name="some_name", header="some_header", footer="some_footer")
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    old_groups.remove(random_group)
    group.id = random_group.id
    app.group.modify_group_by_id(random_group.id, group)
    assert len(old_groups) + 1 == app.group.count()
    #app.group.return_to_group_page()
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
#   app.group.open_groups_page()
#   if app.group.count() == 0:
#      app.group.create(Group(name="test"))
#   old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    app.group.return_to_group_page()
#   new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
