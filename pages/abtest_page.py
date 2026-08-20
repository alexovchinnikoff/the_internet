# pages/abtest_page.py

import pytest
from playwright.sync_api import Page, expect

class ABTestPageElms:
    def __init__(self, page: Page):
        self.page_header = page.locator("h3", has_text="A/B Test Control")
        self.page_text = page.locator("xpath=//p[contains(text(), 'Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through).')]")

class ABTestPage:
    # создаем функцию начальных значений (ссылка на браузер из теста и локаторы)
    def __init__(self, page: Page, elms: ABTestPageElms):
        self.page = page
        self.elms = elms

    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/abtest")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    def header_and_text_visible(self):
        expect(self.elms.page_header).to_be_visible()
        expect(self.elms.page_text).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/abtest")  # Проверяем урл