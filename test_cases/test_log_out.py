from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import TrueRegistration

class TestLogOut:
    def test_exit_from_personal_account(self,driver): #Выход из личного кабинета
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.exit_btn)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.log_into))
        burger = driver.find_element(*Locators.log_into).text
        assert burger == 'Зарегистрироваться'