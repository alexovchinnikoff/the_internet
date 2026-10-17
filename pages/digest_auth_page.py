# pages/digest_auth_page.py
from playwright.sync_api import Page, expect
from base.user_client import User


class DigestAuthPageElms:
    PAGE_HEADER = "xpath=//h3[contains(text(), 'Digest Auth')]"
    PAGE_TEXT = "xpath=//p[contains(text(), 'Congratulations!')]"


class DigestAuthPage:
    url = "https://admin:admin@the-internet.herokuapp.com/digest_auth"
    # создаем функцию начальных значений (ссылка на браузер из теста и локаторы)
    def __init__(self, page: Page, elms: DigestAuthPageElms):
        self.page = page
        self.elms = elms
        self.user = User(page)

    def go_to(self):
        self.user.open_page(self.url)
        return self

    def wait_for_load(self, sec: int = 2):
        self.user.wait_sec(sec)
        return self

    def header_and_text_visible(self):
        expect(self.page.locator(self.elms.PAGE_HEADER)).to_be_visible()
        expect(self.page.locator(self.elms.PAGE_TEXT)).to_be_visible()

    def url_check(self):
        expect(self.page).to_have_url(self.url)