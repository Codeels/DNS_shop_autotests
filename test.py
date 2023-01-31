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


def test_test():
    link = "https://www.dns-shop.ru/"
    driver = webdriver.Chrome(service=Service("DNS_shop\\chromedriver.exe"))
    driver.get(link)
    driver.maximize_window()
    mp = MainPage(driver)
    mp.log_in(login, password)
    mp.go_to_cpus()
    cp = CatalogPage(driver)
    time.sleep(3)
    cp.input_filter_price_min()
    time.sleep(5)
    # cp.input_filter_price_max()
    # cp.click_button_submit()
