import time
import pytest

from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.comparison_page import ComparisonPage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage

login = 'gamag25045@ekcsoft.com'
password = 'gamag25045'
cores = [1, 1, 1]
price = [1500, 15000]
brand = [1, 1]
internal_graphics = [1, 0]
ram = [1, 1]
filter_stock = '//div[@data-id="stock"]'
telephone_number_checkout = '1111111111'
sms_code_checkout = '111111'


@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_1(driver):
    link = "https://www.dns-shop.ru/"

    # логин
    mp = MainPage(driver)
    mp.log_in(login, password, main=True)

    # очистка корзины и страницы сравнения от товаров
    mp.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.delete_products_in_cart()
    cart_page.go_to_comparison_page()
    comparison_page = ComparisonPage(driver)
    comparison_page.delete_products_in_comparison()
    comparison_page.go_to_main_page()
    mp = MainPage(driver)
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
    time.sleep(1)

    # сравнение атрибутов товара из каталога и корзины
    product_name_in_catalog = catalog.get_name_product1()
    product_price_in_catalog = catalog.get_price_product1()
    product_link_in_catalog = catalog.get_link_product1()
    catalog.click_button_product1_buy()
    time.sleep(2)
    catalog.go_to_cart()
    cart = CartPage(driver)
    product_name_in_cart = cart.get_name_product()
    product_price_in_cart = cart.get_price_product()
    product_link_in_cart = cart.get_link_product()
    print(f'name: {cart.check_name(product_name_in_catalog, product_name_in_cart)}')
    print(f'price: {cart.check_price(product_price_in_catalog, product_price_in_cart)}')
    print(f'link: {cart.check_links(product_link_in_catalog, product_link_in_cart)}')

    # оформление товара. в конце проверка на неправильный код из смс
    time.sleep(2)
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    checkout.input_telephone_number(telephone_number_checkout)
    checkout.input_email(login)
    checkout.choose_shop()
    time.sleep(2)
    checkout.click_button_confirm_order()
    checkout.input_sms_code(sms_code_checkout)
    checkout.click_button_confirm_sms_code()
    print(f'error message: {checkout.check_error_message()}')
    time.sleep(5)


@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_2(driver):
    link = "https://www.dns-shop.ru/"
    mp = MainPage(driver)

    # очистка корзины и сравнения
    mp.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.delete_products_in_cart()
    cart_page.go_to_comparison_page()
    comparison_page = ComparisonPage(driver)
    comparison_page.delete_products_in_comparison()
    comparison_page.go_to_main_page()

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
    product_name_in_catalog = catalog.get_name_product1()
    product_price_in_catalog = catalog.get_price_product1()
    product_link_in_catalog = catalog.get_link_product1()
    catalog.click_button_product1_buy()
    catalog.go_to_cart()
    cart = CartPage(driver)
    product_name_in_cart = cart.get_name_product()
    product_price_in_cart = cart.get_price_product()
    product_link_in_cart = cart.get_link_product()
    print(f'name: {cart.check_name(product_name_in_catalog, product_name_in_cart)}')
    print(f'price: {cart.check_price(product_price_in_catalog, product_price_in_cart)}')
    print(f'link: {cart.check_links(product_link_in_catalog, product_link_in_cart)}')

    # заполнение данных на странице оформления заказа. на этой странице происходит логин. в конце проверка на неправильный код из смс
    time.sleep(2)
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    time.sleep(2)
    mp.log_in(login, password, checkout=True)
    checkout.input_telephone_number(telephone_number_checkout)
    checkout.input_email(login)
    checkout.choose_shop()
    time.sleep(2)
    checkout.click_button_confirm_order()
    checkout.input_sms_code(sms_code_checkout)
    checkout.click_button_confirm_sms_code()
    print(f'error message: {checkout.check_error_message()}')
    time.sleep(5)


