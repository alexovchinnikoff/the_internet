# pages/chal_dom_page.py
class ChalDomPageElms:
    PAGE_HEADER = "xpath=//div[@class='example']/h3[contains(text(), 'Challenging DOM')]"
    PAGE_TEXT = "xpath=//div[@class='example']/p[contains(text(), 'The hardest part in automated web testing')]"
    BUTTONS = "xpath=//div[@class='large-2 columns']/a"
    BUTTON_UPPER = "xpath=//a[@class='button'][1]"
    BUTTON_MIDDLE = "xpath=//a[@class='button alert']"
    BUTTON_LOWER = "xpath=//a[@class='button success']"
    TABLE = "xpath=//table"
    THEAD = "xpath=//table/thead"
    THEAD_ROW = "xpath=//table/thead/tr"
    THEAD_HEADERS = "xpath=//table/thead/tr/th"
    LOREM = "xpath=//th[contains(text(), 'Lorem')]"
    IPSUM = "xpath=//th[contains(text(), 'Ipsum')]"
    DOLOR = "xpath=//th[contains(text(), 'Dolor')]"
    SIT = "xpath=//th[contains(text(), 'Sit')]"
    AMET = "xpath=//th[contains(text(), 'Amet')]"
    DICERET = "xpath=//th[contains(text(), 'Diceret')]"
    ACTION = "xpath=//th[contains(text(), 'Action')]"

    TABLE_BODY = "xpath=//table/tbody"
    TABLE_BODY_ROWS = "xpath=//table/tbody/tr"
    TABLE_BODY_HEADERS = "xpath=//table/tbody/tr/td"
    HREF_EDIT = "xpath=//a[contains(text(), 'edit')]"
    HREF_DELETE = "xpath=//a[contains(text(), 'delete')]"

    PAGE_CANVAS = 'xpath=//div//canvas[@width="599" and @height="200"]'


class ChalDomPage:
    url = "https://the-internet.herokuapp.com/challenging_dom"