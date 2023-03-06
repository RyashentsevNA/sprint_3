import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import RandomRegistration
from  locators import Locators

class TestRegistration:
    def test_random_registration(self,driver):
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.registration).click()
        driver.find_element(*Locators.name).send_keys(RandomRegistration.name())
        driver.find_element(*Locators.email).send_keys(RandomRegistration.mail())
        driver.find_element(*Locators.password).send_keys(RandomRegistration.password())
        driver.find_element(*Locators.reg_now).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.log_into))
        title=driver.find_element(*Locators.log_into).text
        assert title == 'Зарегистрироваться'


    def test_registration_incorrect_password(self,driver):
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.registration).click()
        driver.find_element(*Locators.name).send_keys(RandomRegistration.name())
        driver.find_element(*Locators.email).send_keys(RandomRegistration.mail())
        driver.find_element(*Locators.password).send_keys(RandomRegistration.wrong_password())
        driver.find_element(*Locators.reg_now).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.incorrect_password))
        password=driver.find_element(*Locators.incorrect_password).text
        assert password == 'Некорректный пароль'