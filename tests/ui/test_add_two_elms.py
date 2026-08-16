import pytest
from playwright.sync_api import Page, expect
import time

# Открывает страницу и ждет 3 секунд
def test_add_two_elements(page: Page):
    page.goto("https://the-internet.herokuapp.com/") # Открываем стартовую страницу
    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунд
    add_remove_elms = page.locator("xpath=//a[contains(text(), 'Add/Remove Elements')]")
    expect(add_remove_elms).to_be_visible()  # Элемент виден
    expect(add_remove_elms).to_be_enabled()  # Элемент активен
    expect(add_remove_elms).to_have_text("Add/Remove Elements")# На элементе есть надпись
    page.click("xpath=//a[contains(text(), 'Add/Remove Elements')]")  # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунд

    second_header = page.locator("xpath=//h3[contains(text(), 'Add/Remove Elements')]")
    add_element = page.locator("xpath=//button[text()='Add Element']")
    expect(page).to_have_url("https://the-internet.herokuapp.com/add_remove_elements/")
    expect(add_element).to_be_visible()  # Элемент виден
    expect(add_element).to_be_enabled()  # Элемент активен
    expect(add_element).to_have_text("Add Element")# На элементе есть надпись
    page.click("xpath=//button[text()='Add Element']") # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунд

    expect(page).to_have_url("https://the-internet.herokuapp.com/add_remove_elements/")
    delete_element = page.locator("xpath=//button[text()='Delete']")
    expect(add_element).to_be_visible()  # Элемент виден
    expect(add_element).to_be_enabled()  # Элемент активен
    expect(add_element).to_have_text("Add Element")  # На элементе есть надпись
    expect(delete_element).to_be_visible()  # Элемент виден
    expect(delete_element).to_be_enabled()  # Элемент активен
    expect(delete_element).to_have_text("Delete")  # На элементе есть надпись
    page.click("xpath=//button[text()='Add Element']")  # Клик по элементу

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунд

    expect(page).to_have_url("https://the-internet.herokuapp.com/add_remove_elements/")
    added_elements = page.locator("xpath=//div[@id='elements']/button")
    expect(added_elements).to_have_count(2)
    added_elements_number = added_elements.count()
    expect(added_elements.first).to_be_visible()  # Элемент виден
    expect(added_elements.nth(1)).to_be_visible()  # Элемент виден
    expect(added_elements.first).to_be_enabled()  # Элемент активен
    expect(added_elements.nth(1)).to_be_enabled()
    expect(added_elements.first).to_have_text("Delete")  # На элементе есть надпись
    expect(added_elements.nth(1)).to_have_text("Delete")
    current_url = page.url  # Текущий URL
    page_title = page.title()  # Заголовок страницы

    page.wait_for_timeout(3000)  # 3000 миллисекунд = 3 секунд

    # Выводим информацию для наглядности
    print(f"\n✅ Страница успешно загружена")
    print(f"📍 Текущий URL: {current_url}")
    print(f"📄 Заголовок: {page_title}")
    print(f"📄 Виден заголовок страницы: {second_header.inner_text()}")
    print(f"📄 Видна кнопка: {add_element.inner_text()}")
    print(f"📄 Видна кнопка: {delete_element.first.inner_text()} в количестве {added_elements_number} шт.")
    print("⏳ Ожидание 3 секунды...")

    # Можно добавить скриншот для наглядности
    page.screenshot(path="add_two_elms_screenshot.png")
    print("📸 Скриншот сохранен как 'add_two_elms_screenshot.png'")


   