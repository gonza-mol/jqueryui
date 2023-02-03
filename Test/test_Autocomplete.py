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
from POM.AutocompletePage import AutocompletePage

@pytest.mark.usefixtures("test_setup")
class TestAutocomplete(BaseClass):

    def test_Autocomplete(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickAutocompleteLink()
        time.sleep(2)
        ac = AutocompletePage(driver)
        driver.switch_to.frame(0)
        time.sleep(2)
        ac.writeLanguageSearched("ja")
        time.sleep(2)
        ac.selectJavaLanguage()
        time.sleep(2)


