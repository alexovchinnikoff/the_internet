# tests/ui/test_add_and_delete_elm.py

import pytest, time
from playwright.sync_api import Page
from pages.main_page import MainPage, MainPageElms
from pages.add_remove_page import AddRemovePage, AddRemovePageElms

# Открывает страницу
def test_add_and_delete_elm(page: Page):
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

    '''
    add_remove_page.page_header_visible()# вызываем проверку видимости
    add_remove_page.add_button_visible()# вызываем проверку видимости
    add_remove_page.one_add_button()# вызываем проверку количества
    add_remove_page.no_delete_buttons()# вызываем проверку количества
    '''

    # локаторы к переменные
    header_locator = page.locator(elms.PAGE_HEADER)
    add_button_locator = page.locator(elms.ADD_BUTTON)
    delete_buttons_locator = page.locator(elms.DELETE_BUTTONS)

    # проверки
    assert "/add_remove_elements" in page.url
    assert header_locator.is_visible()
    assert add_button_locator.is_visible()
    assert add_button_locator.count() == 1
    assert delete_buttons_locator.count() == 0

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url }")
    print(f"📄 Виден заголовок страницы: {header_locator.inner_text()}")
    print(f"📄 Видна кнопка Add Button в количестве: {add_button_locator.count()}")
    print(f"📄 Видна кнопка Delete в количестве: {delete_buttons_locator.count()}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/delete_elm_screenshot.png")
    print("📸 Скриншот сохранен как 'delete_elm_screenshot.png'")
