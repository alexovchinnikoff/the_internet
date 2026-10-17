# pages/abtest_page.py
class ABTestPageElms:
    PAGE_HEADER = "//h3[contains(text(), 'A/B Test')]"
    PAGE_TEXT = "//p[contains(text(), 'Also known as split testing.')]"


class ABTestPage:
    url = "https://the-internet.herokuapp.com/abtest"