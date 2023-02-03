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
from POM.SelectablePage import SelectablePage

@pytest.mark.usefixtures("test_setup")
class TestSelectable(BaseClass):

    def test_Selectable(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickSelectableLink()
        time.sleep(2)
        driver.switch_to.frame(0)
        sp = SelectablePage(driver)
        cant = len(sp.getListItems())
        print("La cantidad de items listados es: "+str(cant))
        aux = sp.getListItems()
        n = 1
        for i in aux:
            sp.selectEachItems(n)
            assert 'rgba(243, 152, 20, 1)' == i.value_of_css_property('background-color')
            n = n+1
            time.sleep(1)
        sp.addNewItem()
        assert 'rgba(243, 152, 20, 1)' == self.driver.find_element(By.CSS_SELECTOR, "#selectable>li:nth-child(2)").value_of_css_property('background-color')
        assert 'rgba(243, 152, 20, 1)' == self.driver.find_element(By.CSS_SELECTOR, "#selectable>li:nth-child(7)").value_of_css_property('background-color')
        time.sleep(2)



