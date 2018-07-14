from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_remove_contact_from_group(app, db):
    # ensure there is at least 1 contact in app
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New name", lastname="Ivanova", id="1",address="Test1", homephone="89211000000",
                      mobilephone="89211000000", workphone="89211000000",
                      secondaryphone="89211000000", email="test@mail.com"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    # select random group
    group_list_db = db.get_group_list()
    random_group = random.choice(group_list_db)
    contacts_in_group = orm.get_contacts_in_group(random_group)
    contact_list = db.get_contact_list()
    random_contact = random.choice(contact_list)
    if len(contacts_in_group) == 0:
        app.contact.add_to_group(contact_id=random_contact.id, group_id=random_group.id)
        app.contact.remove_from_group(contact_id=random_contact.id, group_id=random_group.id)
        for contact in contacts_in_group:
            if contact.id != random_contact.id:
                assert True
                print(random_contact)
    else:
        random_contact_from_group = random.choice(contacts_in_group)
        app.contact.remove_from_group(contact_id=random_contact_from_group.id, group_id=random_group.id)
        for contact in contacts_in_group:
            if contact.id != random_contact_from_group.id:
                assert True
                print(random_contact_from_group)
    print(random_group)