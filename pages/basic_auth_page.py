# pages/abtest_page.py

import pytest
from playwright.sync_api import Page, expect

class BasicAuthPageElms:
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//h3[contains(text(), 'Basic Auth')]")
        # self.page_header = page.locator("h3", has_text="Basic Auth")
        self.page_text = page.locator("xpath=//p[contains(text(), 'Congratulations!')]")
        # self.page_header = page.locator("p", has_text="Congratulations!)
class BasicAuthPage:
    # создаем функцию начальных значений (ссылка на браузер из теста и локаторы)
    def __init__(self, page: Page, elms: BasicAuthPageElms):
        self.page = page
        self.elms = elms

    def go_to(self):
        self.page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    def header_and_text_visible(self):
        expect(self.elms.page_header).to_be_visible()
        expect(self.elms.page_text).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/basic_auth")  # Проверяем урл