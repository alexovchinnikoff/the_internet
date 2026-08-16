import pytest
from playwright.sync_api import Page, expect
import time

# Открывает страницу и ждет 3 секунд
def test_open_basic_auth_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/") # Открываем страницу
    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды
    basic_auth = page.locator("xpath=//a[contains(text(), 'Basic Auth')]")
    expect(basic_auth).to_be_visible()  # Элемент виден
    expect(basic_auth).to_be_enabled()  # Элемент активен
    expect(basic_auth).to_have_text("Basic Auth")  # На элементе есть надпись
    page.click("xpath=//a[contains(text(), 'Basic Auth')]")  # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды

    # ввести во всплывающем окне (user and pass: admin) и нажать "Войти"
    expect(page).to_have_url("https://the-internet.herokuapp.com/basic_auth")
    header = page.locator("xpath=//h3[contains(text(), 'Basic Auth')]")
    expect(header).to_be_visible()
    expect(header).to_have_text("Basic Auth")
    text = page.locator("xpath=//p[contains(text(), 'Congratulations! You must have the proper credentials.')]")
    expect(text).to_be_visible()
    expect(text).to_have_text("Congratulations! You must have the proper credentials.")

    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы

    # Выводим информацию для наглядности
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Заголовок: {page_title}")
    print(f"📄 Виден заголовок страницы: {header.inner_text()}")
    print(f"📄 Виден заголовок страницы: {text.inner_text()}")
    print("⏳ Ожидание 3 секунд...")

    # Можно добавить скриншот для наглядности
    page.screenshot(path="abtest_screenshot.png")
    print("📸 Скриншот сохранен как 'abtest_screenshot.png'")