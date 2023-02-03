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
from POM.TabsPage import TabsPage


@pytest.mark.usefixtures("test_setup")
class TestTabs2(BaseClass):

    def test_Tabs2(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickTabsLink()
        driver.execute_script("window.scrollTo(0, 300)")
        tp = TabsPage(driver)
        driver.switch_to_default_content()
        tp.selectModalOption1()
        time.sleep(1)
        driver.switch_to.frame(0)
        time.sleep(2)
        tp.openTab()
        time.sleep(2)
        tp.collapseTab()
        time.sleep(2)





