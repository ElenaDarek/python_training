# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="gr1.1", header="gr1.2", footer="gr1.3"))
    app.return_to_group_page()
    app.logout()

def test_add_empty_group(app):
    wd = self.wd
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="", footer=""))
    app.return_to_group_page()
    app.logout()

