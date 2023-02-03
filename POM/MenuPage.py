import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class MenuLocators:
    menuItems = (By.CSS_SELECTOR, "#menu>li")
    subItemRock = (By.CSS_SELECTOR, "#ui-id-10")
    subItemAlternative = (By.CSS_SELECTOR, "#ui-id-11")


class MenuPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllItems(self):
        return self.driver.find_elements(*MenuLocators.menuItems)

    def selectHover(self, items):
        n = 1
        for item in items:
            time.sleep(1)
            if "(n/a)" in item.text: #or item.text in "Specials (n/a)":
                print("opción deshabilitada " + item.text)
            else:
                action = ActionChains(self.driver)
                action.move_to_element(item).perform()
                print("opción habilitada " + item.text)
                if item.text == "Music":
                    time.sleep(1)
                    action.move_to_element(self.driver.find_element(*MenuLocators.subItemRock)).click().perform()
                    name = self.driver.find_element(*MenuLocators.subItemRock).text
                    assert "Rock" == name
                    print("sub opción seleccionado " + str(name))
                    time.sleep(2)
                    action.move_to_element(self.driver.find_element(*MenuLocators.subItemAlternative)).perform()
                    name1 = self.driver.find_element(*MenuLocators.subItemAlternative).text
                    action.move_to_element(self.driver.find_element(*MenuLocators.subItemAlternative)).click()
                    time.sleep(2)
                    print("sub opción habilitada " + str(name1))


