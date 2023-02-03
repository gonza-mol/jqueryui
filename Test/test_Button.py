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
from POM.ButtonPage import ButtonPage

@pytest.mark.usefixtures("test_setup")
class TestButton(BaseClass):

    def test_Button(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickButtonLink()
        time.sleep(2)
        bp = ButtonPage(driver)
        driver.switch_to.frame(0)
        bp.selectFirstButton()
        bp.selectSecondButton()
        bp.selectThirdButton()
        time.sleep(2)


