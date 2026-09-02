# tests/ui/test_abtest_page_open.py

from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.abtest_page import ABTestPageElms

# Открывает страницу
def test_abtest_page_open(page: Page):
    # объекты класса
    user = User(page)

    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)  # ждем 1500 миллисекунд = 1,5 секунды
    user.click_element(MainPageElms.LINK_ABTEST)
    user.wait_sec(1)  # ждем 1500 миллисекунд = 1,5 секунды

    # объекты класса
    elms = ABTestPageElms()

    # локаторы к переменные
    header_locator = page.locator(elms.PAGE_HEADER)
    text_locator = page.locator(elms.PAGE_TEXT)

    '''
    abtest_page.url_check()  # вызываем проверку урла
    abtest_page.header_and_text_visible()# вызываем проверку видимости
    '''

    # проверки
    assert "/abtest" in page.url, "Урл корректный"
    assert header_locator.is_visible(), "Заголовок виден"
    assert text_locator.is_visible(), "Текст виден"

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url }")
    print(f"📄 Виден заголовок страницы: {header_locator.inner_text()}")
    print(f"📄 Виден текст: {text_locator.inner_text()}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_abtest_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_abtest_page_screenshot.png'")