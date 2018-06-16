# -*- coding: utf-8!-*-
from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Elena", lastname="Darek", address="Test", mobile="89210000000", email="elenadarek@gmail.com"))
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New name", lastname="Ivanova", address="test_address", mobile="89211110000", email="test@mail.com")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    app.open_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


