import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

main_page_link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, main_page_link)
        # открываем страницу
        page.open()
        # выполняем метод страницы — переходим на страницу логина
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_page_link)
    # Гость открывает главную страницу
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page_by_button()
    basket = BasketPage(browser, main_page_link)
    # Ожидаем, что в корзине нет товаров
    basket.is_basket_empty()
    # Ожидаем, что есть текст о том что корзина пуста
    basket.should_be_basket_empty_message()
