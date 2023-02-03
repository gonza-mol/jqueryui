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
class TestDatePicker(BaseClass):

    def test_DatePicker(self):
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
        #Con el metodo de abajo obtengo mes y año
        #data = dp.getCalendarMonthYear()
        #Con esta sentencia de abajo, lo que hago es al texto de mes y año que vienen
        #juntos a través de un espacio le digo que imprima solo uno o el otro, es decir el año o el mes
        #dependiendo la posición del texto que necesito
        #print(data.split(" ")[1])
        time.sleep(2)
        #la de abajo con el while es una forma de buscar el año
        #while dp.getCalendarYear() != "2024":
        #    dp.nextMonthAndYear()
        #    time.sleep(1)
        dp.selectYear("2023")
        dp.selectMonthAndYear()
        dp.selectDay(22)
        time.sleep(2)
        print("Now the date selected and visualized in the text box is: "+dp.getallDateSelected())
        time.sleep(2)




