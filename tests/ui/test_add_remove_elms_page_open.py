# tests/ui/test_add_remove_elms_page_open.py

import pytest, time
from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.add_remove_page import AddRemovePage, AddRemovePageElms

# Открывает страницу и ждет 3 секунды
def test_add_remove_elms_page_open(page: Page):
    # Инициализируем класс
    user = User(page)
    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    user.click_element(MainPageElms.LINK_ADDREMOVEELMS)
    user.wait_sec(1)

    elms = AddRemovePageElms()

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    add_button = page.locator(elms.ADD_BUTTON)
    delete_buttons = page.locator(elms.DELETE_BUTTONS)

    # проверки
    user.make_screenshot("check_add_remove_elms_page_open")
    assert "/add_remove_elements" in page.url, "Урл корректный" # сделал не строгую проверку. в отличие от остальных страниц, здесь урл со слэшем в конце /add_remove_element/
    assert page_header.is_visible(), "Заголовок виден"
    assert add_button.is_visible(), "Кнопка видна"
    assert add_button.count() == 1, "Количество кнопок корректное"
    assert delete_buttons.count() == 0, "Количество кнопок корректное"

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Видна кнопка Add Button в количестве: {add_button.count()}")
    print(f"📄 Видна кнопка Delete в количестве: {delete_buttons.count()}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_add_remove_elms_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_add_remove_elms_page_screenshot.png'")