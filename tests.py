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
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.mail_login))
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'
        driver.quite()

    def test_log_in_from_registration(self): #тест входа через кнопку в форме регистрации
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.registration).click()
        driver.find_element(*Locators.enter_reg_form).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'
        driver.quite()

    def test_log_in_from_recover_password(self): #тест входа через форму восстановления пароля
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.log_in).click()
        driver.find_element(*Locators.recover_password).click()
        driver.find_element(*Locators.enter_reg_form).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.place_an_order))
        order_btn = driver.find_element(*Locators.place_an_order).text
        assert order_btn == 'Оформить заказ'
        driver.quite()

class Test_personal_account:
    def test_enter_to_personal_account(self): #переход по клику на «Личный кабинет».
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.profil))
        profil = driver.find_element(*Locators.profil).text
        assert profil == 'Профиль'
        driver.quite()

class Test_from_personal_account_to_the_constructor:
    def test_enter_to_the_constructor_button(self): #Переход из личного кабинета в конструктор по клику на «Конструктор»
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.constructor).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.burger))
        burger = driver.find_element(*Locators.burger).text
        assert burger == 'Соберите бургер'
        driver.quite()

    def test_enter_to_the_constructor_logo(self): #Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers.
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.logo_burger).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.burger))
        burger = driver.find_element(*Locators.burger).text
        assert burger == 'Соберите бургер'
        driver.quite()

class Test_log_out:
    def test_exit_from_personal_account(self): #Выход из личного кабинета
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.exit_btn)).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.log_into))
        burger = driver.find_element(*Locators.log_into).text
        assert burger == 'Зарегистрироваться'
        driver.quite()

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
        # driver.find_element(*Locators.bread).click()
        souse = driver.find_element(*Locators.search_souse).text
        assert souse == 'Соус традиционный галактический'
        driver.find_element(*Locators.bread).click()
        bread = driver.find_element(*Locators.search_bread).text
        assert bread == 'Флюоресцентная булка R2-D3'
        driver.find_element(*Locators.filling).click()
        filling = driver.find_element(*Locators.search_filling).text
        assert filling == 'Мясо бессмертных моллюсков Protostomia'
        driver.quite()