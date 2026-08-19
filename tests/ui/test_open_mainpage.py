# pages/test_open_mainpage_2.py

import pytest
from playwright.sync_api import Page, expect
import time
from pages.main_page import MainPage

def test_mainpage_open(page: Page):
    # Инициализируем классы
    main_page_object = MainPage(page)
    # Действия и проверки
    main_page_object.go_to()  # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page_object.url_check()  # вызываем проверку урла
    main_page_object.headers_visible() # вызываем проверку видимости
    main_page_object.links_visible() # вызываем проверку видимости
    main_page_object.links_enabled()# вызываем проверку активности
    main_page_object.links_count(44) # вызываем проверку количества
    links_number = main_page_object.links.count() # передаем реальное количество для вывода

    # page_title = page.title()
    current_url = page.url
    welcome_text = main_page_object.welcome_header.inner_text()
    second_text = main_page_object.second_header.inner_text()

    # Вывод результатов в консоль
    print(f"\n✅ Стартовая страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден приветственный заголовок: {welcome_text}")
    print(f"📄 Виден второй заголовок: {second_text}")
    print(f"📄 В списке найдено {links_number} ссылок (пунктов меню).")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/main_page_screenshot.png")
    print("📸 Скриншот сохранен как 'main_page_screenshot.png'")