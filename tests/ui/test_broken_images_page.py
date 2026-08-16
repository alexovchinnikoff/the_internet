import pytest
from playwright.sync_api import Page, expect
import time

# Открывает страницу и ждет 3 секунд
def test_open_broken_images_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/") # Открываем страницу
    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды
    broken_images = page.locator("xpath=//a[contains(text(), 'Broken Images')]")
    expect(broken_images).to_be_visible()  # Элемент виден
    expect(broken_images).to_be_enabled()  # Элемент активен
    expect(broken_images).to_have_text("Broken Images")  # На элементе есть надпись
    page.click("xpath=//a[contains(text(), 'Broken Images')]")  # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды

    # ввести во всплывающем окне (user and pass: admin) и нажать "Войти"
    expect(page).to_have_url("https://the-internet.herokuapp.com/broken_images")
    header = page.locator("xpath=//h3[contains(text(), 'Broken Images')]")
    expect(header).to_be_visible()
    expect(header).to_have_text("Broken Images")
    images_to_see = page.locator("xpath=//div[@id='content']/div/img")
    expect(images_to_see).to_have_count(3)
    images_to_see_number = broken_images.count()
    expect(images_to_see.first).to_be_visible()
    expect(images_to_see.nth(1)).to_be_visible()
    expect(images_to_see.nth(2)).to_be_visible()
# как проверить наличие картинок по .jpg????
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы

    # Выводим информацию для наглядности
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Заголовок: {page_title}")
    print(f"📄 Виден заголовок страницы: {header.inner_text()}")
    print(f"📄 Количество картинок: {images_to_see_number}")
    print("⏳ Ожидание 3 секунд...")

    # Можно добавить скриншот для наглядности
    page.screenshot(path="abtest_screenshot.png")
    print("📸 Скриншот сохранен как 'abtest_screenshot.png'")