from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.GO_TO_CHECKOUT_BUTTON), 'Basket is not empty!'

    def is_basket_empty_message_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), 'Basket empty message is not displayed'
