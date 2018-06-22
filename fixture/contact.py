# -*- coding: utf-8-*-
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self,app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def select_first_contact(self):
        self.select_contact_by_index()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id=')]")[index].click()
        #fill contact form
        self.fill_contact_form(contact)
        #submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return self.contact_cache

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id=')]")[index].click()
        #row = wd.find_elements_by_name("entry")[index]
        #cell = row.find_elements_by_tag_name("td")[7]
        #cell.find_element_by_tag_name("a").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, mobilephone=mobilephone,workphone=workphone,
                       secondaryphone=secondaryphone,  email=email, email2=email2, email3=email3,)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone)



