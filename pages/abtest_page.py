# pages/abtest_page.py

import pytest
from playwright.sync_api import Page, expect


class ABTestPageElms:
    PAGE_HEADER = "xpath=//h3[contains(text(), 'A/B Test')]"
    PAGE_TEXT = "xpath=//p[contains(text(), 'Also known as split testing.')]"






    '''
    def __init__(self, page: Page):
        # self.page_header = page.locator("xpath=.//h3[contains(text(), 'A/B Test')]")
        self.page_header = page.locator("h3", has_text="A/B Test")
        # self.page_text = page.locator("xpath=.//p[contains(text(), 'Also known as split testing.')]")
        self.page_text = page.locator("p", has_text="Also known as split testing.")
    '''


class ABTestPage:


    def __init__(self, page: Page, elms: ABTestPageElms):
        self.page = page
        self.elms = elms

    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/abtest")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    def header_and_text_visible(self):
        expect(self.elms.PAGE_HEADER).to_be_visible()
        expect(self.elms.PAGE_TEXT).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/abtest")  # Проверяем урл