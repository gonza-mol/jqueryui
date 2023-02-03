import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SortableLocators:
    listElement = (By.CSS_SELECTOR, "#sortable>li")
    item7Box = (By.CSS_SELECTOR, "#sortable>li:nth-child(7)")


class SortablePage:

    def __init__(self, driver):
        self.driver = driver

    def getListItems(self):
        return self.driver.find_elements(*SortableLocators.listElement)

    def printAllListItems(self):
        aux = self.getListItems()
        n = 1
        for i in aux:
            print(self.getEachNameItems(n))
            n = n+1

    def printUpdatedListItems(self):
        aux = self.getListItems()
        n = 1
        nas = 1
        print("\nY ahora, habiendo movido el item 7, la lista a quedado de la siguiente manera:")
        for i in aux:
            print(self.getEachNameItems(n))
            if nas == 5:
                assert self.getEachNameItems(n) == "Item 7"
            n = n + 1
            nas = nas+1
        print("En la posición 5, está el item 7, como es lo esperado")


    def getEachNameItems(self, n):
        return self.driver.find_element(By.CSS_SELECTOR, "#sortable>li:nth-child(" + str(n) + ")").text

    def clickDraggableItem7(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*SortableLocators.item7Box), 0, -100).perform()
