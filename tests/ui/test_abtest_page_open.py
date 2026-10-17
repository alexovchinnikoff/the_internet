# tests/ui/test_abtest_page_open.py
import allure
from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.abtest_page import ABTestPageElms


@allure.feature("Навигация и переходы")
@allure.story("Проверка перехода на страницу A/B теста")
@allure.title("Тест: Открытие страницы A/B теста и валидация контента")
@allure.description("Проверяет, что пользователь может перейти на страницу A/B теста, страница загружается корректно, и на ней присутствует ожидаемый контент.")
@allure.severity(allure.severity_level.CRITICAL)
def test_abtest_page_open(page: Page):
    # Инициализация объекта User
    user = User(page)

    with allure.step("1. Открытие главной страницы"):
        user.open_page(MainPage.url)

    with allure.step("2. Переход на страницу A/B теста"):
        user.click_element(MainPageElms.LINK_ABTEST)
        # Небольшая пауза после клика, чтобы страница успела начать загрузку
        user.wait_sec(1)

    with allure.step("3. Локализация элементов на странице A/B теста"):
        elms = ABTestPageElms()
        header_locator = page.locator(elms.PAGE_HEADER)
        text_locator = page.locator(elms.PAGE_TEXT)

        # Явные проверки видимости (лучше, чем просто wait_sec)
        assert header_locator.is_visible(), "Заголовок страницы не виден"
        assert text_locator.is_visible(), "Текст на странице не виден"

    with allure.step("4. Валидация URL и контента"):
        assert "/abtest" in page.url, "Неверный URL: страница не перешла на /abtest"

        header_text = header_locator.inner_text()
        text_text = text_locator.inner_text()

        assert header_text, "Заголовок страницы пустой"
        assert text_text, "Текст страницы пустой"

    with allure.step("5. Фиксация результата (Скриншот)"):
        screenshot_path = "D:/Projects/the_internet/prtscr/open_abtest_page_screenshot.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="open_abtest_page_screenshot",
                           attachment_type=allure.attachment_type.PNG)

        # Вывод данных в отчет Allure (вместо print)
        allure.attach(
            f"URL: {page.url}\nHeader: {header_text}\nText: {text_text}",
            name="Детали страницы",
            attachment_type=allure.attachment_type.TEXT
        )