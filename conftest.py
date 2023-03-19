# import pytest as pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
#
# @pytest.fixture(scope="function")
# def driver():
#     print("\nbrowser open")
#     link = "https://www.dns-shop.ru/"
#     # driver = webdriver.Chrome(service=Service("DNS_shop\\chromedriver"))
#     driver = webdriver.Chrome(service=Service("\\chromedriver"))
#     driver.get(link)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#     print("\nbrowser close")


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope="function")
# def driver():
#     print("\nbrowser open")
#     link = "https://www.dns-shop.ru/"
#     driver = webdriver.Chrome(service=Service("\\chromedriver"))
#     # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get(link)
#     yield driver
#     driver.quit()
#     print("\nbrowser close")


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)