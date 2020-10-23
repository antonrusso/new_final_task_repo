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