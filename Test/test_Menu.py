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
from POM.MenuPage import MenuPage


@pytest.mark.usefixtures("test_setup")
class TestMenu(BaseClass):

    def test_Menu(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickMenuLink()
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        mp = MenuPage(driver)
        items = mp.getAllItems()
        mp.selectHover(items)
        time.sleep(2)

