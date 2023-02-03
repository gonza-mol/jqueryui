import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SliderLocators:
    slider = (By.CSS_SELECTOR, "#custom-handle.ui-state-default")
    modalOption = (By.CSS_SELECTOR, "#content ul>li:nth-child(3)>a")


class SliderPage:

    def __init__(self, driver):
        self.driver = driver

    def pickAndMoveSlider(self, value):
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element(*SliderLocators.slider)).move_by_offset(value, 0).pause(2).perform()

    def selectModalOption(self):
        self.driver.find_element(*SliderLocators.modalOption).click()

    def getValueOverSlider(self):
        return self.driver.find_element(*SliderLocators.slider)


