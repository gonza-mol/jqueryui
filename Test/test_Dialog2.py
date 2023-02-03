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
from POM.Dialog import DialogPage


@pytest.mark.usefixtures("test_setup")
class TestDialog2(BaseClass):

    def test_Dialog2(self):
        driver = self.driver
        log = self.get_Logger()
        hp = HomePage(driver)
        hp.clickDialogLink()
        driver.execute_script("window.scrollTo(0, 200)")
        dp = DialogPage(driver)
        dp.selectModalForm()
        time.sleep(2)
        driver.switch_to.frame(0)
        #el comando que está abajo de esta linea es solo para que imprima logs en el archivo logfile que está
        #en la carpeta Data
        log.info("En proceso de ejecución")
        dp.selectBtnCreateNewUser()
        #assert "Create new user" == dp.getTitleFromModal()

        file = open("C:\\Users\\admin\\PycharmProjects\\jqueryui\\Datos\\users.json", "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        users = obj['users']
        #print(users)
        #print(len(users))
        listUsersAdded = []
        for i in range(len(users)):
            name = users[i].get("name")
            email = users[i].get("email")
            password = users[i].get("password")
            dp.AddNewUser(name, email, password)
            time.sleep(2)
            dp.selectCreateAccount()
            time.sleep(2)
            dp.selectBtnCreateNewUser()
            print(Fore.BLUE + "\nAccount Added of " + name)
            listUsersAdded.append(name)
        print("Usuarios recientemente agregados")
        print(listUsersAdded)
        users = dp.getAllUsers()
        listusersexisting = []
        for user in users:
            listusersexisting.append(user.text)
        print("Usuarios existentes en la tabla")
        print(listusersexisting)
        #Y esta de abajo es otra forma de obtener la diferencia entre dos tablas dependiendo como se ponga
        print("El usuario prexistente en la tabla general es: "+str(set(listusersexisting) - set(listUsersAdded)))
        #print("Los nuevos usuarios agregados en la tabla general son: " + str(set(listUsersAdded) - set(listusersexisting)))
        #aux = set(listUsersAdded) - set(listusersexisting)
        #print(aux)
        #El metodo de abajo lo que hace es permitir recorrer dos listas y compararlas
        #Cada elemento de una tabla con todos los elementos de la otra tabla y ver si lo
        #encuentra o no, y asi sigue con el siguiente
        # n = 0
        # b = 0
        # for userv in listusersexisting:
        #     for usern in listUsersAdded:
        #         if usern == userv:
        #             print("usuario esperado, es de los nuevos " + usern)
        #             b = 1
        #         else:
        #             if n == 1:
        #                 print("Usuario preexistente " + userv)
        #                 n = 0
        #             else:
        #                 if b == 1:
        #                     n = 0
        #                 else:
        #                     n = n+1
        # print(b)
        # print(n)