# tests/ui/test_challenging_dom_page_open.py

import pytest, time
from playwright.sync_api import Page
from pages.main_page import MainPage, MainPageElms
from pages.chal_dom_page import ChalDomPage, ChalDomPageElms

def test_chal_dom_page_open(page: Page):
    # Инициализируем классы
    elms = MainPageElms()
    main_page = MainPage(page, elms)

    # Действия и проверки
    main_page.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    main_page.click_chaldom()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    elms = ChalDomPageElms()
    chal_dom_page = ChalDomPage(page, elms)
    '''
    chal_dom_page.page_header_visible()# вызываем проверку видимости
    chal_dom_page.url_check()  # вызываем проверку урла
    '''
    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_text = page.locator(elms.PAGE_TEXT)
    button_upper = page.locator(elms.BUTTON_UPPER)
    button_middle = page.locator(elms.BUTTON_MIDDLE)
    button_lower = page.locator(elms.BUTTON_LOWER)
    buttons = page.locator(elms.BUTTONS)
    table = page.locator(elms.TABLE)
    thead = page.locator(elms.THEAD)
    thead_row = page.locator(elms.THEAD_ROW)
    thead_headers = page.locator(elms.THEAD_HEADERS)
    header_0 =  page.locator(elms.LOREM)
    header_1 = page.locator(elms.IPSUM)
    header_2 = page.locator(elms.DOLOR)
    header_3 = page.locator(elms.SIT)
    header_4 = page.locator(elms.AMET)
    header_5 = page.locator(elms.DICERET)
    header_6 = page.locator(elms.ACTION)
    table_body = page.locator(elms.TABLE_BODY)
    table_body_rows = page.locator(elms.TABLE_BODY_ROWS)
    table_body_headers = page.locator(elms.TABLE_BODY_HEADERS)
    href_edit = page.locator(elms.HREF_EDIT)
    href_delete = page.locator(elms.HREF_DELETE)
    page_canvas = page.locator(elms.PAGE_CANVAS)


    # проверки
    assert "/challenging_dom" in page.url
    assert page_header.is_visible()
    assert page_text.is_visible()

    assert button_upper.is_visible()
    assert button_middle.is_visible()
    assert button_lower.is_visible()
    assert buttons.count() == 3

    assert table.is_visible()
    assert table.count() == 1
    assert thead.count() == 1
    assert thead_row.count() == 1
    assert thead_headers.count() == 7

    assert thead_headers.count() == 7
    assert table_body.count() == 1
    assert table_body_rows.count() == 10
    assert table_body_headers.count() == 70

    assert href_edit.count() == 10
    assert href_delete.count() == 10

    assert page_canvas.is_visible()
    assert page_canvas.count() == 1

    assert header_0.is_visible()
    assert header_1.is_visible()
    assert header_2.is_visible()
    assert header_3.is_visible()
    assert header_4.is_visible()
    assert header_5.is_visible()
    assert header_6.is_visible()
    '''
    count = elms.thead_headers.count()
    for i in range(count):
            header = elms.thead_headers.nth(i)
            assert header.is_visible()
    '''


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