import time

from _pytest import mark
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import TrueRegistration
import pytest

class Test_constructor_bar:
    def test_constructor_bar(self, driver): #переходы к разделам:«Булки»,«Соусы»,«Начинки».
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.logo_burger).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.burger))
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.sauce)).click()
        souse = driver.find_element(*Locators.search_souse).text
        assert souse == 'Соус традиционный галактический'


    def test_constructor_bar_1(self, driver): #переходы к разделам:«Булки»,«Соусы»,«Начинки».
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.logo_burger).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.burger))
        bread = driver.find_element(*Locators.search_bread).text
        assert bread == 'Флюоресцентная булка R2-D3'


    def test_constructor_bar_2(self, driver):  # переходы к разделам:«Булки»,«Соусы»,«Начинки».
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.logo_burger).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.burger))
        driver.find_element(*Locators.filling).click()
        filling = driver.find_element(*Locators.search_filling).text
        assert filling == 'Мясо бессмертных моллюсков Protostomia'