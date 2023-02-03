import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class SpinnerLocators:
    upNumber = (By.CSS_SELECTOR, "body span span.ui-icon-triangle-1-n")
    valueTextField = (By.CSS_SELECTOR, "#spinner.ui-spinner-input")
    btnEnabledDisabled = (By.CSS_SELECTOR, "#disable.ui-button")
    btnToggle = (By.CSS_SELECTOR, "#destroy.ui-widget")
    flagWithToggle = (By.CSS_SELECTOR, "body>p:nth-child(1)>span")
    flagWithOutToggle = (By.CSS_SELECTOR, "input#spinner")
    btnGetValue = (By.CSS_SELECTOR, "#getvalue")
    btnSetValue = (By.CSS_SELECTOR, "#setvalue")


class SpinnerPage:

    def __init__(self, driver):
        self.driver = driver

    def increaseNumber(self, number):
        n = 1
        while n <= number:
            self.driver.find_element(*SpinnerLocators.upNumber).click()
            time.sleep(1)
            n = n+1

    def getActualValueTextField(self):
        return self.driver.find_element(*SpinnerLocators.valueTextField).get_attribute('aria-valuenow')

    def enabledAndDisabledTextBox(self):
        self.driver.find_element(*SpinnerLocators.btnEnabledDisabled).click()

    def getStatusTextField(self):
        return self.driver.find_element(*SpinnerLocators.valueTextField).get_attribute('disabled')

    def seeActualStatusWithToggle(self):
        return self.driver.find_element(*SpinnerLocators.flagWithToggle).is_displayed()

    def seeActualStatusWithOutToggle(self):
        return self.driver.find_element(*SpinnerLocators.flagWithOutToggle).is_displayed()

    def disabledAndEnabledToogle(self):
        self.driver.find_element(*SpinnerLocators.btnToggle).click()

    def clickGetValueBtn(self):
        self.driver.find_element(*SpinnerLocators.btnGetValue).click()

    def clickSetValueBtn(self):
        self.driver.find_element(*SpinnerLocators.btnSetValue).click()
        return self.driver.find_element(*SpinnerLocators.valueTextField).get_attribute('aria-valuenow')

    def handleGetValue(self):
        ob = self.driver.switch_to.alert
        text = ob.text
        print("Text is: "+text)
        time.sleep(1)
        ob.accept()
        time.sleep(1)

