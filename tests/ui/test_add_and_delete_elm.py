# tests/ui/test_add_and_delete_elm.py

from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.add_remove_page import AddRemovePage, AddRemovePageElms

# Открывает страницу
def test_add_and_delete_elm(page: Page):
    # Инициализируем классы
    user = User(page)

    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)
    user.click_element(MainPageElms.LINK_ADDREMOVEELMS)
    user.wait_sec(1)

    elms = AddRemovePageElms()

    user.click_element(elms.ADD_BUTTON)
    user.wait_sec(1)

    user.click_element(elms.DELETE_BUTTONS)
    user.wait_sec(1)
    # локаторы к переменные
    header_locator = page.locator(elms.PAGE_HEADER)
    add_button_locator = page.locator(elms.ADD_BUTTON)
    delete_buttons_locator = page.locator(elms.DELETE_BUTTONS)

    # проверки
    user.make_screenshot("check_add_and_delete_elm")
    assert "/add_remove_elements" in page.url, "Урл корректный"# сделал не строгую проверку. в отличие от остальных страниц, здесь урл со слэшем в конце /add_remove_element/
    assert header_locator.is_visible(), "Заголовок виден"
    assert add_button_locator.is_visible(), "Кнопка видна"
    assert add_button_locator.count() == 1, "Количество кнопок корректное"
    assert delete_buttons_locator.count() == 0, "Количество кнопок корректное"

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
