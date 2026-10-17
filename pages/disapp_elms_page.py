# pages/disapp_elms_page.py
class DisAppElmsPageElms:
    PAGE_HEADER = "xpath=//div[@class='example']/h3[contains(text(), 'Disappearing Elements')]"
    PAGE_TEXT = "xpath=//div[@class='example']/p[contains(text(), 'This example demonstrates when elements on a page change by disappearing')]"
    HREFS = "//div[@id='content']/div[@class='example']/ul/li/a"
    HREF_HOME = "//a[contains(text(), 'Home')]"
    HREF_ABOUT = "//a[contains(text(), 'About')]"
    HREF_CONTACT = "//a[contains(text(), 'Contact Us')]"
    HREF_PORTFOLIO = "//a[contains(text(), 'Portfolio')]"