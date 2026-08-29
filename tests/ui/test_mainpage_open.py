# pages/test_main_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms

def test_main_page_open(page: Page):
    elms = MainPageElms() # со скобками обращаемся к объекту, без скобок - просто к классу
    main_page = MainPage(page,elms)
    # Действия и проверки
    main_page.go_to()  # переход на стартовую страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды
    '''
    main_page.url_check()  # проверяем урл
    main_page.headers_visible() # проверяем заголовки
    main_page.links_visible() # проверяем видимость ссылок
    #main_page.links_enabled()# НЕ проверяем активность ссылок
    main_page.links_count(44) # проверяем количество ссылок
    '''
    # локаторы к переменные
    welcome_header = page.locator(elms.WELCOME_HEADER)
    second_header = page.locator(elms.SECOND_HEADER)
    links = page.locator(elms.LINKS)
    link_abtest = page.locator(elms.LINK_ABTEST)
    link_addremoveelms = page.locator(elms. LINK_ADDREMOVEELMS)
    link_basicauth = page.locator(elms.LINK_BASICAUTH)
    link_brokenimgs = page.locator(elms.LINK_BROKENIMGS)
    link_chaldom = page.locator(elms.LINK_CHALDOM)
    link_checkboxes = page.locator(elms.LINK_CHECKBOXES)
    link_contextmenu = page.locator(elms.LINK_CONTEXTMENU)

    # проверки

    # урл проверяем ассертом можно так:
    assert page.url == "https://the-internet.herokuapp.com/"

    assert welcome_header.is_visible()
    assert second_header.is_visible()
    assert link_abtest.is_visible()
    assert link_addremoveelms.is_visible()
    assert link_basicauth.is_visible()
    assert link_brokenimgs.is_visible()
    assert link_chaldom.is_visible()
    assert link_checkboxes.is_visible()
    assert link_contextmenu.is_visible()
    assert links.count() == 44

    # Вывод результатов в консоль
    print(f"\n✅ Стартовая страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден приветственный заголовок: {welcome_header.inner_text()}")
    print(f"📄 Виден второй заголовок: {second_header.inner_text()}")
    print(f"📄 В списке найдено {links.count()} ссылок (пунктов меню).")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_main_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_main_page_screenshot.png'")