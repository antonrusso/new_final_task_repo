from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_form()
    page.should_be_add_to_basket_button()
    page.product_should_be_in_stock()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
