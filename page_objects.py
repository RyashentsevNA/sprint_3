from selenium.webdriver.common.by import By

class Locators():
    registration = (By.LINK_TEXT, 'Зарегистрироваться')
    log_in = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]')
    name = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]')
    email = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]')
    password = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]')
    reg_now = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    log_into = (By.LINK_TEXT, 'Зарегистрироваться')
    incorrect_password = (By.XPATH, '//*[@class ="input__error text_type_main-default"]')
    mail_login = (By.XPATH, "//*[@name = 'name']")
    password_login = (By.XPATH, "//*[@name='Пароль']")
    enter = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[1]")
    place_an_order = (By.XPATH, "//*[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    personal_account = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")

