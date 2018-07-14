from fixture.orm import ORMFixture

__author__ = 'tester'

from fixture.orm import ORMFixture
from model.group import Group

check = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = check.get_contacts_in_group(Group(id="194"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()