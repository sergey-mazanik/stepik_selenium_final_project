from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, f"expected 'login' to be substring of '{self.url}'"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        # self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is absent'

    def should_be_register_form(self):
        # self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is absent'
