# -*- coding: utf-8-*-
from sys import maxsize


class Contact:

    def __init__(self, name=None, surname=None, address=None, phone=None, email=None, id=None):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.email = email
        self.id = id



    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
