from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Корзина не пуста!"

    def should_be_basket_empty_message(self):
        # определяем текущий язык страницы для определения ожидаемого текста
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        # словарик ожидаемого результата на разных языках
        expected_text = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        # находим фактический текст, отрезая от него второе предложение "Продолжить покупки"
        excess_text = self.browser.find_element(*BasketPageLocators.CONTINUE_SHOPPING_LINK).text
        all_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        fact_text = all_text.replace(excess_text, "").strip()
        # выполняем проверку
        assert fact_text == expected_text[language], "Не найдена надпись о том, что корзина пуста!"
