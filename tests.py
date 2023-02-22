import time
import random
import pytest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import dfs
from page_objects import Locators
from dfs import RandomRegistration
from dfs import TrueRegistration
from dfs import Login
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)

class TestRegistration:
    def test_random_registration(self):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.registration).click()
        driver.find_element(*Locators.name).send_keys(RandomRegistration.name())
        driver.find_element(*Locators.email).send_keys(RandomRegistration.mail())
        driver.find_element(*Locators.password).send_keys(RandomRegistration.password())
        driver.find_element(*Locators.reg_now).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.log_into))
        title=driver.find_element(*Locators.log_into).text
        assert title == 'Зарегистрироваться'
        driver.quite()

    def test_registration_incorrect_password(self):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.registration).click()
        driver.find_element(*Locators.name).send_keys(RandomRegistration.name())
        driver.find_element(*Locators.email).send_keys(RandomRegistration.mail())
        driver.find_element(*Locators.password).send_keys(RandomRegistration.wrong_password())
        driver.find_element(*Locators.reg_now).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.incorrect_password))
        password=driver.find_element(*Locators.incorrect_password).text
        assert password == 'Некорректный пароль'
        driver.quite()


class TestEntrance:
    def test_log_in_to_account_enter(self): #тест входа через "Войти в аккаунт"
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'
        driver.quite()


    def test_log_in_to_account(self): #тест входа через "Личный кабинет"
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'
        driver.quite()
