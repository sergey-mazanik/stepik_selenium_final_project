from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, f"expected 'login' to be substring of '{self.url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is absent'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is absent'

    def register_new_user(self, email, password):
        login_email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        login_email_input.send_keys(email)
        register_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1_INPUT)
        register_password_input.send_keys(password)
        register_confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2_INPUT)
        register_confirm_password_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
