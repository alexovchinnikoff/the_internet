# tests/ui/test_open_challenging_dom_page.py

import pytest
from playwright.sync_api import Page, expect
import time
from pages.main_page import MainPage
from pages.chal_dom_page import ChalDomPage

def test_open_chal_dom_page(page: Page):
    # Инициализируем классы
    main_page_object = MainPage(page)
    # Действия и проверки
    main_page_object.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page_object.links_visible()# вызываем проверку видимости
    main_page_object.links_enabled()# вызываем проверку активности

    main_page_object.click_chaldom()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    chal_dom_page_object = ChalDomPage(page)# Инициализируем класс
    chal_dom_page_object.page_header_visible()# вызываем проверку видимости
    chal_dom_page_object.url_check()  # вызываем проверку урла

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_header = chal_dom_page_object.page_header.inner_text()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {page_header}")

    print("⏳ Ожидание 1,5 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/chal_dom_screenshot.png")
    print("📸 Скриншот сохранен как 'chal_dom_screenshot.png'")