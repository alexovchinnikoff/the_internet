# tests/ui/test_open_basic_auth_page.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.basic_auth_page import BasicAuthPage, BasicAuthPageElms

def test_basic_auth_page_open(page: Page):
    # Инициализируем классы
    elms = MainPageElms(page)
    main_page = MainPage(page, elms)

    # Действия и проверки
    main_page.go_to()  # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    elms = BasicAuthPageElms(page)
    basic_auth_page = BasicAuthPage(page,elms)

    basic_auth_page.go_to()# Открывает страницу по ссылке
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    basic_auth_page.header_and_text_visible()# вызываем проверку видимости
    basic_auth_page.url_check()  # вызываем проверку урла

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    header_text = basic_auth_page.elms.page_header.inner_text()
    text = basic_auth_page.elms.page_text.inner_text()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {header_text}")
    print(f"📄 Виден текст: {text}")
    print("⏳ Ожидание 3 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_basic_auth_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_basic_auth_page_screenshot.png'")