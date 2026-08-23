# tests/ui/test_checkboxes_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.context_menu_page import ContextMenuPage, ContextMenuPageElms

# Открывает страницу
def test_context_menu_page_open(page: Page):
    # объекты класса
    elms = MainPageElms(page)
    main_page = MainPage(page, elms)

    # Действия
    main_page.go_to() # открываем стартовую страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page.click_context_menu()# кликаем по ссылке
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    # объекты класса
    elms = ContextMenuPageElms(page)
    checkboxes_page = ContextMenuPage(page, elms)

    '''
    checkboxes_page.url_check()  # вызываем проверку урла
    checkboxes_page.header_and_checkboxes_visible()# вызываем проверку видимости
    '''

    assert "/context_menu" in page.url
    assert elms.page_header.is_visible()
    assert elms.page_text_upper.count() == 1
    assert elms.page_text_lower.count() == 1
    # assert page.right_click_page_box() == <script> function displayMessage() {window.alert('You selected a context menu')} </script>

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы
    header_text = elms.page_header.inner_text()
    text_upper = elms.page_text_upper.inner_text()
    text_lower = elms.page_text_lower.inner_text()
    page_box_number = elms.page_box.count()


    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {header_text}")
    print(f"📄 Виден заголовок страницы: {text_upper}")
    print(f"📄 Виден заголовок страницы: {text_lower}")
    print(f"📄 Виден текст: {page_box_number}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_checkboxes_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_checkboxes_page_screenshot.png'")