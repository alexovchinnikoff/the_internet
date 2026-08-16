import pytest
from playwright.sync_api import Page, expect
import time

# Открывает страницу и ждет 3 секунды
def test_open_abtest_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/") # Открываем стартовую страницу
    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды
    abtest = page.locator("xpath=//a[contains(text(), 'A/B Testing')]")
    expect(abtest).to_be_visible()  # Элемент виден
    expect(abtest).to_be_enabled()  # Элемент активен
    expect(abtest).to_have_text("A/B Testing")# На элементе есть надпись
    page.click("xpath=//a[contains(text(), 'A/B Testing')]")  # Клик по элементу

    second_header = page.locator("xpath=//h3[contains(text(), 'A/B Test Control')]")
    expect(page).to_have_url("https://the-internet.herokuapp.com/abtest")
    expect(second_header).to_be_visible()
    expect(second_header).to_have_text("A/B Test Control")
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы

    # Выводим информацию для наглядности
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Заголовок: {page_title}")
    print(f"📄 Виден заголовок страницы: {second_header.inner_text()}")
    print("⏳ Ожидание 3 секунды...")

    # Можно добавить скриншот для наглядности
    page.screenshot(path="abtest_screenshot.png")
    print("📸 Скриншот сохранен как 'abtest_screenshot.png'")