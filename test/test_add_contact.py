# -*- coding: utf-8-*-
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.contact.open_new_contact_page()
    app.contact.create_contact(Contact(name="Elena", surname="Darek", address="Test", phone="89210000000", email="elenadarek@gmail.com"))

