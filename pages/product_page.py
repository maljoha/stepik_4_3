import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def open_product_page(self):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        self.open(url)

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        button.click()
        time.sleep(1)

    def check_success_message(self):
        product_name_in_message = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)[0].text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == product_name_in_message, "Название товара не совпадает с сообщением об добавлении в корзину"

    def check_price(self):
        price_product = self.browser.find_elements(*ProductPageLocators.PRODUCT_PRICE)[0].text
        price_in_message = self.browser.find_elements(*ProductPageLocators.PRICE_IN_MESSAGE)[0].text
        assert price_in_message == price_product, "Стоимость корзины не совпадает с ценой товара"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Есть успешное сообщение. Сообщения быть не должно"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Успешное сообщение не исчезает. Сообщение должно исчезать"
