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
from POM.TooltipPage import ToolTipPage


@pytest.mark.usefixtures("test_setup")
class TestTooltip(BaseClass):

    def test_Tooltip(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickTooltipLink()
        driver.execute_script("window.scrollTo(0, 200)")
        tt = ToolTipPage(driver)
        driver.switch_to.frame(0)
        tt.clickYourAgeTxtField()
        time.sleep(1)
        print("\nPrimer Banner -->"+tt.getBanner())
        assert tt.getBanner() == "We ask for your age only for statistical purposes."
        time.sleep(2)
        tt.clickFirstTooltip()
        print("Segundo Banner -->"+tt.getBanner())
        assert tt.getBanner() == "That's what this widget is"
        time.sleep(2)
        tt.clickSecondTooltip()
        time.sleep(2)
        print("Tercer Banner -->"+tt.getBanner())
        assert tt.getBanner() == "ThemeRoller: jQuery UI's theme builder application"
        time.sleep(2)



