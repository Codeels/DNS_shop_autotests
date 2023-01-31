import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# @pytest.fixture(scope="function")
def browser():
    print("\nbrowser open")
    link = "https://www.dns-shop.ru/"
    driver = webdriver.Chrome(service=Service("DNS_shop\\chromedriver.exe"))
    driver.get(link)
    driver.maximize_window()
    yield
    print("\nbrowser close")
