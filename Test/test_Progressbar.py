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
from POM.ProgressbarPage import ProgressbarPage


@pytest.mark.usefixtures("test_setup")
class TestProgressbar(BaseClass):

    def test_Progressbar(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickProgressbarLink()
        pb = ProgressbarPage(driver)
        driver.switch_to_default_content()
        pb.selectModalOption()
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        pb.selectBtnStartDownload()
        status = pb.verifyFileDownload()
        assert status == "Complete!"
        print("Se ha realizado la descarga completa")
        pb.closePopUpDownload()
        time.sleep(2)

