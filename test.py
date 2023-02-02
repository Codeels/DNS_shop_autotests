import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.catalog_page import CatalogPage
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


def test_test(driver):
    link = "https://www.dns-shop.ru/"
    link2 = 'https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/'
    link3 = 'https://www.dns-shop.ru/checkout/'
    mp = MainPage(driver)
    mp.log_in(login, password)
    mp.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.delete_products_in_cart()
    cart_page.go_to_comparison_page()
    comparison_page = ComparisonPage(driver)
    comparison_page.delete_products_in_comparison()
    comparison_page.go_to_main_page()
    mp = MainPage(driver)
    mp.go_to_cpus()
    # cp = CatalogPage(driver)
    time.sleep(5)

    # cp.set_price(*price)
    # cp.set_brand(*brand)
    # cp.set_cores(*cores)
    # cp.set_internal_graphics(*internal_graphics)
    # cp.set_ram(*ram)
    # cp.click_button_submit()
