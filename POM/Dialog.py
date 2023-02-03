import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DialogLocators:
    optionClose = (By.CSS_SELECTOR, "body div.ui-draggable-handle>button")
    showText = (By.CSS_SELECTOR, "#dialog")
    modalFormOption = (By.CSS_SELECTOR, "#content ul > li:nth-child(4) > a")
    btnCreateNewUser = (By.CSS_SELECTOR, "#create-user.ui-widget")
    modalTitle = (By.CSS_SELECTOR, "#ui-id-1")
    btnCreateAccount = (By.CSS_SELECTOR, "body div>button:nth-child(1)")
    tableUsers = (By.CSS_SELECTOR, "#users>tbody td:nth-child(1)")
    nameField = (By.ID, "name")
    emailField = (By.ID, "email")
    passwordField = (By.ID, "password")
    btnCreateNewUser2 = (By.CSS_SELECTOR, "#create-user.ui-corner-all")


class DialogPage:

    def __init__(self, driver):
        self.driver = driver


    def clickCloseOption(self):
        self.driver.find_element(*DialogLocators.optionClose).click()

    def readTextFromPopUp(self):
        return self.driver.find_element(*DialogLocators.showText).text


    def selectModalForm(self):
        self.driver.find_element(*DialogLocators.modalFormOption).click()

    def selectBtnCreateNewUser(self):
        self.driver.find_element(*DialogLocators.btnCreateNewUser).click()

    def selectBtnCreateNewUser2(self):
        self.driver.find_element(*DialogLocators.btnCreateNewUser2).click()

    def getTitleFromModal(self):
        return self.driver.find_element(*DialogLocators.modalTitle).text

    def selectCreateAccount(self):
        self.driver.find_element(*DialogLocators.btnCreateAccount).click()

    def getAllUsers(self):
        return self.driver.find_elements(*DialogLocators.tableUsers)

    def verifyUserExistence(self):
        users = self.getAllUsers()
        for user in users:
            time.sleep(2)
            if user.text == "Jane Smith":
                print("La usuaria " + user.text + " ha sido creada con éxito")
                break
            print("\nUsuario/a ya existente: " + user.text)

    def AddNewUser(self, name, email, password):
        self.driver.find_element(*DialogLocators.nameField).clear()
        self.driver.find_element(*DialogLocators.emailField).clear()
        self.driver.find_element(*DialogLocators.passwordField).clear()
        self.driver.find_element(*DialogLocators.nameField).send_keys(name)
        self.driver.find_element(*DialogLocators.emailField).send_keys(email)
        self.driver.find_element(*DialogLocators.passwordField).send_keys(password)
        #self.driver.find_element(*DialogLocators.btnCreateAccount).click()

