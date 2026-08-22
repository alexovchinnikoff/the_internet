# pages/checkboxes_page.py

import pytest
from playwright.sync_api import Page, expect

class CheckBoxesPageElms:
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//h3[contains(text(), 'Checkboxes')]")
        # self.page_header = page.locator("h3", has_text="Checkboxes'")
        self.page_checkboxes = page.locator("xpath=//input[@type='checkbox']")
        # self.page_text = page.locator("input", has_text = "checkbox")
        self.checked_checkboxes = page.locator("xpath=//input[@type='checkbox' and @checked]")
        # self.page_text = page.locator("input", has_text = "checkbox")
class CheckBoxesPage:
    def __init__(self, page: Page, elms: CheckBoxesPageElms):
        self.page = page
        self.elms = elms

    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")
        return self

    def header_and_checkboxes_visible(self):
        expect(self.elms.page_header).to_be_visible()
        expect(self.elms.page_checkboxes).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/checkboxes")

    def click_checkboxes(self):
        self.elms.page_checkboxes.first.click()