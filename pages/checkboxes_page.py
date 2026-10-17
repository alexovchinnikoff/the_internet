# pages/checkboxes_page.py
class CheckBoxesPageElms:
    PAGE_HEADER = "xpath=//h3[contains(text(), 'Checkboxes')]"
    PAGE_CHECKBOXES = "xpath=//input[@type='checkbox']"
    CHECKED_CHECKBOXES = "xpath=//input[@type='checkbox' and @checked]"
    CHECKBOX_UPPER = "xpath=//input[@type='checkbox'][1]"
    CHECKBOX_LOWER = "xpath=//input[@type='checkbox'][2]"


class CheckBoxesPage:
    url = "https://the-internet.herokuapp.com/checkboxes"