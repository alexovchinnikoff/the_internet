# pages/mainpage_2.py

import pytest
from playwright.sync_api import Page, expect

# создаем класс(шаблон страницы), в который пишем локаторы элементов страницы
class MainPageElms:
    def __init__(self, page: Page):
        self.welcome_header = page.locator("xpath=.//h1[contains(text(), 'Welcome to the-internet')]")
        # self.welcome_header = page.locator("h1", has_text="Welcome to the-internet")
        self.second_header = page.locator("xpath=.//h2[contains(text(), 'Available Examples')]")
        # self.second_header = page.locator("h2", has_text="Available Examples")
        self.links = page.locator("xpath=.//div[@id='content']/li/u/a")
        # self.links = page.locator("div#content ul li a")
        self.link_abtest = page.locator("xpath=.//a[contains(text(), 'A/B Testing')]")
        # self.link_abtest = page.locator("a", has_text="A/B Testing")
        self.link_addremoveelms = page.locator("xpath=.//a[contains(text(), 'Remove Elements')]")
        # self.link_addremoveelms = page.locator("a", has_text="Add/Remove Elements")
        self.link_basicauth = page.locator("xpath=.//a[contains(text(), 'Basic Auth')]")
        # self.link_basicauth = page.locator("a", has_text="Basic Auth")
        self.link_brokenimgs = page.locator("xpath=.//a[contains(text(), 'Broken Images')]")
        # self.link_brokenimgs = page.locator("a", has_text="Broken Images")
        self.link_chaldom = page.locator("xpath=.//a[contains(text(), 'Challenging DOM')]")
        # self.link_chaldom = page.locator("a", has_text="Challenging DOM")
        self.link_checkboxes = page.locator("xpath=.//a[contains(text(), 'Checkboxes')]")
        # self.link_checkboxes = page.locator("a", has_text="Checkboxes")
class MainPage:
    def __init__(self, page: Page, elms: MainPageElms):
        self.page = page # берем ссылку на страницу из теста
        self.elms = elms # берем ссылку на объект с локаторами
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/")
        return self
    def click_abtest(self):
        self.elms.link_abtest.click() # self.elms.link_abtest.click()
        return self
    def click_addremoveelms(self):
        self.elms.link_addremoveelms.click()
        return self
    def click_basicauth(self):
        self.elms.link_basicauth.click()
        return self
    def click_brokenimgs(self):
        self.elms.link_brokenimgs.click()
        return self
    def click_chaldom(self):
        self.elms.link_chaldom.click()
        return self
    def click_checkboxes(self):
        self.elms.link_checkboxes.click()
        return self

    # функции проверки (Методы-проверки - возвращают True/False или ничего, просто ждут)
    # Проверяем попадание на стартовую страницу
    '''
    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/")

    # Проверяем заголовки: рендеринг, состояние
    def headers_visible(self):
        expect(self.elms.welcome_header).to_be_visible()
        expect(self.elms.second_header).to_be_visible()

    # Проверяем ссылки: рендеринг, состояние UI, ложные клики
    def links_visible(self):
        expect(self.elms.link_abtest).to_be_visible()
        expect(self.elms.link_addremoveelms).to_be_visible()
        expect(self.elms.link_basicauth).to_be_visible()
        expect(self.elms.link_brokenimgs).to_be_visible()
        expect(self.elms.link_chaldom).to_be_visible()
        expect(self.elms.link_checkboxes).to_be_visible()
    # def links_enabled(self): # не проверяем

    # проверяем количество ссылок
    def links_count(self, expected_count: int): # проверяем количество ссылок
        expect(self.elms.links).to_have_count(expected_count)
    '''
