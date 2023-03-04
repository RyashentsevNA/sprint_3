import time

from _pytest import mark
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects import Locators
from conftest import TrueRegistration
import pytest

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)


class Test_constructor_bar:
    def test_constructor_bar(self): #переходы к разделам:«Булки»,«Соусы»,«Начинки».
        driver.get("https://stellarburgers.nomoreparties.site")
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
        driver.find_element(*Locators.bread).click()
        bread = driver.find_element(*Locators.search_bread).text
        assert bread == 'Флюоресцентная булка R2-D3'
        driver.find_element(*Locators.filling).click()
        filling = driver.find_element(*Locators.search_filling).text
        assert filling == 'Мясо бессмертных моллюсков Protostomia'
        driver.quit()
