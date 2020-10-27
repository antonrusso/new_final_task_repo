from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket_has_no_product(self):
        assert self.is_element_present(*BasketPageLocators.YOUR_BASKET_IS_EMPTY_MESSAGE), "Basket is NOT empty"

    def message_that_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket should BE EMPTY"


