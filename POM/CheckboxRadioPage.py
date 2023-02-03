import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class CheckboxRadioLocators:
    allRadioButton = (By.CSS_SELECTOR, "body fieldset:nth-child(3) span.ui-icon-background.ui-icon-blank")
    allCheckbox = (By.CSS_SELECTOR, "body fieldset:nth-child(5) span.ui-icon-blank")
    check2star = (By.CSS_SELECTOR, "body>div>fieldset:nth-child(5)>label>span.ui-state-checked")
    check3star = (By.CSS_SELECTOR, "fieldset:nth-child(5)>label:nth-child(4)>span.ui-state-checked")
    allCheckboxBed = (By.CSS_SELECTOR, "body fieldset:nth-child(7) span.ui-icon-blank")
    chebox1King = (By.CSS_SELECTOR, "body>div>fieldset:nth-child(7) span.ui-state-checked")
    title = (By.CSS_SELECTOR, "body>div>h1")

class CheckboxRadioPage:

    def __init__(self, driver):
        self.driver = driver

    def selectAllRadioButton(self):
        radioButtons = self.driver.find_elements(*CheckboxRadioLocators.allRadioButton)
        for radioButton in radioButtons:
            time.sleep(2)
            radioButton.click()

    def selectAllCheckbox(self):
        checkboxes = self.driver.find_elements(*CheckboxRadioLocators.allCheckbox)
        for checkbox in checkboxes:
            time.sleep(2)
            checkbox.click()


    def uncheckSecondCheckbox(self):
        self.driver.find_element(*CheckboxRadioLocators.check2star).click()


    def uncheckThirdCheckbox(self):
        self.driver.find_element(*CheckboxRadioLocators.check3star).click()

    def checkIfSecondIsUnselected(self):
        return self.driver.find_element(*CheckboxRadioLocators.check2star).get_attribute('class')

    def checkIfThirdIsUnselected(self):
        return self.driver.find_element(*CheckboxRadioLocators.check3star).get_attribute('class')

    def selectLastTwoCheckboxBed(self):
        checkboxes = self.driver.find_elements(*CheckboxRadioLocators.allCheckboxBed)
        #cant = len(sp.getListItems())
        i = 0
        for checkbox in checkboxes:
            if i >= 2:
                checkbox.click()
                i = i+1
                time.sleep(2)
            i = i+1





