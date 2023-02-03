import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HomePageLocators:
    draggableLink = (By.XPATH, "//a[contains(text(),'Draggable')]")
    droppableLink = (By.XPATH, "//a[contains(text(),'Droppable')]")
    resizableLink = (By.XPATH, "//a[contains(text(),'Resizable')]")
    selectableLink = (By.XPATH, "//a[contains(text(),'Selectable')]")
    sortableLink = (By.XPATH, "//a[contains(text(),'Sortable')]")
    accordionLink = (By.XPATH, "//a[contains(text(),'Accordion')]")
    autocompleteLink = (By.XPATH, "//a[contains(text(),'Autocomplete')]")
    buttonLink = (By.XPATH, "//a[contains(text(),'Button')]")
    checkboxRadioLink = (By.XPATH, "//a[contains(text(),'Checkboxradio')]")
    datePickerLink = (By.XPATH, "//a[contains(text(),'Datepicker')]")
    dialogLink = (By.XPATH, "//a[contains(text(),'Dialog')]")
    menuLink = (By.XPATH, "//a[contains(text(),'Menu')]")
    progressbarLink = (By.XPATH, "//a[contains(text(),'Progressbar')]")
    selectMenuLink = (By.XPATH, "//a[contains(text(),'Selectmenu')]")
    sliderLink = (By.XPATH, "//a[contains(text(),'Slider')]")
    spinnerLink = (By.XPATH, "//a[contains(text(),'Spinner')]")
    tabsLink = (By.XPATH, "//a[contains(text(),'Tabs')]")
    tooltipLink = (By.XPATH, "//a[contains(text(),'Tooltip')]")
    colorAnimationLink = (By.XPATH, "//a[contains(text(),'Color Animation')]")



class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def clickDraggableLink(self):
        self.driver.find_element(*HomePageLocators.draggableLink).click()

    def clickDroppaleLink(self):
        self.driver.find_element(*HomePageLocators.droppableLink).click()

    def clickResizeableLink(self):
        self.driver.find_element(*HomePageLocators.resizableLink).click()

    def clickSelectableLink(self):
        self.driver.find_element(*HomePageLocators.selectableLink).click()

    def clickSortableLink(self):
        self.driver.find_element(*HomePageLocators.sortableLink).click()

    def clickAccordionLink(self):
        self.driver.find_element(*HomePageLocators.accordionLink).click()

    def clickAutocompleteLink(self):
        self.driver.find_element(*HomePageLocators.autocompleteLink).click()

    def clickButtonLink(self):
        self.driver.find_element(*HomePageLocators.buttonLink).click()

    def clickCheckboxRadioLink(self):
        self.driver.find_element(*HomePageLocators.checkboxRadioLink).click()

    def clickDatePickerLink(self):
        self.driver.find_element(*HomePageLocators.datePickerLink).click()

    def clickDialogLink(self):
        self.driver.find_element(*HomePageLocators.dialogLink).click()

    def clickMenuLink(self):
        self.driver.find_element(*HomePageLocators.menuLink).click()

    def clickProgressbarLink(self):
        self.driver.find_element(*HomePageLocators.progressbarLink).click()

    def clickSelectMenuLink(self):
        self.driver.find_element(*HomePageLocators.selectMenuLink).click()

    def clickSliderLink(self):
        self.driver.find_element(*HomePageLocators.sliderLink).click()

    def clickSpinnerLink(self):
        self.driver.find_element(*HomePageLocators.spinnerLink).click()

    def clickTabsLink(self):
        self.driver.find_element(*HomePageLocators.tabsLink).click()

    def clickTooltipLink(self):
        self.driver.find_element(*HomePageLocators.tooltipLink).click()

    def colorAnimationLink(self):
        self.driver.find_element(*HomePageLocators.colorAnimationLink).click()



