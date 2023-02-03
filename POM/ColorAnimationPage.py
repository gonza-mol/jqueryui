import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ColorAnimationLocators:
    textarea = (By.CSS_SELECTOR, "div#effect")
    btnToggleEffect = (By.CSS_SELECTOR, "button#button")



class ColorAnimationPage:

    def __init__(self, driver):
        self.driver = driver

    def getWidthOfBoxArea(self):
        return self.driver.find_element(*ColorAnimationLocators.textarea).value_of_css_property('width')

    def getBackgroundColorOfBoxArea(self):
        return self.driver.find_element(*ColorAnimationLocators.textarea).value_of_css_property('background-color')

    def selectBtnToggleEffect(self):
        self.driver.find_element(*ColorAnimationLocators.btnToggleEffect).click()


