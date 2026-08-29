# context_menu_page.py

import pytest
from playwright.sync_api import Page, expect


class ContextMenuPageElms:


    PAGE_HEADER = "xpath=//h3[contains(text(), 'Context Menu')]"
    PAGE_TEXT_UPPER = "xpath=//p[contains(text(), 'Context menu items are custom')]"
    PAGE_TEXT_LOWER = "xpath=//p[contains(text(), 'Right-click in the box below')]"
    PAGE_BOX = "xpath=//div[@id='hot-spot']"


    '''
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//h3[contains(text(), 'Context Menu')]")
        # self.page_header = page.locator("h3", has_text="Context Menu")
        self.page_text_upper = page.locator("xpath=.//p[contains(text(), 'Context menu items are custom')]")
        # self.page_text_upper = page.locator("p", has_text="Context menu items are custom")
        self.page_text_lower = page.locator("xpath=.//p[contains(text(), 'Right-click in the box below')]")
        # self.page_text_lower = page.locator("p", has_text="Right-click in the box below")

        self.page_box = page.locator("xpath=//div[@id='hot-spot']")
        # self.page_text = page.locator("input", has_text = "checkbox")
    '''

class ContextMenuPage:


    def __init__(self, page: Page, elms: ContextMenuPageElms):
        self.page = page
        self.elms = elms

    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")
        return self

    def header_and_texts_visible(self):
        expect(self.elms.PAGE_HEADER).to_be_visible()
        expect(self.elms.PAGE_TEXT_UPPER).to_be_visible()
        expect(self.elms.PAGE_TEXT_LOWER).to_be_visible()
        expect(self.elms.PAGE_BOX).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/context_menu")

    def right_click_page_box(self):
        self.page.locator(self.elms.PAGE_BOX).right.click()