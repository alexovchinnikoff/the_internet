# pages/broken_imgs_page.py
class BrokenImgsPageElms:
    PAGE_HEADER = "xpath=//h3[contains(text(), 'Broken Images')]"
    PAGE_IMAGES = "xpath=//img[contains(@src, '.jpg')]"


class BrokenImgsPage:
    url = "https://the-internet.herokuapp.com/broken_images"