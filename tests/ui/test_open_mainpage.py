# pages/test_open_main_page.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms

def test_main_page_open(page: Page):
    elms = MainPageElms(page) # со скобками обращаемся к объекту, без скобок - просто к классу
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
    # урл проверяем ассертом можно так:
    assert page.url == "https://the-internet.herokuapp.com/"

    assert elms.welcome_header.is_visible()
    assert elms.second_header.is_visible()
    assert elms.link_abtest.is_visible()
    assert elms.link_addremoveelms.is_visible()
    assert elms.link_basicauth.is_visible()
    assert elms.link_brokenimgs.is_visible()
    assert elms.link_chaldom.is_visible()

    assert main_page.elms.links.count() == 44

    # Переменные для вывода результатов
    # page_title = page.title()
    current_url = page.url
    welcome_text = main_page.elms.welcome_header.inner_text()
    second_text = main_page.elms.second_header.inner_text()
    links_number = main_page.elms.links.count()
    # Вывод результатов в консоль
    print(f"\n✅ Стартовая страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Виден приветственный заголовок: {welcome_text}")
    print(f"📄 Виден второй заголовок: {second_text}")
    print(f"📄 В списке найдено {links_number} ссылок (пунктов меню).")
    print("⏳ Ожидание 1,5 секунды...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_main_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_main_page_screenshot.png'")