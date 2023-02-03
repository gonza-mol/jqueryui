import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class ToolTipLocators:
    yourAgeTxtField = (By.ID, "age")
    banner = (By.CSS_SELECTOR, "div.ui-tooltip")
    firstTooltip = (By.CSS_SELECTOR, "body>p:nth-child(1)>a")
    outHover = (By.CSS_SELECTOR, "body>p:nth-child(3)")
    secondTooltip = (By.CSS_SELECTOR, "body>p:nth-child(2)>a")


class ToolTipPage:

    def __init__(self, driver):
        self.driver = driver

    def clickYourAgeTxtField(self):
        self.driver.find_element(*ToolTipLocators.yourAgeTxtField).click()

    def getBanner(self):
        return self.driver.find_element(*ToolTipLocators.banner).text

    def clickFirstTooltip(self):
        self.driver.find_element(*ToolTipLocators.firstTooltip).click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*ToolTipLocators.firstTooltip)).perform()
        time.sleep(2)

    def clickSecondTooltip(self):
        self.driver.find_element(*ToolTipLocators.outHover).click()
        self.driver.find_element(*ToolTipLocators.secondTooltip).click()

        #action = ActionChains(self.driver)
        #action.send_keys(self.driver.find_element(*ToolTipLocators.firstTooltip)).perform()
