# -*- coding: utf-8!-*-
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

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.phone)
        self.change_field_value("email", contact.email)


    def select_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #fill contact form
        self.fill_contact_form(contact)
        #submit modification
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))




