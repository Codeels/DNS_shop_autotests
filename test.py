import pytest
import allure

from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.comparison_page import ComparisonPage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage

login = 'gamag25045@ekcsoft.com'
password = 'gamag25045'
telephone_number_checkout = '1111111111'
sms_code_checkout = '111111'

# данные для фильтрации
cores = [1, 1, 1]
price = [1500, 15000]
brand = [0, 1]
internal_graphics = [1, 0]
ram = [1, 1]


@allure.title("Тест 1")
@allure.description('Тест 1')
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_1(driver):
    # авторизация
    mp = MainPage(driver)
    mp.log_in(login, password, main=True)

    # очистка корзины и страницы сравнения от товаров
    mp.clear_cart_and_comparison(driver, CartPage, ComparisonPage)
    mp = MainPage(driver)

    # переход на страницу с товарами
    mp.go_to_cpus()
    catalog = CatalogPage(driver)

    # фильтрация по разным параметрам
    catalog.set_stock()
    catalog.set_price(*price)
    catalog.set_brand(*brand)
    catalog.set_cores(*cores)
    catalog.set_internal_graphics(*internal_graphics)
    catalog.set_ram(*ram)
    catalog.click_button_submit()

    # сравнение атрибутов товара из каталога и корзины
    catalog = CatalogPage(driver)
    catalog.get_product_info_and_check_catalog_cart()

    # оформление товара. в конце проверка на неправильный код из смс
    cart = CartPage(driver)
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    checkout.input_data_and_code(telephone_number_checkout, login, sms_code_checkout)


@allure.title("Тест 2")
@allure.description('Тест 2')
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_2(driver):
    mp = MainPage(driver)

    # переход на страницу с товарами
    mp.go_to_cpus()
    catalog = CatalogPage(driver)

    # фильтрация товаров по параметрам
    catalog.set_stock()
    catalog.set_price(*price)
    catalog.set_brand(*brand)
    catalog.set_cores(*cores)
    catalog.set_internal_graphics(*internal_graphics)
    catalog.set_ram(*ram)
    catalog.click_button_submit()

    # сравнение атрибутов товара в каталоге и в корзине
    catalog = CatalogPage(driver)
    catalog.get_product_info_and_check_catalog_cart()

    # заполнение данных на странице оформления заказа.
    # на этой странице происходит авторизация. в конце проверка на неправильный код из смс
    cart = CartPage(driver)
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    mp.log_in(login, password, checkout=True)
    checkout.input_data_and_code(telephone_number_checkout, login, sms_code_checkout)


@allure.title("Тест 3")
@allure.description('Тест 3')
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_3(driver):
    # авторизация
    mp = MainPage(driver)
    mp.log_in(login, password, main=True)

    # очистка корзины и страницы сравнения от товаров
    mp.clear_cart_and_comparison(driver, CartPage, ComparisonPage)

    # переход на страницу с товарами
    mp = MainPage(driver)
    mp.go_to_cpus()
    catalog = CatalogPage(driver)

    # фильтрация товаров по параметрам
    catalog.set_stock()
    catalog.set_price(*price)
    catalog.set_brand(*brand)
    catalog.set_cores(*cores)
    catalog.set_internal_graphics(*internal_graphics)
    catalog.set_ram(*ram)
    catalog.click_button_submit()

    # сравнение параметров товаров из каталога и страницы сравнения
    catalog.get_product_info_and_check_catalog_compare()

    # выбор товара подешевле на странице сравнения товаров
    compare = ComparisonPage(driver)
    compare.choose_best_product()

    # переход в корзину
    compare.go_to_cart()
    cart = CartPage(driver)

    # заполнение данных на странице оформления заказа. в конце проверка на неправильный код из смс
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    checkout.input_data_and_code(telephone_number_checkout, login, sms_code_checkout)


@allure.title("Тест 4")
@allure.description('Тест 4')
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_4(driver):
    # авторизация
    mp = MainPage(driver)
    mp.log_in(login, password, main=True)

    # очистка корзины и сравнения
    mp.clear_cart_and_comparison(driver, CartPage, ComparisonPage)
    mp = MainPage(driver)

    # переход на страницу с товарами
    mp.go_to_cpus()
    catalog = CatalogPage(driver)

    # фильтрация товаров по параметрам
    catalog.set_stock()
    catalog.set_price(*price)
    catalog.set_brand(*brand)
    catalog.set_cores(*cores)
    catalog.set_internal_graphics(*internal_graphics)
    catalog.set_ram(*ram)
    catalog.click_button_submit()

    # сравнение атрибутов товара в каталоге и на странице товара
    catalog.get_product_info_and_check_catalog_product()

    # сравнение атрибутов товара на странице товара и в корзине. покупка
    product = ProductPage(driver)
    product.get_product_info_and_check_product_cart()

    # заполнение данных на странице оформления заказа.
    # на этой странице происходит авторизация. в конце проверка на неправильный код из смс
    cart = CartPage(driver)
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    checkout.input_data_and_code(telephone_number_checkout, login, sms_code_checkout)
