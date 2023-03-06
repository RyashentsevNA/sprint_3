from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import TrueRegistration


class Test_personal_account:
    def test_enter_to_personal_account(self, driver): #переход по клику на «Личный кабинет».
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
        driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
        driver.find_element(*Locators.enter).click()
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(Locators.profil))
        profil = driver.find_element(*Locators.profil).text
        assert profil == 'Профиль'