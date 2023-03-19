# import pytest as pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
#
# @pytest.fixture(scope="function")
# def driver():
#     print("\nbrowser open")
#     link = "https://www.dns-shop.ru/"
#     driver = webdriver.Chrome(service=Service("DNS_shop\\chromedriver.exe"))
#     driver.get(link)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#     print("\nbrowser close")
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    link = "https://www.dns-shop.ru/"
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    time.sleep(15)
    driver.get(link)
    time.sleep(15)
    yield driver
    driver.quit()