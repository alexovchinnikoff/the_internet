# tests/ui/test_open_add_remove_elms_page.py

import pytest
from playwright.sync_api import Page, expect
import time
from pages.main_page import MainPage
from pages.add_remove_elms_page import AddRemoveElmsPage

# Открывает страницу
def test_open_add_remove_elements_page(page: Page):
    # Инициализируем классы
    main_page_object = MainPage(page)
    add_remove_elms_page_object = AddRemoveElmsPage(page)

    # Действия и проверки
    main_page_object.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page_object.links_visible()# вызываем проверку видимости
    main_page_object.links_enabled()# вызываем проверку видимости

    main_page_object.click_addremoveelms()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    add_remove_elms_page_object.page_header_visible()# вызываем проверку видимости
    add_remove_elms_page_object.add_button_visible()# вызываем проверку видимости
    add_remove_elms_page_object.no_delete_buttons()# вызываем проверку количества

    add_remove_elms_page_object.click_add_button()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    add_remove_elms_page_object.page_header_visible()# вызываем проверку видимости
    add_remove_elms_page_object.add_button_visible()# вызываем проверку видимости
    add_remove_elms_page_object.one_add_button()# вызываем проверку количества
    add_remove_elms_page_object.one_delete_buttons()# вызываем проверку количества

    add_remove_elms_page_object.click_add_button()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    add_remove_elms_page_object.page_header_visible()# вызываем проверку видимости
    add_remove_elms_page_object.add_button_visible()# вызываем проверку видимости
    add_remove_elms_page_object.one_add_button()# вызываем проверку количества
    add_remove_elms_page_object.two_delete_buttons()# вызываем проверку количества

    add_remove_elms_page_object.click_second_delete()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    add_remove_elms_page_object.page_header_visible()# вызываем проверку видимости
    add_remove_elms_page_object.add_button_visible()# вызываем проверку видимости
    add_remove_elms_page_object.one_add_button()
    add_remove_elms_page_object.one_delete_buttons()

    add_remove_elms_page_object.click_first_delete()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # 1500 миллисекунд = 1,5 секунды
    add_remove_elms_page_object.page_header_visible()# вызываем проверку видимости
    add_remove_elms_page_object.add_button_visible()# вызываем проверку видимости
    add_remove_elms_page_object.one_add_button()# вызываем проверку количества
    add_remove_elms_page_object.no_delete_buttons()# вызываем проверку количества

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_header = add_remove_elms_page_object.page_header.inner_text()
    add_button_number = add_remove_elms_page_object.add_button.count()
    delete_buttons_number = add_remove_elms_page_object.delete_buttons.count()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {page_header}")
    print(f"📄 Видна кнопка Add Button в количестве: {add_button_number}")
    print(f"📄 Видна кнопка Delete в количестве: {delete_buttons_number}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/add_remove_elms_screenshot.png")
    print("📸 Скриншот сохранен как 'add_remove_elms_screenshot.png'")