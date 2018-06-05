# -*- coding: utf-8-*-
from model.contact import Contact


def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(name="Elena", surname="Darek", address="Test", phone="89210000000", email="elenadarek@gmail.com"))
    app.contact.delete_first_contact()


