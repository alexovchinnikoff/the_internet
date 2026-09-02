# tests/ui/test_basic_auth_page_open.py

import pytest, time
from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.basic_auth_page import BasicAuthPage, BasicAuthPageElms

def test_basic_auth_page_open(page: Page):
    # Инициализируем класс
    user = User(page)

    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    user.click_element(MainPageElms.LINK_BASICAUTH)
    user.wait_sec(1)

    user.open_page(BasicAuthPage.url)

    elms = BasicAuthPageElms()

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_text = page.locator(elms.PAGE_TEXT)

    # проверки
    assert "/basic_auth" in page.url
    assert page_header.is_visible()
    assert page_text.is_visible()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url }")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Виден текст: {page_text.inner_text()}")
    print("⏳ Ожидание 3 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_basic_auth_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_basic_auth_page_screenshot.png'")