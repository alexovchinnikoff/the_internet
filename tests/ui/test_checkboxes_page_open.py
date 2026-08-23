# tests/ui/test_checkboxes_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.checkboxes_page import CheckBoxesPage, CheckBoxesPageElms

# Открывает страницу
def test_checkboxes_page_open(page: Page):
    # объекты класса
    elms = MainPageElms(page)
    main_page = MainPage(page, elms)

    # Действия
    main_page.go_to() # открываем стартовую страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    main_page.click_checkboxes()# кликаем по ссылке
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    # объекты класса
    elms = CheckBoxesPageElms(page)
    checkboxes_page = CheckBoxesPage(page, elms)

    '''
    checkboxes_page.url_check()  # вызываем проверку урла
    checkboxes_page.header_and_checkboxes_visible()# вызываем проверку видимости
    '''

    assert "/checkboxes" in page.url
    assert elms.page_header.is_visible()
    assert elms.page_checkboxes.count() == 2

    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы
    header_text = elms.page_header.inner_text()
    checkboxes_number = checkboxes_page.elms.page_checkboxes.count()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {header_text}")
    print(f"📄 Виден текст: {checkboxes_number}")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_checkboxes_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_checkboxes_page_screenshot.png'")