# -*- coding: utf-8 !-*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="gr1.1", header="gr1.2", footer="gr1.3"))
    app.group.return_to_group_page()
    app.session.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_group_page()
    app.session.logout()

