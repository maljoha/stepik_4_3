import math

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page_by_button(self):
        # кликаем по кнопке "Посмотреть корзину"
        button = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        button.click()
        # ждём когда загрузится наименование страницы
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(BasePageLocators.NAME_PAGE))
        # определяем текущий язык страницы
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        # словарик наименоваиний корзины на разных языках
        basket_names = {"ar": "سلة المشتريات",
                        "ca": "Cistella",
                        "cs": "Košík",
                        "da": "Indkøbskurv",
                        "de": "Warenkorb",
                        "en": "Basket",
                        "el": "Καλάθι",
                        "es": "Carrito",
                        "fi": "Korisi",
                        "fr": "Panier",
                        "it": "Carrello",
                        "ko": "장바구니",
                        "nl": "Winkelmand",
                        "pl": "Koszyk",
                        "pt": "Carrinho",
                        "pt-br": "Cesta",
                        "ro": "Cosul",
                        "ru": "Корзина",
                        "sk": "Košík",
                        "uk": "Кошик",
                        "zh-cn": "Basket",
                        }
        # ждём когда наименование страницы будет "Корзина" - значит страница корзины загрузилась, ура!)
        WebDriverWait(self.browser, 10).until(
            lambda driver: self.browser.find_element(*BasePageLocators.NAME_PAGE).text == basket_names[language])

    def should_be_authorized_user(self):
        """Проверка того, что пользователь залогинен"""
        assert self.is_element_present(
            *BasePageLocators.USER_ICON), "Иконка пользвателя не отображается. Возможно, пользовтаель не авторизоан"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Не найдена ссылка на страницу авторизации"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Отсутствует второй алерт!")

    def is_element_present(self, how, what, timeout=4):
        """метод для проверки на наличие элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        """метод для проверки на отсутствия элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """метод для проверки на исчезнования элемента со страницы"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
