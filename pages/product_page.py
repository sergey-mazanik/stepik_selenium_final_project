from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_param_in_url(self, param):
        assert param in self.url, f"expected '{param}' to be substring of '{self.url}'"

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def enter_solve_to_alert(self, solve):
        switch_to_alert = self.browser.switch_to.alert
        switch_to_alert.send_keys(solve)
        switch_to_alert.accept()

    def product_has_been_added_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_ALERT), "Product didn't added to basket"

    def return_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PRODUCT_PAGE)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PRODUCT_PAGE)
        return book_price.text

    def check_product_name(self, book_name):
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT_BASKET)
        assert book_name == product_name_in_alert.text, 'Product in basket is different'

    def check_product_price(self, book_price):
        product_price_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT_BASKET)
        assert book_price == product_price_in_alert.text, "It's wrong price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_ALERT), 'Success message is presented, but should not be'

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_ALERT), 'Success message is not disappeared'
