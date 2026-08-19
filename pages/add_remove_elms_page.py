# pages/add_remove_elms_page.py

import pytest
from playwright.sync_api import Page, expect

class AddRemoveElmsPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_header = page.locator("h3", has_text="Add/Remove Elements")
        self.add_button = page.locator("button", has_text="Add Element")
        self.delete_buttons = page.locator("div#elements > button")

    # Методы-действия (то, что делает пользователь)
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    def click_add_button(self):
        self.add_button.click()

    def click_first_delete(self):
        self.delete_buttons.first.click()

    def click_second_delete(self):
        self.delete_buttons.nth(1).click()

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def page_header_visible(self):
        expect(self.page_header).to_be_visible()

    def add_button_visible(self):
        expect(self.add_button).to_be_visible()

    def add_button_count(self, count: int):
        expect(self.add_button).to_have_count(count)

    def one_add_button(self):
        expect(self.add_button).to_have_count(1)

    def delete_buttons_count(self, count: int):
        expect(self.delete_buttons).to_have_count(count)

    def no_delete_buttons(self):
        expect(self.delete_buttons).to_have_count(0)

    def one_delete_buttons(self):
        expect(self.delete_buttons).to_have_count(1)

    def two_delete_buttons(self):
        expect(self.delete_buttons).to_have_count(2)