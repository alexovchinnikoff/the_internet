# tests/ui/test_basic_auth_page_open.py
import pytest
import allure
from playwright.sync_api import Page
from base.user_client import User
from pages.basic_auth_page import BasicAuthPage, BasicAuthPageElms


# Эти два декоратора говорят pytest:
# 1. Используй фикстуру 'context' (она настроена на HTTP Auth).
# 2. Передай в неё логин/пароль: admin/admin.
@pytest.mark.usefixtures("context")
@pytest.mark.parametrize("context", [{"username": "admin", "password": "admin"}], indirect=True)
@allure.feature("Авторизация и безопасность")
@allure.story("Проверка доступа к защищенным страницам")
@allure.title("Тест: Доступ к странице Basic Auth")
@allure.description(
    "Проверяет доступ к странице, защищенной HTTP Basic Auth, используя автоматическую авторизацию в контексте браузера и увеличенный таймаут.")
@allure.severity(allure.severity_level.CRITICAL)
def test_basic_auth_page_open(page: Page):
    user = User(page)
    elms = BasicAuthPageElms()
    base_url = BasicAuthPage.url

    with allure.step("1. Переход на страницу Basic Auth (авторизация применяется автоматически)"):
        page.goto(base_url, wait_until="domcontentloaded", timeout=90000)
        user.wait_sec(1)

    with allure.step("2. Валидация контента страницы"):
        page_header = page.locator(elms.PAGE_HEADER)
        page_text = page.locator(elms.PAGE_TEXT)

        assert "/basic_auth" in page.url, f"Неверный URL страницы. Ожидался /basic_auth, но получен {page.url}"
        assert page_header.is_visible(), "Заголовок страницы не виден"
        assert page_text.is_visible(), "Текст страницы не виден"

    with allure.step("3. Фиксация результата (Скриншот и детали)"):
        screenshot_path = "D:/Projects/the_internet/prtscr/open_basic_auth_page_screenshot.png"
        page.screenshot(path=screenshot_path)

        # Прикрепляем скриншот к отчету Allure
        allure.attach.file(screenshot_path, name="basic_auth_screenshot", attachment_type=allure.attachment_type.PNG)

        # Прикрепляем текстовую информацию вместо print()
        allure.attach(
            f"URL: {page.url}\n"
            f"Заголовок: {page_header.inner_text()}\n"
            f"Текст: {page_text.inner_text()}",
            name="Детали страницы",
            attachment_type=allure.attachment_type.TEXT
        )