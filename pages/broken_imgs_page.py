# pages/broken_imgs_page.py

import pytest
from playwright.sync_api import Page, expect

# объявляем класс
class BrokenImgsPage:
    # создаем функцию начальных значений (ссылка на браузер из теста и локаторы)
    def __init__(self, page: Page):
        self.page = page
        # Локаторы (храним их как свойства класса)
        self.page_header = page.locator("h3", has_text="Broken Images")
        self.page_images = page.locator("img[src$='.jpg']")

    # создаем функции, имитация действий пользователя (Методы-действия)
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/broken_images")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def page_header_visible(self):
        expect(self.page_header).to_be_visible()

    # def page_images_visible(self):
        # expect(self.page_images).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/broken_images")  # Проверяем урл
        return self

    def images_count(self, expected_count: int):
        expect(self.page_images).to_have_count(expected_count)
        return self