# pages/mainpage.py

import pytest
from playwright.sync_api import Page, expect

class MainPageElms: # создаем класс(шаблон страницы), в который пишем локаторы элементов страницы
    def __init__(self): # функция-метод(конструктор) пропускаем. можно в init записать локаторы так self.welcome_header = page.locator("h1", has_text="Welcome to the-internet")
        pass
    def get_welcome_header(self, page: Page): # elms = MainPageElms()  # Создали объект без страницы # elms.get_welcome_header(page).click()
        return page.locator("h1", has_text="Welcome to the-internet")
    def get_second_header(self, page: Page):
        return page.locator("h2", has_text="Available Examples")
    def get_links(self, page: Page):
        return page.locator("div#content ul li a")
    def get_link_abtest(self, page: Page):
        return page.locator("a", has_text="A/B Testing")
    def get_link_addremoveelms(self, page: Page):
        return page.locator("a", has_text="Add/Remove Elements")
    def get_link_basicauth(self, page: Page):
        return page.locator("a", has_text="Basic Auth")
    def get_link_brokenimgs(self, page: Page):
        return page.locator("a", has_text="Broken Images")
    def get_link_chaldom(self, page: Page):
        return page.locator("a", has_text="Challenging DOM")

class MainPage:
    def __init__(self, page: Page, elms: MainPageElms):
        self.page = page # берем ссылку на страницу из теста
        self.elms = elms # берем ссылку на объект с локаторами
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/")
        return self
    def click_abtest(self):
        self.elms.get_link_abtest(self.page).click() # self.elms.link_abtest.click()
        return self
    def click_addremoveelms(self):
        self.elms.get_link_addremoveelms(self.page).click()
        return self
    def click_basicauth(self):
        self.elms.get_link_basicauth(self.page).click()
        return self
    def click_brokenimgs(self):
        self.elms.get_link_brokenimgs(self.page).click()
        return self
    def click_chaldom(self):
        self.elms.get_link_chaldom(self.page).click()
        return self

    # функции проверки (Методы-проверки - возвращают True/False или ничего, просто ждут)
    # Проверяем урл
    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/")
    # Проверяем заголовки
    def headers_visible(self):
        expect(self.elms.get_welcome_header(self.page)).to_be_visible()
        expect(self.elms.get_second_header(self.page)).to_be_visible()
    # Проверяем ссылки
    def links_visible(self):
        expect(self.elms.get_link_abtest(self.page)).to_be_visible()
        expect(self.elms.get_link_addremoveelms(self.page)).to_be_visible()
        expect(self.elms.get_link_basicauth(self.page)).to_be_visible()
        expect(self.elms.get_link_brokenimgs(self.page)).to_be_visible()
        expect(self.elms.get_link_chaldom(self.page)).to_be_visible()

    def links_enabled(self):
        expect(self.elms.get_link_abtest(self.page)).to_be_enabled()
        expect(self.elms.get_link_addremoveelms(self.page)).to_be_enabled()
        expect(self.elms.get_link_basicauth(self.page)).to_be_enabled()
        expect(self.elms.get_link_brokenimgs(self.page)).to_be_enabled()
        expect(self.elms.get_link_chaldom(self.page)).to_be_enabled()

    def links_count(self, expected_count: int):
        expect(self.elms.get_links(self.page)).to_have_count(expected_count)
        return self