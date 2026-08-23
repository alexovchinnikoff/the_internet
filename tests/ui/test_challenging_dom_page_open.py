# tests/ui/test_challenging_dom_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.chal_dom_page import ChalDomPage, ChalDomPageElms

def test_chal_dom_page_open(page: Page):
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
    assert elms.page_text.is_visible()

    assert elms.button_upper.is_visible()
    assert elms.button_middle.is_visible()
    assert elms.button_lower.is_visible()
    assert elms.buttons.count() == 3

    assert elms.table.is_visible()
    assert elms.table.count() == 1
    assert elms.thead.count() == 1
    assert elms.thead_row.count() == 1
    assert elms.thead_headers.count() == 7
    '''
    count = elms.thead_headers.count()
    for i in range(count):
            header = elms.thead_headers.nth(i)
            assert header.is_visible()
    '''
    assert elms.thead_header_0.is_visible()
    assert elms.thead_header_1.is_visible()
    assert elms.thead_header_2.is_visible()
    assert elms.thead_header_3.is_visible()
    assert elms.thead_header_4.is_visible()
    assert elms.thead_header_5.is_visible()
    assert elms.thead_header_6.is_visible()

    assert elms.table_body.count() == 1
    assert elms.table_body_rows.count() == 10
    assert elms.table_body_headers.count() == 70

    assert elms.href_edit.count() == 10
    assert elms.href_delete.count() == 10

    assert elms.page_canvas.is_visible()
    assert elms.page_canvas.count() == 1


    # page_title = page.title()
    current_url = page.url  # Текущий URL
    page_header = chal_dom_page.elms.page_header.inner_text()
    page_text = chal_dom_page.elms.page_text.inner_text()
    buttons_number = elms.buttons.count()
    rows_number = elms.table_body_rows.count()
    table_number = elms.table.count()
    head_number = elms.thead.count()
    colomns = elms.thead_headers.count()

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден заголовок страницы: {page_header}")
    print(f"📄 Видны {buttons_number} ссылки стилизованные под кнопки")
    print(f"📄 Видна {table_number}  таблица с {head_number} шапкой и {rows_number} рядами, {colomns} столбцами")

    print("⏳ Ожидание 1,5 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_challenging_dom_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_challenging_dom_page_screenshot.png'")