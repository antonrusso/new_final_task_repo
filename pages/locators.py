from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "[name=login-username]")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name=login-password]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name=login_submit]")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, "[class=icon-ok]")
    SUSSESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[class=price_color]")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
