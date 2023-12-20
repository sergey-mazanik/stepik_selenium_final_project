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


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button')
    PRODUCT_HAS_BEEN_ADDED_ALERT = (By.XPATH, '//div[@class="alertinner "]')
    PRODUCT_NAME_IN_ALERT_BASKET = (By.XPATH, '(//div[@class="alertinner "]/strong)[1]')
    PRODUCT_NAME_ON_PRODUCT_PAGE = (By.XPATH, '//h1')
    PRODUCT_PRICE_IN_ALERT_BASKET = (By.XPATH, '(//p/strong)[2]')
    PRODUCT_PRICE_ON_PRODUCT_PAGE = (By.XPATH, '(//p[@class="price_color"])[1]')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    GO_TO_CHECKOUT_BUTTON = (By.XPATH, '//a[@class="btn btn-lg btn-primary btn-block"]')
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')
