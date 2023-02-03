import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AutocompleteLocators:
    textFieldtags = (By.ID, "tags")
    optionJava = (By.ID, "ui-id-2")


class AutocompletePage:

    def __init__(self, driver):
        self.driver = driver

    def writeLanguageSearched(self, language):
        self.driver.find_element(*AutocompleteLocators.textFieldtags).send_keys(language)

    def selectJavaLanguage(self):
        self.driver.find_element(*AutocompleteLocators.optionJava).click()

