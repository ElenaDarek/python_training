# -*- coding: utf-8-*-
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Elena", lastname="Darek",id="1", address="Test", homephone="89210000000",
                                           mobilephone="89210000000", workphone="89210000000",
                                           secondaryphone="89210000000", email="elenadarek@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.open_home_page()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


