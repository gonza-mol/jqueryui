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
from POM.DroppablePage import DroppablePage

@pytest.mark.usefixtures("test_setup")
class TestDroppable(BaseClass):

    def test_Droppable(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDroppaleLink()
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        dp = DroppablePage(driver)
        dp.clickAndDrop()
        time.sleep(2)
        assert "Dropped!" == dp.getTitle()
        time.sleep(2)
        print("Se pudo hacer correctamente el drag and drop")
