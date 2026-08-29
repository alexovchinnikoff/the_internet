# tests/ui/test_basic_auth_page_open.py

import pytest, time
from playwright.sync_api import Page
from pages.main_page import MainPage, MainPageElms
from pages.basic_auth_page import BasicAuthPage, BasicAuthPageElms

def test_basic_auth_page_open(page: Page):
    # Инициализируем классы
    elms = MainPageElms()
    main_page = MainPage(page, elms)

    # Действия и проверки
    main_page.go_to()  # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    elms = BasicAuthPageElms()
    basic_auth_page = BasicAuthPage(page,elms)

    basic_auth_page.go_to()# Открывает страницу по ссылке
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    '''
    basic_auth_page.header_and_text_visible()# вызываем проверку видимости
    basic_auth_page.url_check()  # вызываем проверку урла
    '''

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