# user_client.py
import allure
from playwright.sync_api import Page


class User:


    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url:str):
        with allure.step(f"Открываю страницу {url}"):
            self.page.goto(url, timeout=60000)

    def click_element(self, element):
        with allure.step(f"Клик по элементу {element}"):
            self.page.click(element, timeout=60000)

    def wait_sec(self, sec:int):
        ms = sec * 1000
        with allure.step(f"Жду {sec} секунд (всего {ms} мс)"):
            self.page.wait_for_timeout(ms)

    def make_screenshot(self, name: str = "screenshot"):
        image_bytes = self.page.screenshot()
        with allure.step(f"Делаю скриншот {name}"):
            allure.attach( image_bytes, name=name, attachment_type=allure.attachment_type.PNG)