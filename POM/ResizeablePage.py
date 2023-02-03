import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ResizeableLocators:
    boxIcon = (By.CSS_SELECTOR, "#resizable>div.ui-icon-gripsmall-diagonal-se")


class ResizeablePage:

    def __init__(self, driver):
        self.driver = driver

    def clickResizeable(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*ResizeableLocators.boxIcon), 200, 250).perform()






