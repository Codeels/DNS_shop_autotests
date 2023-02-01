import time

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ComparisonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators

    # страница сравнения товаров (compp = comparison page)
    rating_product1 = "//div[@class='compare-scoring__grades-grade'][1]//span[contains(@data-rating,'')][2]"
    rating_product2 = "//div[@class='compare-scoring__grades-grade'][2]//span[contains(@data-rating,'')][2]"
    button_product1_buy = "//div[@class='buy-button'][1]"
    button_product2_buy = "//div[@class='buy-button'][2]"
    name_product1 = "//div[@class='products-slider__item'][1]//div[@class='products-slider__product-name']"
    name_product2 = "//div[@class='products-slider__item'][2]//div[@class='products-slider__product-name']"
    price_product1 = '//div[@class="products-slider__item"][1]//div[@class="product-min-price__current"]'
    price_product2 = '//div[@class="products-slider__item"][2]//div[@class="product-min-price__current"]'

    # Getters
    def get_rating_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.rating_product1))).get_attribute('data-rating')

    def get_rating_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.rating_product2))).get_attribute('data-rating')

    def get_name_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.name_product1))).text

    def get_name_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.name_product2))).text

    def get_price_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product1))).text

    def get_price_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product2))).text

    def get_button_product1_buy(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product1_buy)))

    def get_button_product2_buy(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product2_buy)))

    # Actions

    def click_button_product1_buy(self):
        self.get_button_product1_buy().click()

    def click_button_product2_buy(self):
        self.get_button_product2_buy().click()

    # Methods
    # TODO написать методы для сравнения товаров между собой
    # TODO написать проверки на то, что правильные товары попали в сравнение