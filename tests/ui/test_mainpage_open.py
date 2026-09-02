# pages/test_main_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from base.user_client import User
from pages.main_page import MainPage, MainPageElms

def test_main_page_open(page: Page):
    user = User(page)
    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    elms = MainPageElms()

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
    user.make_screenshot("check_main_page_open")
    assert page.url == "https://the-internet.herokuapp.com/", "Урл корректный"
    assert welcome_header.is_visible(), "Заголовок 1 виден"
    assert second_header.is_visible(), "Заголовок 2 виден"

    assert link_addremoveelms.is_visible(), "Ссылка видна"
    assert link_basicauth.is_visible(), "Ссылка видна"
    assert link_brokenimgs.is_visible(), "Ссылка видна"
    assert link_chaldom.is_visible(), "Ссылка видна"
    assert link_checkboxes.is_visible(), "Ссылка видна"
    assert link_contextmenu.is_visible(), "Ссылка видна"
    assert links.count() == 44, "Количество ссылок корректное"

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