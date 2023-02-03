import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.ColorAnimationPage import ColorAnimationPage

@pytest.mark.usefixtures("test_setup")
class TestColorAnimation(BaseClass):

    def test_ColorAnimation(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.colorAnimationLink()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        ca = ColorAnimationPage(driver)
        driver.switch_to.frame(0)
        time.sleep(2)
        assert "240px" == ca.getWidthOfBoxArea()
        assert "rgba(255, 255, 255, 1)" == ca.getBackgroundColorOfBoxArea()
        print("El tamaño de la ventana es: " + ca.getWidthOfBoxArea())
        print("El color de fondo del box es Blanco")
        ca.selectBtnToggleEffect()
        time.sleep(2)
        assert "500px" == ca.getWidthOfBoxArea()
        assert "rgba(170, 0, 0, 1)" == ca.getBackgroundColorOfBoxArea()
        print("Ahora el tamaño de la ventana es: "+ca.getWidthOfBoxArea())
        print("Y el color de fondo del box es Rojo")
        time.sleep(2)


