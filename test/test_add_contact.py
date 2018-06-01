# -*- coding: utf-8-*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_new_contact_page()
    app.contact.contact(Contact(name="Elena", surname="Darek", address="Test", phone="89210000000", email="elenadarek@gmail.com"))
    app.session.logout()




