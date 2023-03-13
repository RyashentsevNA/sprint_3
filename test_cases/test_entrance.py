import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import TrueRegistration





class TestEntrance:
    def test_log_in_to_account_enter(self, driver): #тест входа через "Войти в аккаунт"
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'



    def test_log_in_to_account(self, driver): #тест входа через "Личный кабинет"
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.mail_login))
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'



    def test_log_in_from_registration(self, driver): #тест входа через кнопку в форме регистрации
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.registration).click()
        driver.find_element(*Locators.enter_reg_form).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'


    def test_log_in_from_recover_password(self, driver): #тест входа через форму восстановления пароля
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.recover_password).click()
        driver.find_element(*Locators.enter_reg_form).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'