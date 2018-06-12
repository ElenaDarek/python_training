# -*- coding: utf-8!-*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Elena", lastname="Darek", address="Test", mobile="89210000000", email="elenadarek@gmail.com"))
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New name", lastname="Ivanova", address="test_address", mobile="89211110000", email="test@mail.com")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


