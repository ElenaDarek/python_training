from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    # ensure there is at least 1 contact in app
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New name", lastname="Ivanova", id="1",address="Test1", homephone="89211000000",
                      mobilephone="89211000000", workphone="89211000000",
                      secondaryphone="89211000000", email="test@mail.com"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    # select random contact from contacts list
    contact_list = db.get_contact_list()
    random_contact = random.choice(contact_list)
    group_list_db = db.get_group_list()
    random_group = random.choice(group_list_db)
    # add contact to random group
    app.contact.add_to_group(contact_id=random_contact.id, group_id=random_group.id)
    # assertion
    contacts_in_group = orm.get_contacts_in_group(random_group)
    for contact in contacts_in_group:
        if contact.id == random_contact.id:
            assert True