# pages/abtest_page.py

import pytest
from playwright.sync_api import Page, expect
from base.user_client import User


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

    url = "https://the-internet.herokuapp.com/abtest"

'''
    def __init__(self, page: Page, elms: ABTestPageElms):
        self.page = page
        self.elms = elms
        self.user = User(page)

    def go_to(self):
        self.user.open_page(self.url)
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    def wait_for_load(self, sec: int = 2):
        self.user.wait_sec(sec)
        return self

    def header_and_text_visible(self):
        expect(self.page.locator(self.elms.PAGE_HEADER)).to_be_visible()
        expect(self.page.locator(self.elms.PAGE_TEXT)).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url(self.url)
'''