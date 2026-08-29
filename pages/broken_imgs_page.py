# pages/broken_imgs_page.py

import pytest
from playwright.sync_api import Page, expect


class BrokenImgsPageElms:


    PAGE_HEADER = "xpath=//h3[contains(text(), 'Broken Images')]"
    PAGE_IMAGES = "xpath=//img[contains(@src, '.jpg')]"

    '''
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//h3[contains(text(), 'Broken Images')]")
        # self.page_header = page.locator("h3", has_text="Broken Images")
        self.page_images = page.locator("xpath=.//img[contains(@src, '.jpg')]")
        # self.page_images = page.locator("img[src$='.jpg']")
    '''


class BrokenImgsPage:


    # создаем функцию начальных значений (ссылка на браузер из теста и локаторы)
    def __init__(self, page: Page, elms: BrokenImgsPageElms):
        self.page = page
        self.elms = elms

    # создаем функции, имитация действий пользователя (Методы-действия)
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/broken_images")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def page_header_visible(self):
        expect(self.elms.PAGE_HEADER).to_be_visible()

    # def page_images_visible(self):
        # expect(self.page_images).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/broken_images")  # Проверяем урл
        return self

    def images_count(self, expected_count: int):
        expect(self.elms.PAGE_IMAGES).to_have_count(expected_count)
        return self