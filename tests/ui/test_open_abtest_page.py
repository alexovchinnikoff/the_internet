# tests/ui/test_open_abtest_page.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.abtest_page import ABTestPage, ABTestPageElms

# Открывает страницу
def test_abtest_page_open(page: Page):
    # объекты класса
    elms = MainPageElms(page)
    main_page = MainPage(page, elms)

    # Действия
    main_page.go_to() # открываем стартовую страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page.click_abtest()# кликаем по ссылке
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    # объекты класса
    elms = ABTestPageElms(page)
    abtest_page = ABTestPage(page, elms)

    '''
    abtest_page.url_check()  # вызываем проверку урла
    abtest_page.header_and_text_visible()# вызываем проверку видимости
    '''

    assert "/abtest" in page.url
    assert elms.page_header.is_visible() # на странице заголовок (А/В Test) постоянный, а дальше могут добавляться окончания. сделал не строгую проверку, чтоб тест не падал

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы
    header_text = elms.page_header.inner_text()
    text = elms.page_text.inner_text()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {header_text}")
    print(f"📄 Виден текст: {text}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_abtest_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_abtest_page_screenshot.png'")