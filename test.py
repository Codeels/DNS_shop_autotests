import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


computer_parts = "//a//a[@href='/catalog/17aa522a16404e77/komplektuyushhie-dlya-pk/']"
major_parts = "//a[@href='/catalog/88f4ff1d39dee00e/osnovnye-komplektuyushhie-dlya-pk/']"
cpus = "//a[@href='/catalog/17a899cd16404e77/processory/']"
button = '//div[@class="header-bottom__user-menu"]'
button_login = '//button[contains(@class, "base-ui-button-v2")]'
button_enter_with_password_checkp = '//div[@class="block-other-login-methods__password-button"]'

link = "https://www.dns-shop.ru/"
driver = webdriver.Chrome(service=Service("DNS_shop\\chromedriver.exe"))
driver.get(link)
driver.maximize_window()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, computer_parts))).click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, major_parts))).click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cpus))).click()
action = ActionChains(driver)
target = driver.find_element(By.XPATH, button)
action.move_to_element(target).perform()
target = driver.find_element(By.XPATH, button_login)
action.move_to_element(target).click(target).perform()

# n = driver.find_element(By.XPATH, button_login)
# n.click()
driver.find_element(By.XPATH, button_enter_with_password_checkp).click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_login))).click()
time.sleep(5)