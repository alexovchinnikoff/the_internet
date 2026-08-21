# tests/ui/test_open_challenging_dom_page.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.chal_dom_page import ChalDomPage, ChalDomPageElms

def test_open_chal_dom_page(page: Page):
    # Инициализируем классы
    elms = MainPageElms(page)
    main_page = MainPage(page, elms)

    # Действия и проверки
    main_page.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    main_page.click_chaldom()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    elms = ChalDomPageElms(page)
    chal_dom_page = ChalDomPage(page, elms)
    '''
    chal_dom_page.page_header_visible()# вызываем проверку видимости
    chal_dom_page.url_check()  # вызываем проверку урла
    '''

    assert "/challenging_dom" in page.url
    assert elms.page_header.is_visible()

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_header = chal_dom_page.elms.page_header.inner_text()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {page_header}")

    print("⏳ Ожидание 1,5 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_challenging_dom_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_challenging_dom_page_screenshot.png'")