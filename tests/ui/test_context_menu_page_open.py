# tests/ui/test_checkboxes_page_open.py

import pytest, time
from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.context_menu_page import ContextMenuPage, ContextMenuPageElms

# Открывает страницу
def test_context_menu_page_open(page: Page):
    # класс
    user = User(page)
    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    user.click_element(MainPageElms.LINK_CONTEXTMENU)
    user.wait_sec(1)

    elms = ContextMenuPageElms()

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_text_upper = page.locator(elms.PAGE_TEXT_UPPER)
    page_text_lower = page.locator(elms.PAGE_TEXT_LOWER)

    # проверки
    user.make_screenshot("check_context_menu_page_open")
    assert "/context_menu" in page.url, "Урл корректный"
    assert page_header.is_visible(), "Заголовок виден"
    assert page_text_upper.count() == 1, "Количество чекбоксов корректное"
    assert page_text_lower.count() == 1, "Количество чекбоксов корректное"
    # assert page.right_click_page_box() == <script> function displayMessage() {window.alert('You selected a context menu')} </script>

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Виден заголовок страницы: {page_text_upper.inner_text()}")
    print(f"📄 Виден заголовок страницы: {page_text_lower.inner_text()}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_checkboxes_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_checkboxes_page_screenshot.png'")