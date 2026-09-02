# tests/ui/test_broken_images_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from base.user_client import User
from pages.main_page import MainPage, MainPageElms
from pages.broken_imgs_page import BrokenImgsPage, BrokenImgsPageElms

def test_broken_imgs_page_open(page: Page):
    # Инициализируем
    user = User(page)
    # Действия
    user.open_page(MainPage.url)
    user.wait_sec(1)

    user.click_element(MainPageElms.LINK_BROKENIMGS)
    user.wait_sec(1)

    elms = BrokenImgsPageElms()

    user.click_element(elms.PAGE_IMAGES)# вызываем клик по элементу
    user.wait_sec(1)

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_images = page.locator(elms.PAGE_IMAGES)

    # проверки
    user.make_screenshot("check_broken_images_page_open")
    assert "/broken_images" in page.url, "Урл корректный"
    assert page_header.is_visible(), "Заголовок виден"
    assert page_images.is_visible(), "Картинки видны"
    assert page_images.count() == 3, "Количество картинок корректное"

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Количество картинок: {page_images.count()}")
    print("⏳ Ожидание 1,5 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_broken_images_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_broken_images_page_screenshot.png'")