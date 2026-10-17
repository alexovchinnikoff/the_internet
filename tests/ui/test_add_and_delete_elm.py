# tests/ui/test_add_and_delete_elm.py
import allure
from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.add_remove_page import AddRemovePageElms


@allure.feature("Добавление и удаление элементов")
@allure.story("Проверка функционала добавления и удаления кнопок")
@allure.title("Тест: Добавление и удаление элементов на странице Add/Remove")
@allure.description("Проверяет переход на страницу, наличие элементов, добавление кнопки и её последующее удаление.")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_and_delete_elm(page: Page):
    # Инициализация объекта User
    user = User(page)

    with allure.step("1. Переход на главную страницу и навигация"):
        user.open_page(MainPage.url)
        user.wait_sec(1)
        user.click_element(MainPageElms.LINK_ADDREMOVEELMS)
        user.wait_sec(1)

    with allure.step("2. Инициализация локаторов страницы Add/Remove"):
        elms = AddRemovePageElms()
        header_locator = page.locator(elms.PAGE_HEADER)
        add_button_locator = page.locator(elms.ADD_BUTTON)
        delete_buttons_locator = page.locator(elms.DELETE_BUTTONS)

    with allure.step("3. Проверка начального состояния страницы"):
        assert "/add_remove_elements" in page.url, "Неверный URL страницы"
        assert header_locator.is_visible(), "Заголовок страницы не виден"
        assert add_button_locator.is_visible(), "Кнопка 'Add Element' не видна"
        assert add_button_locator.count() == 1, "Количество кнопок 'Add Element' не соответствует ожидаемому (должно быть 1)"
        # На старте кнопок удаления обычно нет
        assert delete_buttons_locator.count() == 0, "На странице не должно быть кнопок удаления до клика на Add"

    with allure.step("4. Добавление элемента (кнопка Delete)"):
        user.click_element(elms.ADD_BUTTON)
        user.wait_sec(1)

        # После добавления должна появиться 1 кнопка удаления
        assert delete_buttons_locator.count() == 1, "После клика на Add должна появиться 1 кнопка удаления"

    with allure.step("5. Удаление элемента"):
        # Кликаем по появившейся кнопке удаления
        user.click_element(elms.DELETE_BUTTONS)
        user.wait_sec(1)

        # После удаления кнопок удаления снова не должно быть
        assert delete_buttons_locator.count() == 0, "После клика на Delete кнопок удаления не должно остаться"

    with allure.step("6. Фиксация результата (Скриншот)"):
        screenshot_path = "D:/Projects/the_internet/prtscr/delete_elm_screenshot.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="delete_elm_screenshot", attachment_type=allure.attachment_type.PNG)

        # Добавляем текстовую информацию в отчет вместо print
        allure.attach(
            f"URL: {page.url}\n"
            f"Заголовок: {header_locator.inner_text()}\n"
            f"Кнопок Add: {add_button_locator.count()}\n"
            f"Кнопок Delete: {delete_buttons_locator.count()}",
            name="Детали состояния",
            attachment_type=allure.attachment_type.TEXT
        )
