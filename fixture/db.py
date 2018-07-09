import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select contact_id, contact_firstname, contact_lastname, contact_address, contact_address,\
                                    contact_homephone, contact_mobilephone, contact_workphone, contact_secondaryphone, \
                                   contact_email from contact_list")
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobilephone, workphone, secondaryphone, email) = row
                list.append(
                    Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=homephone,
                            mobilephone=mobilephone, workphone=workphone,
                            secondaryphone=secondaryphone, email=email))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()