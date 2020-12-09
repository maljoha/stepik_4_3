from selenium.webdriver.common.by import By


class BasePageLocators():
    """Базовые локаторы всех страниц"""

    # ссылки на страницу авторизации: корректная и некорректная
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    # заголовоек открытой страницы
    NAME_PAGE = (By.CSS_SELECTOR, "div.page-header.action>h1")

    # кнопка для перехода в корзину
    BASKET_BTN = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")

    # блок для размещений контента на странице
    PAGE_CONTENT_BLOCK = (By.CSS_SELECTOR, "div.container-fluid.page div.page_inner")

    # икронка юзера для проверки того, что пользователь залогинен
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    """Локаторы страницы корзины"""

    # товары в корзине
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")

    # строка, в которй ожидается надпись "Ваша корзина пуста"
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner>p")

    # ссылка "Продолжить покупки"
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "div#content_inner>p>a")


class LoginPageLocators():
    """Локаторы старницы регистрации нового юзера"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.btn[name='registration_submit']")


class ProductPageLocators():
    """Локаторы страницы товара"""

    # блок с сообщением
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert-success")

    # название и цена продукта в блоке с сообщением
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alertinner strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong")

    # название и цена продукта на странице товара
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

    # кнопка добавления товара в корзину
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
