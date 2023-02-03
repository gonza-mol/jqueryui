import time
import pytest
import unittest
import sys
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.SortablePage import SortablePage

@pytest.mark.usefixtures("test_setup")
class TestSortable(BaseClass):

    def test_Sortable(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickSortableLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        driver.switch_to.frame(0)
        sp = SortablePage(driver)
        cant = len(sp.getListItems())
        print("La cantidad de items listados es: " + str(cant))
        sp.printAllListItems()
        time.sleep(2)
        sp.clickDraggableItem7()
        time.sleep(2)
        sp.printUpdatedListItems()
        time.sleep(2)





