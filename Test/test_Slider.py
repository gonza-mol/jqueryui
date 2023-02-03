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
from POM.SliderPage import SliderPage


@pytest.mark.usefixtures("test_setup")
class TestSlider(BaseClass):

    def test_Slider(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickSliderLink()
        sp = SliderPage(driver)
        driver.switch_to_default_content()
        sp.selectModalOption()
        time.sleep(2)
        driver.switch_to.frame(0)
        sp.pickAndMoveSlider("44")
        time.sleep(2)
        print("\nEl valor mostrado en el slider es: "+str(sp.getValueOverSlider().text))
        value = sp.getValueOverSlider().text
        assert value in sp.getValueOverSlider().get_attribute('style')
        time.sleep(2)




