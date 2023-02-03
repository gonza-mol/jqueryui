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
from POM.SpinnerPage import SpinnerPage


@pytest.mark.usefixtures("test_setup")
class TestSpinner(BaseClass):

    def test_Spinner(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickSpinnerLink()
        driver.execute_script("window.scrollTo(0, 300)")
        sp = SpinnerPage(driver)
        time.sleep(2)
        driver.switch_to.frame(0)
        sp.increaseNumber(3)
        time.sleep(2)
        print("\nEl valor mostrado en el textField es: "+str(sp.getActualValueTextField()))
        time.sleep(2)
        sp.enabledAndDisabledTextBox()
        time.sleep(2)
        assert sp.getStatusTextField() == "true"
        time.sleep(2)
        sp.enabledAndDisabledTextBox()
        time.sleep(2)
        assert str(sp.getStatusTextField()) == "None"
        time.sleep(2)
        value = str(sp.seeActualStatusWithToggle())
        assert value == "True"
        time.sleep(2)
        sp.disabledAndEnabledToogle()
        value1 = str(sp.seeActualStatusWithOutToggle())
        assert value1 == "True"
        time.sleep(2)
        sp.disabledAndEnabledToogle()
        time.sleep(2)
        sp.clickGetValueBtn()
        sp.handleGetValue()
        lastvalue = str(sp.clickSetValueBtn())
        assert lastvalue == "5"
        print("El último número mostrado en el text fiels es 5")
        time.sleep(2)




