import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ButtonLocators:
    firstButton = (By.CSS_SELECTOR, "body>div>button")
    secondButton = (By.CSS_SELECTOR, "body>div>input")
    thirdButton = (By.CSS_SELECTOR, "body>div>a")

class ButtonPage:

    def __init__(self, driver):
        self.driver = driver

    def selectFirstButton(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element(*ButtonLocators.firstButton)).pause(2).perform()

    def selectSecondButton(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element(*ButtonLocators.secondButton)).pause(2).perform()

    def selectThirdButton(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element(*ButtonLocators.thirdButton)).pause(2).perform()

