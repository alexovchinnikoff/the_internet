# tests/ui/test_checkboxes_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.checkboxes_page import CheckBoxesPage, CheckBoxesPageElms

# Открывает страницу
def test_checkboxes_page_open(page: Page):
    # класс
    user = User(page)
    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    user.click_element(MainPageElms.LINK_CHECKBOXES)
    user.wait_sec(1)

    elms = CheckBoxesPageElms()

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_checkboxes = page.locator(elms.PAGE_CHECKBOXES)

    # проверки
    assert "/checkboxes" in page.url
    assert page_header.is_visible()
    assert page_checkboxes.count() == 2

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Виден текст: {page_checkboxes.count()}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_checkboxes_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_checkboxes_page_screenshot.png'")