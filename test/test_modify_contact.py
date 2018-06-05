# -*- coding: utf-8!-*-
from model.contact import Contact

def test_modify_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(name="Elena", surname="Darek", address="Test", phone="89210000000", email="elenadarek@gmail.com"))
    app.contact.modify_first_contact(Contact(name="New name", surname="Ivanova", address="test_address", phone="89211110000", email="test@mail.com"))
