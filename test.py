import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.base_page import BasePage

login = 'gamag25045@ekcsoft.com'
password = 'gamag25045'
cores = [1, 1, 1]

def test_test():
    link = "https://www.dns-shop.ru/"
    driver = webdriver.Chrome(service=Service("DNS_shop\\chromedriver.exe"))
    driver.get(link)
    driver.maximize_window()
    mp = MainPage(driver)
    mp.log_in(login, password)
    mp.go_to_cpus()
    cp = CatalogPage(driver)
    cp.click_button_product2_buy()
    cp.go_to_cart()
    # cp.click_button_product1_compare()
    # cp.click_button_product2_compare()
    time.sleep(5)
    # cp.input_filter_cores(*cores)
    # cp.input_filter_brand(amd=True, intel=True)
    # cp.input_filter_internal_graphics(1, 0)
    # cp.click_button_submit()

    # cp.click_button_reset()
