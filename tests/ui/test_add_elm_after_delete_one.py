# tests/ui/test_add_elm_after_delete_one.py

import pytest, time
from playwright.sync_api import Page
from pages.main_page import MainPage, MainPageElms
from pages.add_remove_page import AddRemovePage, AddRemovePageElms

# Открывает страницу
def test_add_elm_after_delete_one(page: Page):
    # Инициализируем классы
    elms = MainPageElms()
    main_page = MainPage(page, elms)

    # Действия и проверки
    main_page.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    main_page.click_addremoveelms()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    elms = AddRemovePageElms()
    add_remove_page = AddRemovePage(page, elms)

    add_remove_page.click_add_button()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    add_remove_page.click_first_delete()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    add_remove_page.click_add_button()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    '''
    add_remove_page.one_add_button()# вызываем проверку количества
    add_remove_page.one_delete_buttons()# вызываем проверку количества
    '''

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    add_button = page.locator(elms.ADD_BUTTON)
    delete_buttons = page.locator(elms.DELETE_BUTTONS)

    # проверки
    assert "/add_remove_elements" in page.url
    assert page_header.is_visible()
    assert add_button.is_visible()
    assert add_button.count() == 1
    assert delete_buttons.is_visible()
    assert delete_buttons.count() == 1

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Видна кнопка Add Button в количестве: {add_button.count()}")
    print(f"📄 Видна кнопка Delete в количестве: {delete_buttons.count()}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/add_elm_after_delete_one_screenshot.png")
    print("📸 Скриншот сохранен как 'add_elm_after_delete_one_screenshot.png'")
