import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DraggableLocators:
    draggable = (By.CSS_SELECTOR, "#draggable")




class DraggablePage:

    def __init__(self, driver):
        self.driver = driver


    def clickDraggable(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element(*DraggableLocators.draggable)).move_by_offset(300, 0).perform()







