from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.should_be_add_to_basket_form()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is NOT shown"

    def should_be_add_to_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), \
            "Add to basket form is NOT shown"

    def product_should_be_in_stock(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_AVAILABILITY), \
            "Product NOT in stock"

    def success_message_after_product_added_to_the_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUSSESS_MESSAGE), \
            "Success message is NOT shown"

    def price_in_basket_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == price_in_basket, f"Product price and price in basket are different! Product price == {product_price}, price in basket == {price_in_basket}"