# tests/ui/test_checkboxes_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.checkboxes_page import CheckBoxesPage, CheckBoxesPageElms

# Открывает страницу
def test_checkboxes_page_open(page: Page):
    # объекты класса
    elms = MainPageElms()
    main_page = MainPage(page, elms)

    # Действия
    main_page.go_to() # открываем стартовую страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page.click_checkboxes()# кликаем по ссылке
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    # объекты класса
    elms = CheckBoxesPageElms()
    checkboxes_page = CheckBoxesPage(page, elms)

    '''
    checkboxes_page.url_check()  # вызываем проверку урла
    checkboxes_page.header_and_checkboxes_visible()# вызываем проверку видимости
    '''
    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_checkboxes = page.locator(elms.PAGE_CHECKBOXES)

    # проверки
    assert "/checkboxes" in page.url
    assert page_header.is_visible()
    assert page_checkboxes.count() == 2

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Виден текст: {page_checkboxes.count()}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_checkboxes_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_checkboxes_page_screenshot.png'")