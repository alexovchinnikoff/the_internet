# tests/ui/test_add_elm.py

from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.add_remove_page import AddRemovePage, AddRemovePageElms

def test_add_elm(page: Page):
    # Инициализируем класс
    user = User(page)
    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    user.click_element(MainPageElms.LINK_ADDREMOVEELMS)
    user.wait_sec(1)

    elms = AddRemovePageElms()

    user.click_element(elms.ADD_BUTTON)
    user.wait_sec(1)
    # локаторы в переменные
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
    page.screenshot(path="D:/Projects/the_internet/prtscr/add_elm_screenshot.png")
    print("📸 Скриншот сохранен как 'add_elm_screenshot.png'")

   