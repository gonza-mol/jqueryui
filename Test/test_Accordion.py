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
from POM.AccordionPage import AccordionPage

@pytest.mark.usefixtures("test_setup")
class TestAccordion(BaseClass):

    def test_Accordion(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickAccordionLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        ap = AccordionPage(driver)
        ap.selectCollapseOption()
        time.sleep(2)
        driver.switch_to.frame(0)
        assert ap.checkItem1IsSelected() == "true"
        ap.contractItem1()
        assert ap.checkItem1IsSelected() == "false"
        time.sleep(2)
        ap.selectItem2()
        time.sleep(2)
        assert "Sed non urna" in ap.getTextOfItem2()
        print("El texto contenido en el item 2 es:")
        print(ap.getTextOfItem2())
        time.sleep(2)


