import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.DatePickerPage import DatePickerPage

@pytest.mark.usefixtures("test_setup")
class TestDatePicker2(BaseClass):

    def test_DatePicker2(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDatePickerLink()
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        dp = DatePickerPage(driver)
        dp.clickCalendarField()
        time.sleep(2)
        print("\nCurrent Month "+dp.getCalendarMonth())
        print("Current Year "+dp.getCalendarYear())
        time.sleep(2)
        flag = dp.chooseMonthDayAndYear("May", "2023", "30")
        print("Month Selected " + dp.getCalendarMonth())
        print("Year Selected " + dp.getCalendarYear())
        if flag == 1:
            print("Now the date selected and visualized in the text box is: "+dp.getallDateSelected())
        else:
            print("Wrong Date")
        time.sleep(2)




