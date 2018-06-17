# -*- coding: utf-8!-*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", lastname="Darek", id="1", homephone="89210000000",
                      mobilephone="89210000000", workphone="89210000000",
                      secondaryphone="89210000000", email="elenadarek@gmail.com")
    app.contact.open_new_contact_page()
    app.contact.create_contact(contact)
    app.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

