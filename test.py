import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.comparison_page import ComparisonPage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.cart_page import CartPage

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
def test_test(driver):
    link = "https://www.dns-shop.ru/"
    link2 = 'https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/'
    # noinspection PyPackageRequirements
    link3 = 'https://www.dns-shop.ru/checkout/'
    mp = MainPage(driver)
    mp.log_in(login, password)
    # очистка корзины и сравнения работает
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
    # фильтрация работает
    catalog.set_stock()
    catalog.set_price(*price)
    catalog.set_brand(*brand)
    catalog.set_cores(*cores)
    catalog.set_internal_graphics(*internal_graphics)
    catalog.set_ram(*ram)
    catalog.click_button_submit()
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
    cart.click_button_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    checkout.input_telephone_number(telephone_number_checkout)
    checkout.input_email(login)
    checkout.click_button_confirm_order()
    checkout.input_sms_code(sms_code_checkout)
    checkout.click_button_confirm_sms_code()
    print(f'error message: {checkout.check_error_message()}')
    time.sleep(5)
