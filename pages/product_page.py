import time

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators
    sku_product = '//div[@class="product-card-top__code"]'
    name_product = '//a[contains(@class,"product-card-tabs__product-title")]'
    price_product = '//div[@class="product-buy__price"]'

    # Getters
    def get_sku_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.sku_product))).text

    def get_name_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.name_product))).text

    def get_price_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product))).text

    # Actions

    # Methods
    def compare_price_in_product_page(self, product_in_catalog):
        assert self.get_price_product() == product_in_catalog, "Price do not match"

    # TODO скомпоновать все ассерты в один метод
