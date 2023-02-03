import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SelectMenuLocators:
    modalOption = (By.CSS_SELECTOR, "#content ul>li:nth-child(3)>a")
    circleRadiusDropdown = (By.ID, "radius-button")
    circleColorDropdown = (By.ID, "color-button")
    allRadiusValues = (By.CSS_SELECTOR, "#radius-menu>li>div")
    allColorValues = (By.CSS_SELECTOR, "#color-menu>li>div")
    actualRadiusValue = (By.CSS_SELECTOR, "#radius-button > span.ui-selectmenu-text")
    actualColorValue = (By.CSS_SELECTOR, "#color-button > span.ui-selectmenu-text")
    circle = (By.CSS_SELECTOR, "#circle")


class SelectMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def selectModalOption(self):
        return self.driver.find_element(*SelectMenuLocators.modalOption).click()

    def selectRadiusDropdown(self):
        self.driver.find_element(*SelectMenuLocators.circleRadiusDropdown).click()

    def selectColorDropdown(self):
        self.driver.find_element(*SelectMenuLocators.circleColorDropdown).click()

    def selectRadiusValue(self, radius):
        values = self.driver.find_elements(*SelectMenuLocators.allRadiusValues)
        n = 1
        for value in values:
            #print(value.text)
            if radius == value.text:
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#radius-menu>li:nth-child(" + str(n) + ")")).click().perform()
                print("Se ha seleccionado y encontrado el radius solicitado "+radius)
                break

            else:
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#radius-menu>li:nth-child(" + str(n) + ")")).pause(2).perform()
                n = n+1

    def selectCircleColor(self, col):
        colors = self.driver.find_elements(*SelectMenuLocators.allColorValues)
        n = 1
        for color in colors:
            #print(color.text)
            #print(col)
            if col == color.text:
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#color-menu > li:nth-child(" + str(n) + ")")).click().perform()
                print("Se ha seleccionado y encontrado el color solicitado "+col)
                break


            else:
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#color-menu > li:nth-child(" + str(n) + ")")).pause(2).perform()
                n = n+1


    def getActualRadiusValue(self):
        return self.driver.find_element(*SelectMenuLocators.actualRadiusValue).text

    def getActualColorValue(self):
        return self.driver.find_element(*SelectMenuLocators.actualColorValue).text

    def getwidthAndHeightCircle(self):
        return self.driver.find_element(*SelectMenuLocators.circle).get_attribute('style')

    def getColorCircle(self):
        return self.driver.find_element(*SelectMenuLocators.actualColorValue).value_of_css_property('background')

