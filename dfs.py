import random
from random import choices, sample
import string
class Registration:
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