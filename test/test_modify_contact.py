# -*- coding: utf-8!-*-
from model.contact import Contact

def test_modify_group_name(app):
    app.open_home_page()
    app.contact.modify_first_contact(Contact(name="New name", surname="Ivanova", address="test_address", phone="89211110000", email="test@mail.com"))
