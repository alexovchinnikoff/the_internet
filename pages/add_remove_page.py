# pages/add_remove_elms_page.py

import pytest
from playwright.sync_api import Page, expect

class AddRemovePageElms:
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//h3[contains(text(), 'Add/Remove Elements')]")
        # self.page_header = page.locator("h3", has_text="Add/Remove Elements")
        self.add_button = page.locator("xpath=.//button[contains(text(), 'Add Element')]")
        # self.add_button = page.locator("button", has_text="Add Element")
        self.delete_buttons = page.locator("xpath=.//button[contains(text(), 'Delete')]")
        # self.delete_buttons = page.locator("div#elements > button")
        # self.delete_buttons = page.locator("div.elements button")

class AddRemovePage:
    def __init__(self, page: Page, elms: AddRemovePageElms):
        self.page = page
        self.elms = elms

    # Методы-действия
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    def click_add_button(self):
        self.elms.add_button.click()

    def click_first_delete(self):
        self.elms.delete_buttons.first.click()

    def click_second_delete(self):
        self.elms.delete_buttons.nth(1).click()

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def page_header_visible(self):
        expect(self.elms.page_header).to_be_visible()

    def add_button_visible(self):
        expect(self.elms.add_button).to_be_visible()

    def add_button_count(self, count: int):
        expect(self.elms.add_button).to_have_count(count)

    def one_add_button(self):
        expect(self.elms.add_button).to_have_count(1)

    def delete_buttons_count(self, count: int):
        expect(self.elms.delete_buttons).to_have_count(count)

    def no_delete_buttons(self):
        expect(self.elms.delete_buttons).to_have_count(0)

    def one_delete_buttons(self):
        expect(self.elms.delete_buttons).to_have_count(1)

    def two_delete_buttons(self):
        expect(self.elms.delete_buttons).to_have_count(2)