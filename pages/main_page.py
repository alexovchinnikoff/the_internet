# pages/mainpage.py

import pytest
from playwright.sync_api import Page, expect

class MainPage:
  # создаем функцию начальных значений (ссылка на браузер из теста и локаторы)
    def __init__(self, page: Page):
        # берем ссылку на страницу из теста
        self.page = page
        # Локаторы (храним их как свойства класса) по сути то что есть и можно проверить на странице
        self.welcome_header = page.locator("h1", has_text="Welcome to the-internet")
        self.second_header = page.locator("h2", has_text="Available Examples")
        self.links = page.locator("div#content ul li a")
        self.link_abtest = page.locator("a", has_text="A/B Testing")
        self.link_addremoveelms = page.locator("a", has_text="Add/Remove Elements")
        self.link_basicauth = page.locator("a", has_text="Basic Auth")
        self.link_brokenimgs = page.locator("a", has_text="Broken Images")
        self.link_chaldom = page.locator("a", has_text="Challenging DOM")

    # функции-имитация действий пользователя (Методы-действия)
    # Переход на страницу
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/")
        #return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    # Кликаем по ссылкам
    def click_abtest(self):
        self.link_abtest.click()
        return self
    def click_addremoveelms(self):
        self.link_addremoveelms.click()
        return self
    def click_basicauth(self):
        self.link_basicauth.click()
        return self
    def click_brokenimgs(self):
        self.link_brokenimgs.click()
        return self
    def click_chaldom(self):
        self.link_chaldom.click()
        return self

    # функции проверки (Методы-проверки - возвращают True/False или ничего, просто ждут)
    # Проверяем урл
    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/")
    # Проверяем заголовки
    def headers_visible(self):
        expect(self.welcome_header).to_be_visible()
        expect(self.second_header).to_be_visible()
    # Проверяем ссылки
    def links_visible(self):
        expect(self.link_abtest).to_be_visible()
        expect(self.link_addremoveelms).to_be_visible()
        expect(self.link_basicauth).to_be_visible()
        expect(self.link_brokenimgs).to_be_visible()
        expect(self.link_chaldom).to_be_visible()

    def links_enabled(self):
        expect(self.link_abtest).to_be_enabled()
        expect(self.link_addremoveelms).to_be_enabled()
        expect(self.link_basicauth).to_be_enabled()
        expect(self.link_brokenimgs).to_be_enabled()
        expect(self.link_chaldom).to_be_enabled()

    def links_count(self, expected_count: int):
        expect(self.links).to_have_count(expected_count)
        return self