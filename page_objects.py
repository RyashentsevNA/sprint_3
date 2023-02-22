from selenium.webdriver.common.by import By

class Locators():
    registration = (By.LINK_TEXT, 'Зарегистрироваться')
    log_in = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]')
    name = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]')
    email = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]')
    password = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]')
    reg_now = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    log_into = (By.LINK_TEXT, 'Зарегистрироваться')