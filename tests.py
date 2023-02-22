import time
import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import dfs
from page_objects import Locators
from dfs import Registration


driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://stellarburgers.nomoreparties.site")
driver.find_element(*Locators.log_in).click()
driver.find_element(*Locators.registration).click()
driver.find_element(*Locators.name).send_keys(Registration.name())
driver.find_element(*Locators.email).send_keys(Registration.mail())
driver.find_element(*Locators.password).send_keys(Registration.password())
driver.find_element(*Locators.reg_now).click()
# e=driver.find_element(*Locators.log_into).until
e=WebDriverWait(driver, 60).until(expected_conditions.text_to_be_present_in_element_value(*Locators.log_into))
assert e=='Зарегистрироваться'
