from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    LOGIN_EMAIL_INPUT = (By.XPATH, '//input[@id="id_login-username"]')
    LOGIN_PASSWORD_INPUT = (By.XPATH, '//input[@id="id_login-password"]')
    REGISTER_EMAIL_INPUT = (By.XPATH, '//input[@id="id_registration-email"]')
    REGISTER_PASSWORD1_INPUT = (By.XPATH, '//input[@id="id_registration-password1"]')
    REGISTER_PASSWORD2_INPUT = (By.XPATH, '//input[@id="id_registration-password2"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
