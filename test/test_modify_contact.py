# -*- coding: utf-8!-*-
from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    contact = Contact(firstname="New name", lastname="Ivanova", id="1",address="Test1", homephone="89211000000",
                      mobilephone="89211000000", workphone="89211000000",
                      secondaryphone="89211000000", email="test@mail.com")
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(contact)
    old_contacts = db.get_contact_list()
    app.open_home_page()
    random_contact = random.choice(old_contacts)
    old_contacts.remove(random_contact)
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(random_contact.id, contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


