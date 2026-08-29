# pages/checkboxes_page.py

import pytest
from playwright.sync_api import Page, expect


class CheckBoxesPageElms:


    PAGE_HEADER = "xpath=//h3[contains(text(), 'Checkboxes')]"
    PAGE_CHECKBOXES = "xpath=//input[@type='checkbox']"
    CHECKED_CHECKBOXES = "xpath=//input[@type='checkbox' and @checked]"
    '''
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//h3[contains(text(), 'Checkboxes')]")
        # self.page_header = page.locator("h3", has_text="Checkboxes")
        self.page_checkboxes = page.locator("xpath=//input[@type='checkbox']")
        # self.page_text = page.locator("input", has_text = "checkbox")
        self.checked_checkboxes = page.locator("xpath=//input[@type='checkbox' and @checked]")
        # self.page_text = page.locator("input", has_text = "checkbox")
    '''


class CheckBoxesPage:


    def __init__(self, page: Page, elms: CheckBoxesPageElms):
        self.page = page
        self.elms = elms

    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")
        return self

    def header_and_checkboxes_visible(self):
        expect(self.elms.PAGE_HEADER).to_be_visible()
        expect(self.elms.PAGE_CHECKBOXES).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/checkboxes")

    def click_checkbox_upper(self):
        self.page.locator(self.elms.PAGE_CHECKBOXES).first.click()

    def click_checkbox_lower(self):
        self.page.locator(self.elms.PAGE_CHECKBOXES).nth(1).click()