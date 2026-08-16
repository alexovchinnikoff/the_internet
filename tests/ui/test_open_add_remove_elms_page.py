import pytest
from playwright.sync_api import Page, expect
import time

# Открывает страницу и ждет 3 секунды
def test_open_add_remove_elements_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/") # Открываем стартовую страницу
    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды
    expect(page.locator("xpath=//a[contains(text(), 'Add/Remove Elements')]")).to_be_visible()  # Элемент виден
    expect(page.locator("xpath=//a[contains(text(), 'Add/Remove Elements')]")).to_be_enabled()  # Элемент активен
    expect(page.locator("xpath=//a[contains(text(), 'Add/Remove Elements')]")).to_have_text("Add/Remove Elements")# На элементе есть надпись
    page.click("xpath=//a[contains(text(), 'Add/Remove Elements')]")  # Клик по элементу

    second_header = page.locator("xpath=//h3[contains(text(), 'Add/Remove Elements')]")
    expect(page).to_have_url("https://the-internet.herokuapp.com/add_remove_elements/")
    expect(second_header).to_be_visible()
    expect(second_header).to_have_text("Add/Remove Elements")
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы

    # Выводим информацию для наглядности
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Заголовок: {page_title}")
    print(f"📄 Виден заголовок страницы: {second_header.inner_text()}")
    print("⏳ Ожидание 3 секунды...")

    # Можно добавить скриншот для наглядности
    page.screenshot(path="add_remove_elms_screenshot.png")
    print("📸 Скриншот сохранен как 'add_remove_elms_screenshot.png'")