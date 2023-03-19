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
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


@pytest.fixture(scope="function")
def driver():
    print("\nbrowser open")
    link = "https://www.dns-shop.ru/"
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.maximize_window()
    driver.get(link)
    yield driver
    driver.quit()
    print("\nbrowser close")