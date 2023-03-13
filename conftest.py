import random
from random import choices, sample
import string
from test_cases import *
import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators




class RandomRegistration:
    def name():
        random_letters = ''.join(random.choices(string.ascii_letters, k=10))
        test_name = (str(random_letters) + "_ТестовыйПользователь")
        return test_name

    def mail():
        random_letters = ''.join(random.choices(string.ascii_letters,k=10))
        email=(str(random_letters)+"@yandex.ru")
        return email

    def password():
        random_pas = ''.join(random.choices(string.ascii_letters,k=7))
        return random_pas

    def wrong_password():
        random_pas = ''.join(random.choices(string.ascii_letters, k=5))
        return random_pas

class TrueRegistration:
    def name():
        test_name = 'Никита'
        return test_name

    def mail():
        email = 'Ryashentsev_06@yandex.ru'
        return email

    def password():
        pas = '1234567'
        return pas

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()

