# -*- coding: utf-8-*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(name="Elena", surname="Darek", address="Test", phone="89210000000", email="elenadarek@gmail.com"))
    app.open_home_page()
    app.contact.delete_first_contact()


