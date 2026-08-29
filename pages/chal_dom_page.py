# pages/chal_dom_page.py

import pytest
from playwright.sync_api import Page, expect


class ChalDomPageElms:


    PAGE_HEADER = "xpath=//div[@class='example']/h3[contains(text(), 'Challenging DOM')]"
    PAGE_TEXT = "xpath=//div[@class='example']/p[contains(text(), 'The hardest part in automated web testing')]"
    BUTTONS = "xpath=//div[@class='large-2 columns']/a"
    BUTTON_UPPER = "xpath=//a[@class='button'][1]"
    BUTTON_MIDDLE = "xpath=//a[@class='button alert']"
    BUTTON_LOWER = "xpath=//a[@class='button success']"
    TABLE = "xpath=//table"
    THEAD = "xpath=//table/thead"
    THEAD_ROW = "xpath=//table/thead/tr"
    THEAD_HEADERS = "xpath=//table/thead/tr/th"
    LOREM = "xpath=//th[contains(text(), 'Lorem')]"
    IPSUM = "xpath=//th[contains(text(), 'Ipsum')]"
    DOLOR = "xpath=//th[contains(text(), 'Dolor')]"
    SIT = "xpath=//th[contains(text(), 'Sit')]"
    AMET = "xpath=//th[contains(text(), 'Amet')]"
    DICERET = "xpath=//th[contains(text(), 'Diceret')]"
    ACTION = "xpath=//th[contains(text(), 'Action')]"

    TABLE_BODY = "xpath=//table/tbody"
    TABLE_BODY_ROWS = "xpath=//table/tbody/tr"
    TABLE_BODY_HEADERS = "xpath=//table/tbody/tr/td"
    HREF_EDIT = "xpath=//a[contains(text(), 'edit')]"
    HREF_DELETE = "xpath=//a[contains(text(), 'delete')]"

    PAGE_CANVAS = 'xpath=//div//canvas[@width="599" and @height="200"]'


    '''
    def __init__(self, page: Page):
        self.page_header = page.locator("xpath=.//div[@class='example']/h3[contains(text(), 'Challenging DOM')]")
        # self.page_header = page.locator("div.example", has_text="Challenging DOM")

        #main>section>div.profile__image
        #main div.profile__image
        #main>section>div[class='profile__image']
        #main div[class='profile__image']

        self.page_text = page.locator("div.example", has_text="The hardest part in automated web testing")
        self.buttons = page.locator("a.button")
        self.button_upper = page.locator("a.button").first
        self.button_middle = page.locator("a.alert")
        self.button_lower = page.locator("a.success")
        self.table = page.locator("div table")
        self.thead = page.locator("table  thead")
        self.thead_row = page.locator("table thead tr")
        self.thead_headers = page.locator("table thead tr th")
        self.thead_header_0 = page.locator("table thead th", has_text="Lorem")
        self.thead_header_1 = page.locator("table thead th", has_text="Ipsum")
        self.thead_header_2 = page.locator("table thead th", has_text="Dolor")
        self.thead_header_3 = page.locator("table thead th", has_text="Sit")
        self.thead_header_4 = page.locator("table thead th", has_text="Amet")
        self.thead_header_5 = page.locator("table thead th", has_text="Diceret")
        self.thead_header_6 = page.locator("table thead th", has_text="Action")

        self.table_body = page.locator("table tbody")
        self.table_body_rows = page.locator("table tbody tr")
        self.table_body_headers = page.locator("table tbody tr td")
        self.href_edit = page.locator("table tbody a", has_text="edit")
        self.href_delete = page.locator("table tbody a", has_text="delete")


        self.page_canvas = page.locator('xpath=//div//canvas[@width="599" and @height="200"]')
    '''


class ChalDomPage:


    def __init__(self, page: Page, elms: ChalDomPageElms):
        self.page = page
        self.elms = elms

    # создаем функции, имитация действий пользователя (Методы-действия)
    def go_to(self):
        self.page.goto("https://the-internet.herokuapp.com/challenging_dom")
        return self  # Возвращаем self, чтобы можно было делать цепочки (опционально)

    # Методы-проверки (возвращают True/False или ничего, просто ждут)
    def page_header_visible(self):
        expect(self.elms.PAGE_HEADER).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/challenging_dom")  # Проверяем урл
        return self
