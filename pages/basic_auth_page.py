# pages/abtest_page.py

import pytest
from playwright.sync_api import Page, expect

# объявляем класс
class BasicAuthPage:
    # создаем функцию начальных значений (ссылка на браузер из теста и локаторы)
    def __init__(self, page: Page):
        self.page = page
        # Локаторы (храним их как свойства класса)
        self.page_header = page.locator("h3", has_text="Basic Auth")
        self.page_text = page.locator("xpath=//p[contains(text(), 'Congratulations! You must have the proper credentials.')]")

    # создаем функции, имитация действий пользователя (Методы-действия)
    def go_to(self):
        self.page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def header_and_text_visible(self):
        expect(self.page_header).to_be_visible()
        expect(self.page_text).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/basic_auth")  # Проверяем урл