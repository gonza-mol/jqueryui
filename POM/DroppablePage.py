import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DroppableLocators:
    drag = (By.CSS_SELECTOR, "#draggable")
    drop = (By.CSS_SELECTOR, "#droppable")
    titleDroppable = (By.CSS_SELECTOR, "#droppable>p")



class DroppablePage:

    def __init__(self, driver):
        self.driver = driver


    def clickAndDrop(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*DroppableLocators.drag), self.driver.find_element(*DroppableLocators.drop)).perform()

    def getTitle(self):
        return self.driver.find_element(*DroppableLocators.titleDroppable).text