@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_3(driver):
    link = "https://www.dns-shop.ru/"
    # логин
    mp = MainPage(driver)
    mp.log_in(login, password, main=True)

    # очистка корзины и страницы сравнения от товаров
    mp.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.delete_products_in_cart()
    cart_page.go_to_comparison_page()
    comparison_page = ComparisonPage(driver)
    comparison_page.delete_products_in_comparison()
    comparison_page.go_to_main_page()

    # переход на страницу с товарами
    mp = MainPage(driver)
    mp.go_to_cpus()

    # фильтрация товаров по параметрам
    catalog = CatalogPage(driver)
    catalog.set_stock()
    catalog.set_price(*price)
    catalog.set_brand(*brand)
    catalog.set_cores(*cores)
    catalog.set_internal_graphics(*internal_graphics)
    catalog.set_ram(*ram)
    catalog.click_button_submit()

    # сравнение параметров товаров из каталога и страницы сравнения
    product1_name_in_catalog = catalog.get_name_product1()
    product1_price_in_catalog = catalog.get_price_product1()
    product1_link_in_catalog = catalog.get_link_product1()
    product2_name_in_catalog = catalog.get_name_product2()
    product2_price_in_catalog = catalog.get_price_product2()
    product2_link_in_catalog = catalog.get_link_product2()
    catalog.click_button_product1_compare()
    catalog.click_button_product2_compare()
    time.sleep(2)
    catalog.go_to_comparison_page()
    compare = ComparisonPage(driver)
    product1_name_in_comparison = compare.get_name_product1()
    product1_price_in_comparison = compare.get_price_product1()
    product1_link_in_comparison = compare.get_link_product1()
    product2_name_in_comparison = compare.get_name_product2()
    product2_price_in_comparison = compare.get_price_product2()
    product2_link_in_comparison = compare.get_link_product2()
    print(f'name1: {compare.check_name(product1_name_in_catalog, product1_name_in_comparison)}')
    print(f'price1: {compare.check_price(product1_price_in_catalog, product1_price_in_comparison)}')
    print(f'link1: {compare.check_links(product1_link_in_catalog, product1_link_in_comparison)}')
    print(f'name2: {compare.check_name(product2_name_in_catalog, product2_name_in_comparison)}')
    print(f'price2: {compare.check_price(product2_price_in_catalog, product2_price_in_comparison)}')
    print(f'link2: {compare.check_links(product2_link_in_catalog, product2_link_in_comparison)}')

    # выбор товара подешевле на странце сравнения товаров
    compare.choose_best_product()
    time.sleep(2)

    # переход в корзину
    compare.go_to_cart()
    cart = CartPage(driver)
    time.sleep(2)

    # заполнение данных на странице оформления заказа. в конце проверка на неправильный код из смс
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    time.sleep(2)
    checkout.input_telephone_number(telephone_number_checkout)
    checkout.input_email(login)
    checkout.choose_shop()
    time.sleep(2)
    checkout.click_button_confirm_order()
    checkout.input_sms_code(sms_code_checkout)
    checkout.click_button_confirm_sms_code()
    print(f'error message: {checkout.check_error_message()}')
    time.sleep(5)


@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_4(driver):
    link = "https://www.dns-shop.ru/"
    # логин
    mp = MainPage(driver)
    mp.log_in(login, password, main=True)

    # очистка корзины и сравнения
    mp.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.delete_products_in_cart()
    cart_page.go_to_comparison_page()
    comparison_page = ComparisonPage(driver)
    comparison_page.delete_products_in_comparison()
    comparison_page.go_to_main_page()

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

    # сравние атрибутов товара в каталоге и на странице товара
    product_name_in_catalog = catalog.get_name_product1()
    product_price_in_catalog = catalog.get_price_product1()
    product_link_in_catalog = catalog.get_link_product1()
    driver.get(product_link_in_catalog)
    product = ProductPage(driver)
    product_name_in_product = product.get_name_product()
    product_price_in_product = product.get_price_product()
    product_link_in_product = product.get_link_product()
    print(f'name: {catalog.check_name(product_name_in_catalog, product_name_in_product)}')
    print(f'price: {catalog.check_price(product_price_in_catalog, product_price_in_product)}')
    print(f'link: {catalog.check_links(product_link_in_catalog, product_link_in_product)}')

    # покупка товара
    product.click_button_buy()
    time.sleep(2)

    # переход корзину
    product.go_to_cart()
    cart = CartPage(driver)

    # сравнение атрибутов товара на странице товара и в корзине
    product_name_in_cart = cart.get_name_product()
    product_price_in_cart = cart.get_price_product()
    product_link_in_cart = cart.get_link_product()
    print(f'name: {cart.check_name(product_name_in_product, product_name_in_cart)}')
    print(f'price: {cart.check_price(product_price_in_product, product_price_in_cart)}')
    print(f'link: {cart.check_links(product_link_in_product, product_link_in_cart)}')

    # заполнение данных на странице оформления заказа. на этой странице происходит логин. в конце проверка на неправильный код из смс
    time.sleep(2)
    cart.click_button_checkout()
    checkout = CheckoutPage(driver)
    time.sleep(2)
    checkout.input_telephone_number(telephone_number_checkout)
    checkout.input_email(login)
    checkout.choose_shop()
    time.sleep(2)
    checkout.click_button_confirm_order()
    checkout.input_sms_code(sms_code_checkout)
    checkout.click_button_confirm_sms_code()
    print(f'error message: {checkout.check_error_message()}')
    time.sleep(5)