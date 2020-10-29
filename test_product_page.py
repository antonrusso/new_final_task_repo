from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, self.link)
        page.open()
        email = page.generate_fake_email()
        password = page.generate_fake_password()
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.success_message_should_have_correct_product_name()
        page.success_message_after_product_added_to_the_basket()
        page.price_in_basket_equal_product_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):  # (browser, link)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_have_correct_product_name()
    page.success_message_after_product_added_to_the_basket()
    page.price_in_basket_equal_product_price()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_the_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket_has_no_product()
    basket_page.message_that_basket_is_empty()
