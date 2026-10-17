# tests/ui/test_disapp_elms_page_open.py
from playwright.sync_api import Page
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.disapp_elms_page import DisAppElmsPageElms

def test_disapp_elms_page_open(page: Page):
    # Инициализируем класс
    user = User(page)
    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    user.click_element(MainPageElms.LINK_DISAPPELMS)
    user.wait_sec(1)

    elms = DisAppElmsPageElms()

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_text = page.locator(elms.PAGE_TEXT)
    href_home = page.locator(elms.HREF_HOME)
    href_about = page.locator(elms.HREF_ABOUT)
    href_contact = page.locator(elms.HREF_CONTACT)
    href_portfolio = page.locator(elms.HREF_PORTFOLIO)
    hrefs = page.locator(elms.HREFS)

    # проверки
    user.make_screenshot("disapp_elms_page_open")
    assert "/disappearing_elements" in page.url, "Урл корректный"
    assert page_header.is_visible(), "Заголовок виден"
    assert page_text.is_visible(), "Текст виден"

    assert href_home.is_visible(), "Кнопка видна"
    assert href_about.is_visible(), "Кнопка видна"
    assert href_contact.is_visible(), "Кнопка видна"
    assert href_portfolio.is_visible(), "Кнопка видна"
    assert hrefs.count() == 4, "Количество кнопок корректное"


    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Виден текст страницы: {page_text.inner_text()}")
    print(f"📄 Видны {buttons.count()} ссылки стилизованные под кнопки")
    print(f"📄 Видна {table.count()}  таблица с {thead.count()} шапкой и {table_body_rows.count()} рядами, {thead_headers.count()} столбцами")
    print("⏳ Ожидание 1,5 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_challenging_dom_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_challenging_dom_page_screenshot.png'")