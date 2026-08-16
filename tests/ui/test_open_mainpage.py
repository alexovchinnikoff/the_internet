import pytest
from playwright.sync_api import Page, expect
import time

# Открывает страницу и ждет 3 секунды
def test_open_main_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/") # Открываем стартовую страницу
    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды
    expect(page).to_have_title("The Internet")# Ждем появления надписи
    expect(page).to_have_url("https://the-internet.herokuapp.com/")  # Проверяем урл
    welcome_header = page.locator("xpath=//h1[contains(text(), 'Welcome to the-internet')]")
    second_header = page.locator("xpath=//h2[contains(text(), 'Available Examples')]")
    hrefs = page.locator("xpath=//div[@id='content']/ul/li")
    expect(welcome_header).to_be_visible()# Ждем появления первого заголовка
    expect(second_header).to_be_visible()# Ждем появления второго заголовка
    expect(hrefs).to_have_count(44)  # Ждем появления 44 элементов(ссылок для перехода в разделы)
    hrefs_number = hrefs.count() # Кладем в переменную значение количества элементов(ссылок для перехода в разделы)
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы
    # Выводим информацию для наглядности
    print(f"\n✅ Стартовая страница The-Internet успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Заголовок: {page_title}")
    print(f"📄 Виден приветственный заголовок: {welcome_header.inner_text()}")
    print(f"📄 Виден второй заголовок: {second_header.inner_text()}")
    print(f"📄 В списке найдено {hrefs_number} элементов.")
    print("⏳ Ожидание 3 секунды...")

    # Можно добавить скриншот для наглядности
    page.screenshot(path="main_page_screenshot.png")
    print("📸 Скриншот сохранен как 'main_page_screenshot.png'")