import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link_with_promo_newyear = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_with_promo_2019 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_without_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_with_promo_offern = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации;
        page = LoginPage(browser, login_link)
        page.open()
        # зарегистрировать нового пользователя;
        user_password = str(time.time())
        email = f"{user_password}@mailforspam.com"
        page.register_new_user(email, user_password)
        # проверить, что пользователь залогинен.
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_with_promo_offern)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_success_message()
        page.check_price()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_without_promo)
        # Открываем страницу товара
        page.open()
        # Добавляем товар в корзину
        page.add_to_basket()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()


class TestGuestAddToBasketFromProductPage():
    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_success_message()
        page.check_price()


    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_without_promo)
        # Открываем страницу товара
        page.open()
        # Добавляем товар в корзину
        page.add_to_basket()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()


    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_without_promo)
        # Открываем страницу товара
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_without_promo)
        # Открываем страницу товара
        page.open()
        # Добавляем товар в корзину
        page.add_to_basket()
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        page.should_dissapear_of_success_message()


    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link_without_promo)
        page.open()
        page.should_be_login_link()


    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_without_promo)
        page.open()
        page.go_to_login_page()


    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Гость открывает страницу товара
        page = BasketPage(browser, link_without_promo)
        page.open()
        # Переходит в корзину по кнопке в шапке
        page.go_to_basket_page_by_button()
        # Ожидаем, что в корзине нет товаров
        page.is_basket_empty()
        # Ожидаем, что есть текст о том что корзина пуста
        page.should_be_basket_empty_message()
