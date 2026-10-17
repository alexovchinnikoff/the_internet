# context_menu_page.py
class ContextMenuPageElms:
    PAGE_HEADER = "xpath=//h3[contains(text(), 'Context Menu')]"
    PAGE_TEXT_UPPER = "xpath=//p[contains(text(), 'Context menu items are custom')]"
    PAGE_TEXT_LOWER = "xpath=//p[contains(text(), 'Right-click in the box below')]"
    PAGE_BOX = "xpath=//div[@id='hot-spot']"


class ContextMenuPage:
    url = "https://the-internet.herokuapp.com/checkboxes"