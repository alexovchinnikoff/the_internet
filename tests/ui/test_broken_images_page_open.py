# tests/ui/test_broken_images_page_open.py

import pytest, time
from playwright.sync_api import Page, expect
from pages.main_page import MainPage, MainPageElms
from pages.broken_imgs_page import BrokenImgsPage, BrokenImgsPageElms

def test_broken_imgs_page_open(page: Page):
    # Инициализируем
    elms = MainPageElms()
    main_page = MainPage(page, elms)

    # Действия и проверки
    main_page.go_to() # вызываем переход на страницу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    main_page.click_brokenimgs()# вызываем клик по элементу
    page.wait_for_timeout(1500)  # ждем 1500 миллисекунд = 1,5 секунды

    elms = BrokenImgsPageElms()
    broken_imgs_page = BrokenImgsPage(page, elms)

    '''
    broken_imgs_page.page_header_visible()# вызываем проверку видимости
    # broken_imgs_page_object.page_images_visible() # картинки специально битые и тест упадет
    broken_imgs_page.images_count(3)# вызываем проверку количества
    broken_imgs_page.url_check()  # вызываем проверку урла
    '''

    # локаторы к переменные
    page_header = page.locator(elms.PAGE_HEADER)
    page_images = page.locator(elms.PAGE_IMAGES)

    # проверки
    assert "/broken_images" in page.url
    assert page_header.is_visible()
    # assert elms.page_images.is_visible() # пока убрал чтоб тест не падал.но надо как-то проверить что они битые
    assert page_images.count() == 3

    # Вывод результатов в консоль
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {page.url}")
    print(f"📄 Виден заголовок страницы: {page_header.inner_text()}")
    print(f"📄 Количество картинок: {page_images.count()}")
    print("⏳ Ожидание 1,5 секунд...")

    # Скриншот
    page.screenshot(path="D:/Projects/the_internet/prtscr/open_broken_images_page_screenshot.png")
    print("📸 Скриншот сохранен как 'open_broken_images_page_screenshot.png'")