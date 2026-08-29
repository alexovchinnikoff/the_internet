# tests/ui/test_checkboxes_page_open.py

import pytest, time
from playwright.sync_api import Page
from pages.main_page import MainPage, MainPageElms
from pages.context_menu_page import ContextMenuPage, ContextMenuPageElms

# Открывает страницу
def test_context_menu_page_open(page: Page):
    # объекты класса
    elms = MainPageElms()
    main_page = MainPage(page, elms)

    # Действия
    main_page.go_to() # открываем стартовую страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page.click_context_menu()# кликаем по ссылке
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    # объекты класса
    elms = ContextMenuPageElms()
    checkboxes_page = ContextMenuPage(page, elms)

    '''
    checkboxes_page.url_check()  # вызываем проверку урла
    checkboxes_page.header_and_checkboxes_visible()# вызываем проверку видимости
    '''
    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_text_upper = page.locator(elms.PAGE_TEXT_UPPER)
    page_text_lower = page.locator(elms.PAGE_TEXT_LOWER)

    # проверки
    assert "/context_menu" in page.url
    assert page_header.is_visible()
    assert page_text_upper.count() == 1
    assert page_text_lower.count() == 1
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