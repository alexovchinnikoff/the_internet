# pages/main_page.py
class MainPageElms:
    WELCOME_HEADER = "//h1[contains(text(), 'Welcome to the-internet')]"
    SECOND_HEADER = "//h2[contains(text(), 'Available Examples')]"
    LINKS = "//div[@id='content']/ul/li/a"
    LINK_ABTEST = "//a[contains(text(), 'A/B Testing')]"
    LINK_ADDREMOVEELMS = "//a[contains(text(), 'Remove Elements')]"
    LINK_BASICAUTH = "//a[contains(text(), 'Basic Auth')]"
    LINK_BROKENIMGS = "//a[contains(text(), 'Broken Images')]"
    LINK_CHALDOM = "//a[contains(text(), 'Challenging DOM')]"
    LINK_CHECKBOXES = "//a[contains(text(), 'Checkboxes')]"
    LINK_CONTEXTMENU = "//a[contains(text(), 'Context Menu')]"
    LINK_DIGESTAUTH = "//a[contains(text(), 'Digest Auth')]"
    LINK_DISAPPELMS = "//a[contains(text(), 'Disappearing Elements')]"


class MainPage:
    url = "https://the-internet.herokuapp.com/"