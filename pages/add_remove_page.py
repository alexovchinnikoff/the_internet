# pages/add_remove_elms_page.py

import pytest
from playwright.sync_api import Page, expect
from base.user_client import User

class AddRemovePageElms:


    PAGE_HEADER = "xpath=//h3[contains(text(), 'Add/Remove Elements')]"
    ADD_BUTTON = "xpath=//button[contains(text(), 'Add Element')]"
    DELETE_BUTTONS = "xpath=//button[contains(text(), 'Delete')]"
    DELETE_FIRST = "xpath=//button[contains(text(), 'Delete')][1]"
    DELETE_SECOND = "xpath=//button[contains(text(), 'Delete')][2]"
    '''
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//h3[contains(text(), 'Add/Remove Elements')]")
        # self.page_header = page.locator("h3", has_text="Add/Remove Elements")
        self.add_button = page.locator("xpath=.//button[contains(text(), 'Add Element')]")
        # self.add_button = page.locator("button", has_text="Add Element")
        self.delete_buttons = page.locator("xpath=.//button[contains(text(), 'Delete')]")
        # self.delete_buttons = page.locator("div#elements > button")
        # self.delete_buttons = page.locator("div.elements button")
    '''


class AddRemovePage:

    url = "https://the-internet.herokuapp.com/add_remove_elements/"

'''
    def __init__(self, page: Page, elms: AddRemovePageElms):
        self.page = page
        self.elms = elms
        self.user = User(page)

    def go_to(self):
        self.user.open_page(self.url)
        return self

    def wait_for_load(self, sec: int = 2):
        self.user.wait_sec(sec)
        return self

    def click_add_button(self):
        self.user.click_element(self.page.locator(self.elms.ADD_BUTTON))

    def click_first_delete(self):
        self.user.click_element(self.page.locator(self.elms.DELETE_BUTTONS).first)

    def click_second_delete(self):
        self.user.click_element(self.page.locator(self.elms.DELETE_BUTTONS).nth(1))

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def page_header_visible(self):
        expect(self.page.locator(self.elms.PAGE_HEADER)).to_be_visible()

    def add_button_visible(self):
        expect(self.page.locator(self.elms.ADD_BUTTON)).to_be_visible()

    def add_button_count(self, count: int):
        expect(self.page.locator(self.elms.ADD_BUTTON)).to_have_count(count)

    def one_add_button(self):
        expect(self.page.locator(self.elms.ADD_BUTTON)).to_have_count(1)

    def delete_buttons_count(self, count: int):
        expect(self.page.locator(self.elms.DELETE_BUTTONS)).to_have_count(count)

    def no_delete_buttons(self):
        expect(self.page.locator(self.elms.DELETE_BUTTONS)).to_have_count(0)

    def one_delete_buttons(self):
        expect(self.page.locator(self.elms.DELETE_BUTTONS)).to_have_count(1)

    def two_delete_buttons(self):
        expect(self.page.locator(self.elms.DELETE_BUTTONS)).to_have_count(2)
'''