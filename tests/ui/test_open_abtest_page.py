# tests/ui/test_open_abtest_page.py

import pytest
from playwright.sync_api import Page, expect
import time
from pages.main_page import MainPage
from pages.abtest_page import ABTestPage

# Открывает страницу
def test_abtest_page_open(page: Page):
    # Инициализируем классы
    main_page_object = MainPage(page)
    abtest_page_object = ABTestPage(page)
    # Действия и проверки
    main_page_object.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page_object.links_visible()# вызываем проверку видимости
    main_page_object.links_enabled()# вызываем проверку активности

    main_page_object.click_abtest()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    abtest_page_object.url_check()  # вызываем проверку урла
    abtest_page_object.header_and_text_visible()# вызываем проверку видимости

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы
    header_text = abtest_page_object.page_header.inner_text()
    text = abtest_page_object.page_text.inner_text()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {header_text}")
    print(f"📄 Виден текст: {text}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/abtest_page_screenshot.png")
    print("📸 Скриншот сохранен как 'abtest_page_screenshot.png'")