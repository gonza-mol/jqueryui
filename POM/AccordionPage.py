import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AccordionLocators:
    Item1 = (By.ID, "ui-id-1")
    Item2 = (By.ID, "ui-id-3")
    collapseOption = (By.CSS_SELECTOR, "#content ul >li:nth-child(2)>a")
    textOfItem2 = (By.CSS_SELECTOR, "#ui-id-4>p")



class AccordionPage:

    def __init__(self, driver):
        self.driver = driver




    def selectCollapseOption(self):
        self.driver.find_element(*AccordionLocators.collapseOption).click()

    def checkItem1IsSelected(self):
        return self.driver.find_element(*AccordionLocators.Item1).get_attribute('aria-selected')


    def contractItem1(self):
        self.driver.find_element(*AccordionLocators.Item1).click()

    def selectItem2(self):
        self.driver.find_element(*AccordionLocators.Item2).click()

    def getTextOfItem2(self):
        return self.driver.find_element(*AccordionLocators.textOfItem2).text

