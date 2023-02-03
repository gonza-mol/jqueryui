import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SelectableLocators:
    listElement = (By.CSS_SELECTOR, "#selectable>li")


class SelectablePage:

    def __init__(self, driver):
        self.driver = driver

    def getListItems(self):
        return self.driver.find_elements(*SelectableLocators.listElement)

    def selectEachItems(self, n):
        self.driver.find_element(By.CSS_SELECTOR, "#selectable>li:nth-child(" + str(n) + ")").click()

    def addNewItem(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).click(self.driver.find_element(By.CSS_SELECTOR, "#selectable>li:nth-child(2)")).key_up(Keys.CONTROL).perform()




