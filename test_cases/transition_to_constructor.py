import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import TrueRegistration

class Test_from_personal_account_to_the_constructor:
    def test_enter_to_the_constructor_button(self,driver): #Переход из личного кабинета в конструктор по клику на «Конструктор»
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.constructor).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.burger))
        burger = driver.find_element(*Locators.burger).text
        assert burger == 'Соберите бургер'

    def test_enter_to_the_constructor_logo(self,driver): #Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers.
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.logo_burger).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.burger))
        burger = driver.find_element(*Locators.burger).text
        assert burger == 'Соберите бургер'