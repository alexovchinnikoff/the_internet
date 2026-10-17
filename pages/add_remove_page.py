# pages/add_remove_page.py
class AddRemovePageElms:
    PAGE_HEADER = "xpath=//h3[contains(text(), 'Add/Remove Elements')]"
    ADD_BUTTON = "xpath=//button[contains(text(), 'Add Element')]"
    DELETE_BUTTONS = "xpath=//button[contains(text(), 'Delete')]"
    DELETE_FIRST = "xpath=//button[contains(text(), 'Delete')][1]"
    DELETE_SECOND = "xpath=//button[contains(text(), 'Delete')][2]"


class AddRemovePage:
    url = "https://the-internet.herokuapp.com/add_remove_elements/"
