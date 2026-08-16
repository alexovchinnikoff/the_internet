import pytest
from playwright.sync_api import Page, expect
import time

# Открывает страницу и ждет 3 секунд
def test_add_two_elements_and_delete_both(page: Page):
    page.goto("https://the-internet.herokuapp.com/") # Открываем стартовую страницу
    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунд
    add_remove_elms = page.locator("xpath=//a[contains(text(), 'Add/Remove Elements')]")
    expect(add_remove_elms).to_be_visible()  # Элемент виден
    expect(add_remove_elms).to_be_enabled()  # Элемент активен
    expect(add_remove_elms).to_have_text("Add/Remove Elements")# На элементе есть надпись
    page.click("xpath=//a[contains(text(), 'Add/Remove Elements')]")  # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды

    second_header = page.locator("xpath=//h3[contains(text(), 'Add/Remove Elements')]")
    expect(page).to_have_url("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = page.locator("xpath=//button[text()='Add Element']")
    expect(add_element).to_be_visible()  # Элемент виден
    expect(add_element).to_be_enabled()  # Элемент активен
    expect(add_element).to_have_text("Add Element")# На элементе есть надпись
    page.click("xpath=//button[text()='Add Element']") # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды

    page.click("xpath=//button[text()='Add Element']")  # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунды

    delete_element = page.locator("xpath=//button[text()='Delete']")
    page.click("xpath=//button[text()='Delete']") # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3

    expect(page).to_have_url("https://the-internet.herokuapp.com/add_remove_elements/")
    expect(add_element).to_be_visible()  # Элемент виден
    expect(add_element).to_be_enabled()  # Элемент активен
    expect(add_element).to_have_text("Add Element")  # На элементе есть надпись
    expect(delete_element.first).to_be_visible()  # Элемент виден
    expect(delete_element.first).to_be_enabled()  # Элемент активен
    expect(delete_element.first).to_have_text("Delete")  # На элементе есть надпись
    expect(delete_element.nth(1)).to_be_hidden()  # Элемента не видно

    page.click("xpath=//button[text()='Delete']")  # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3

    expect(page).to_have_url("https://the-internet.herokuapp.com/add_remove_elements/")
    expect(add_element).to_be_visible()  # Элемент виден
    expect(add_element).to_be_enabled()  # Элемент активен
    expect(add_element).to_have_text("Add Element")  # На элементе есть надпись
    expect(delete_element.first).to_be_hidden() # Элемента не видно
    expect(delete_element.nth(1)).to_be_hidden()  # Элемента не видно

    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы
    # Выводим информацию для наглядности
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Заголовок: {page_title}")
    print(f"📄 Виден заголовок страницы: {second_header.inner_text()}")
    print(f"📄 Видна кнопка: {add_element.inner_text()}")

    print("⏳ Ожидание 3 секунды...")

    # Можно добавить скриншот для наглядности
    page.screenshot(path="add_two_elms_and_delete_both_screenshot.png")
    print("📸 Скриншот сохранен как 'add_two_elms_and_delete_both_screenshot.png'")


   