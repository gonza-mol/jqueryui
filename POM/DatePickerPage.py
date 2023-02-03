import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DatePickerLocators:
    calendarField = (By.ID, "datepicker")
    calendarMonth = (By.CSS_SELECTOR, "#ui-datepicker-div span.ui-datepicker-month")
    calendarYear = (By.CSS_SELECTOR, "#ui-datepicker-div span.ui-datepicker-year")
    calendarMonthYear = (By.CSS_SELECTOR, "#ui-datepicker-div>div>div")
    nextMonthYear = (By.CSS_SELECTOR, "#ui-datepicker-div a.ui-datepicker-next.ui-corner-all")




class DatePickerPage:

    def __init__(self, driver):
        self.driver = driver


    def clickCalendarField(self):
        self.driver.find_element(*DatePickerLocators.calendarField).click()

    def getCalendarMonth(self):
        return self.driver.find_element(*DatePickerLocators.calendarMonth).text

    def getCalendarYear(self):
        return self.driver.find_element(*DatePickerLocators.calendarYear).text

    def getCalendarMonthYear(self):
        return self.driver.find_element(*DatePickerLocators.calendarMonthYear).text

    def nextMonthAndYear(self):
        self.driver.find_element(*DatePickerLocators.nextMonthYear).click()

    def selectDay(self, day):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'" + str(day) + "')]").click()

    def selectYear(self, exy):
        acy = self.driver.find_element(*DatePickerLocators.calendarYear).text
        while acy != exy:
            self.driver.find_element(*DatePickerLocators.nextMonthYear).click()
            acy = self.driver.find_element(*DatePickerLocators.calendarYear).text
            time.sleep(1)

    def selectMonthAndYear(self):
        # y este metodo de abajo es otra forma y que se haga en el propio método
        # dentro del object de DatePicker
        while self.getCalendarMonth() != "June":
            self.nextMonthAndYear()
            time.sleep(1)
        time.sleep(2)
        print("Month Selected " + self.getCalendarMonth())
        print("Year Selected " + self.getCalendarYear())


    def getallDateSelected(self):
        return self.driver.find_element(*DatePickerLocators.calendarField).get_attribute('value')

    def chooseMonthDayAndYear(self, month, year, day):
        acy = self.driver.find_element(*DatePickerLocators.calendarYear).text
        acm = self.driver.find_element(*DatePickerLocators.calendarMonth).text
        while acy != year:
            self.driver.find_element(*DatePickerLocators.nextMonthYear).click()
            acy = self.driver.find_element(*DatePickerLocators.calendarYear).text
            time.sleep(1)
        while acm != month:
            self.driver.find_element(*DatePickerLocators.nextMonthYear).click()
            acm = self.driver.find_element(*DatePickerLocators.calendarMonth).text
            time.sleep(1)
        if month == "February" and day >= "29":
            print("Wrong Date " + month + " - " + day + " Does not exist")
            return 0
        self.driver.find_element(By.XPATH, "//a[contains(text(),'" + str(day) + "')]").click()
        return 1
