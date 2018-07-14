import re
from model.contact import Contact


def test_contact_check(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="Elena", lastname="Darek", id="1", address="Test", homephone="89210000000",
                                   mobilephone="89210000000", workphone="89210000000",secondaryphone="89210000000",
                                   email="elenadarek@gmail.com", email2="test1@mail.com", email3="test2@gmail.com"))
    db_list = db.get_contact_list()
    sorted_db_list = sorted(db_list, key=Contact.id_or_max)
    ui_list = app.contact.get_contacts_list()
    list_length = len(ui_list)
    sorted_ui_list = sorted(ui_list, key=Contact.id_or_max)
    for index in range(0, list_length):
        assert sorted_ui_list[index].lastname == sorted_db_list[index].lastname
        assert sorted_ui_list[index].firstname == sorted_db_list[index].firstname
        assert sorted_ui_list[index].address == sorted_db_list[index].address
        assert sorted_ui_list[index].all_emails_from_home_page == merge_emails_like_on_home_page(sorted_db_list[index])
        assert sorted_ui_list[index].all_phones_from_home_page == merge_phones_like_on_home_page(sorted_db_list[index])


def clear_for_phones(s):
    return re.sub("[() -.]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_for_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))

def clear_for_emails(s):
    return re.sub("^\s*", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_for_emails(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))