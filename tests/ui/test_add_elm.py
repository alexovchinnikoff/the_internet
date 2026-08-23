# tests/ui/test_add_elm.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.add_remove_page import AddRemovePage, AddRemovePageElms

def test_add_elm(page: Page):
    # Инициализируем классы
    elms = MainPageElms(page)
    main_page = MainPage(page, elms)

    # Действия и проверки
    main_page.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    main_page.click_addremoveelms() # вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    elms = AddRemovePageElms(page)
    add_remove_page = AddRemovePage(page, elms)

    add_remove_page.click_add_button()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # 1500 миллисекунд = 1,5 секунды
    '''
    add_remove_page.page_header_visible()# вызываем проверку видимости
    add_remove_page.add_button_visible()# вызываем проверку видимости
    add_remove_page.one_add_button() # вызываем проверку количества
    add_remove_page.one_delete_buttons() # вызываем проверку количества
    '''
    assert "/add_remove_elements" in page.url
    assert elms.page_header.is_visible()
    assert elms.add_button.is_visible()
    assert elms.add_button.count() == 1
    assert elms.delete_buttons.is_visible()
    assert elms.delete_buttons.count() == 1

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_header = add_remove_page.elms.page_header.inner_text()
    add_button_number = add_remove_page.elms.add_button.count()
    delete_buttons_number = add_remove_page.elms.delete_buttons.count()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {page_header}")
    print(f"📄 Видна кнопка Add Button в количестве: {add_button_number}")
    print(f"📄 Видна кнопка Delete в количестве: {delete_buttons_number}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/add_elm_screenshot.png")
    print("📸 Скриншот сохранен как 'add_elm_screenshot.png'")

   