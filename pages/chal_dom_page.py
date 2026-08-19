# pages/chal_dom_page.py

import pytest
from playwright.sync_api import Page, expect

class ChalDomPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_header = page.locator("h3", has_text="Challenging DOM")

    # создаем функции, имитация действий пользователя (Методы-действия)
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/challenging_dom")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def page_header_visible(self):
        expect(self.page_header).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/challenging_dom")  # Проверяем урл
        return self
