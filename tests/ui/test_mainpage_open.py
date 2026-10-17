# tests/ui/test_main_page_open.py
import pytest
import allure
from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms


@allure.feature("Навигация и структура")
@allure.story("Проверка главной страницы")
@allure.title("Тест: Открытие и валидация главной страницы")
@allure.description(
    "Проверяет загрузку главной страницы, наличие ключевых заголовков, ссылок и соответствие количества элементов ожидаемому.")
@allure.severity(allure.severity_level.CRITICAL)
def test_main_page_open(page: Page):
    user = User(page)
    elms = MainPageElms()
    base_url = MainPage.url

    with allure.step("1. Переход на главную страницу"):
        user.open_page(MainPage.url)

    with allure.step("2. Проверка URL и основных заголовков"):
        assert page.url == "https://the-internet.herokuapp.com/", f"Неверный URL страницы. Ожидался {base_url}, но получен {page.url}"

        welcome_header = page.locator(elms.WELCOME_HEADER)
        second_header = page.locator(elms.SECOND_HEADER)

        assert welcome_header.is_visible(), "Приветственный заголовок не виден"
        assert second_header.is_visible(), "Второй заголовок не виден"

    with allure.step("3. Валидация наличия ссылок и их количества"):
        links = page.locator(elms.LINKS)

        # Проверяем видимость конкретных важных ссылок
        assert page.locator(elms.LINK_ABTEST).is_visible(), "Ссылка A/B Test не видна"
        assert page.locator(elms.LINK_ADDREMOVEELMS).is_visible(), "Ссылка Add/Remove Elements не видна"
        assert page.locator(elms.LINK_BASICAUTH).is_visible(), "Ссылка Basic Auth не видна"
        assert page.locator(elms.LINK_BROKENIMGS).is_visible(), "Ссылка Broken Images не видна"
        assert page.locator(elms.LINK_CHALDOM).is_visible(), "Ссылка Chaldom не видна"
        assert page.locator(elms.LINK_CHECKBOXES).is_visible(), "Ссылка Checkboxes не видна"
        assert page.locator(elms.LINK_CONTEXTMENU).is_visible(), "Ссылка Context Menu не видна"

        # Проверка общего количества ссылок (согласно твоему тесту - 44)
        assert links.count() == 44, f"Количество ссылок не соответствует ожидаемому (44). Найдено: {links.count()}"

    with allure.step("4. Фиксация результата (Скриншот и детали)"):
        screenshot_path = "D:/Projects/the_internet/prtscr/open_main_page_screenshot.png"
        page.screenshot(path=screenshot_path)

        # Прикрепляем скриншот к отчету Allure
        allure.attach.file(screenshot_path, name="main_page_screenshot", attachment_type=allure.attachment_type.PNG)

        # Прикрепляем текстовую информацию вместо print()
        allure.attach(
            f"URL: {page.url}\n"
            f"Заголовок 1: {welcome_header.inner_text()}\n"
            f"Заголовок 2: {second_header.inner_text()}\n"
            f"Количество ссылок: {links.count()}",
            name="Детали страницы",
            attachment_type=allure.attachment_type.TEXT
        )