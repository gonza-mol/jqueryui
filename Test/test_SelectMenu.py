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
from POM.SelectMenuPage import SelectMenuPage


@pytest.mark.usefixtures("test_setup")
class TestSelectMenu(BaseClass):

    def test_SelectMenu(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickSelectMenuLink()
        driver.execute_script("window.scrollTo(0, 300)")
        sm = SelectMenuPage(driver)
        driver.switch_to_default_content()
        sm.selectModalOption()
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        sm.selectRadiusDropdown()
        time.sleep(2)
        sm.selectRadiusValue("100px")
        time.sleep(2)
        sm.selectColorDropdown()
        time.sleep(2)
        sm.selectCircleColor("Blue")
        time.sleep(2)
        assert sm.getActualRadiusValue() == "100px" and sm.getActualColorValue() == "Blue" and "100px" in sm.getwidthAndHeightCircle() and "blue" in sm.getwidthAndHeightCircle()
        time.sleep(2)



