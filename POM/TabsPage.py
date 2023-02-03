import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TabsLocators:
    modalOption = (By.CSS_SELECTOR, "#content ul>li:nth-child(2)>a")
    allTabs = (By.CSS_SELECTOR, "#tabs>ul>li")
    titleOfTabs = (By.CSS_SELECTOR, "#tabs-1>p:nth-child(1)>strong")


class TabsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectModalOption1(self):
        return self.driver.find_element(*TabsLocators.modalOption).click()

    def getAllTabs(self):
        tabs = self.driver.find_elements(*TabsLocators.allTabs)
        n = 1
        for tab in tabs:

            if n != 1:
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#tabs>ul>li:nth-child(" + str(n) + ")")).click().perform()
                time.sleep(2)
                assert "rgb(0, 127, 255)" in tab.value_of_css_property('background')
                print("\nEl nombre de la tab número " + str(n) + " es " + tab.text)
                n = n + 1
            else:
                print("\nEl nombre de la tab número " + str(n) + " es " + tab.text)
                assert "rgb(0, 127, 255)" in tab.value_of_css_property('background')
                n = n + 1
                time.sleep(2)

    def openTab(self):
        tabs1 = self.driver.find_elements(*TabsLocators.allTabs)
        n = 1
        for tab in tabs1:

            if n != 1:
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#tabs>ul>li:nth-child(" + str(
                    n) + ")")).click().perform()
                time.sleep(2)
                assert str(self.driver.find_element(By.CSS_SELECTOR, "#tabs-"+str(n)+">p:nth-child(1)>strong").is_displayed()) == "True"
                print("El texto se está visualizando en la tab "+str(tab.text))
                n = n + 1
            else:
                assert str(self.driver.find_element(By.CSS_SELECTOR, "#tabs-"+str(n)+">p:nth-child(1)>strong").is_displayed()) == "True"
                print("\nEl texto se está visualizando en la tab "+str(tab.text))
                n = n + 1
                time.sleep(2)

    def collapseTab(self):
        n = 1
        while n <= 3:

            if n != 1:
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "#tabs>ul>li:nth-child(" + str(n) + ")").click()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "#tabs>ul>li:nth-child(" + str(n) + ")").click()
                time.sleep(1)
                assert str(self.driver.find_element(By.CSS_SELECTOR, "#tabs-" + str(n) + ">p:nth-child(1)>strong").is_displayed()) == "False"
                print("El texto ya no se está visualizando en la tab " + str(n))
                n = n + 1
                time.sleep(2)
            else:
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "#tabs>ul>li:nth-child(" + str(n) + ")").click()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "#tabs>ul>li:nth-child(" + str(n) + ")").click()
                time.sleep(1)
                assert str(self.driver.find_element(By.CSS_SELECTOR, "#tabs-" + str(n) + ">p:nth-child(1)>strong").is_displayed()) == "False"
                print("El texto ya no se está visualizando en la tab " + str(n))
                n = n + 1
                time.sleep(2)

