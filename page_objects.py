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
    enter_reg_form = (By.LINK_TEXT, 'Войти')
    recover_password = (By.LINK_TEXT, 'Восстановить пароль')
    profil = (By.LINK_TEXT, 'Профиль')
    constructor = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')
    burger = (By.XPATH, '//*[@class="text text_type_main-large mb-5 mt-10"]')
    logo_burger = (By.CSS_SELECTOR, "div.App_App__aOmNj header.AppHeader_header__X9aJA.pb-4.pt-4:nth-child(1) nav.AppHeader_header__nav__g5hnF div.AppHeader_header__logo__2D0X2 a:nth-child(1) > svg:nth-child(1)")
    exit_btn = (By.XPATH, "//*[@id='root']//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    bread = (By.XPATH, "//div/span[text()='Булки']")
    search_bread = (By.XPATH, "//*/p[text()[contains(.,'Флюоресцентная булка R2-D3')]]")
    sauce = (By.XPATH, "//div/span[text()='Соусы']")
    search_souse = (By.XPATH, "//*/p[text()[contains(.,'Соус традиционный галактический')]]")
    filling = (By.XPATH, "//div/span[text()='Начинки']")
    search_filling = (By.XPATH, "//*/p[text()[contains(.,'Мясо бессмертных моллюсков Protostomia')]]")