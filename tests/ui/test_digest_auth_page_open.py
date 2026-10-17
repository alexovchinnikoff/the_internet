# tests/ui/test_digest_auth_page_open.py
import pytest
import allure
from playwright.sync_api import Page
from base.user_client import User
from pages.digest_auth_page import DigestAuthPage, DigestAuthPageElms


@pytest.mark.usefixtures("context")
@pytest.mark.parametrize("context", [{"username": "admin", "password": "admin"}], indirect=True)
@allure.feature("Авторизация и безопасность")
@allure.story("Проверка доступа к защищенным страницам")
@allure.title("Тест: Доступ к странице Digest Auth")
@allure.description("Проверяет доступ к странице, защищенной HTTP Digest Auth. Включает увеличенный таймаут для пробуждения сервера Heroku.")
@allure.severity(allure.severity_level.CRITICAL)

def test_basic_auth_page_open(page: Page):
    user = User(page)
    elms = DigestAuthPageElms()
    base_url = DigestAuthPage.url

    with allure.step("1. Переход на страницу (авторизация применяется автоматически)"):
        # ВАЖНО: Таймаут увеличен до 90000 мс (90 секунд).
        # Сервер на бесплатном Heroku засыпает и просыпается до 60-70 секунд.
        # Стандартный таймаут (30 сек) слишком мал.
        page.goto(base_url, wait_until="domcontentloaded", timeout=90000)
        user.wait_sec(1)

    with allure.step("2. Валидация контента страницы"):
        page_header = page.locator(elms.PAGE_HEADER)
        page_text = page.locator(elms.PAGE_TEXT)

        assert "/digest_auth" in page.url, f"Неверный URL страницы. Ожидался /digest_auth, но получен {page.url}"
        assert page_header.is_visible(), "Заголовок страницы не виден"
        assert page_text.is_visible(), "Текст страницы не виден"

    with allure.step("3. Сохранение скриншота и детализация"):
        screenshot_path = "D:/Projects/the_internet/prtscr/open_digest_auth_page_screenshot.png"
        page.screenshot(path=screenshot_path)

        allure.attach.file(screenshot_path, name="digest_auth_screenshot", attachment_type=allure.attachment_type.PNG)

        allure.attach(
            f"URL: {page.url}\n"
            f"Заголовок: {page_header.inner_text()}\n"
            f"Текст: {page_text.inner_text()}",
            name="Детали страницы",
            attachment_type=allure.attachment_type.TEXT
        )