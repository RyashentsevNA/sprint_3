import random
from random import choices, sample
import string
from tests import *
from page_objects import *
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

# class Login:
#     def true_log_in(self):
#         driver.find_element(*Locators.mail_login).send_keys(TrueRegistration.mail())
#         driver.find_element(*Locators.password_login).send_keys(TrueRegistration.password())
#         driver.find_element(*Locators.enter).click()