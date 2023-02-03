import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.CheckboxRadioPage import CheckboxRadioPage

@pytest.mark.usefixtures("test_setup")
class TestCheckboxRadio(BaseClass):

    def test_CheckboxRadio(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickCheckboxRadioLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        cb = CheckboxRadioPage(driver)
        driver.switch_to.frame(0)
        time.sleep(2)
        cb.selectAllRadioButton()
        time.sleep(2)
        cb.selectAllCheckbox()
        time.sleep(2)
        if "ui-state-checked" in cb.checkIfSecondIsUnselected():
            cb.uncheckSecondCheckbox()
        time.sleep(2)
        if "ui-state-checked" in cb.checkIfThirdIsUnselected():
            cb.uncheckThirdCheckbox()
        time.sleep(2)
        cb.selectLastTwoCheckboxBed()
        time.sleep(2)


