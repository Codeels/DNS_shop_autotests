import time

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators
    # страница каталога (catp = catalog page)
    filter_price_min = "//div[@data-id='price']//div[@class='ui-input-small ui-input-small_list'][1]/input"
    filter_price_max = "//div[@data-id='price']//div[@class='ui-input-small ui-input-small_list'][2]/input"
    filter_brand_amd = "//div[@data-id='brand']//label[1]"
    filter_brand_intel = "//div[@data-id='brand']//label[2]"
    filter_cores_number_4 = "//div[@data-id='f[mo]']//label[2]"
    filter_cores_number_6 = "//div[@data-id='f[mo]']//label[3]"
    filter_cores_number_8 = "//div[@data-id='f[mo]']//label[4]"
    filter_internal_graphics_yes = "//div[@data-id='f[ykgj]']//label[1]"
    filter_internal_graphics_no = "//div[@data-id='f[ykgj]']//label[2]"
    filter_ram_ddr4 = "//div[@data-id='f[ykgf]']//label[3]"
    filter_ram_ddr5 = "//div[@data-id='f[ykgf]']//label[4]"
    button_submit = "//*[@data-role='filters-submit']"
    button_product1_compare = "//div[@data-id='product'][1]//span[@class='compare-checkbox']"
    button_product2_compare = "//div[@data-id='product'][2]//span[@class='compare-checkbox']"
    # надо достать href
    link_product1 = "//div[@data-id='product'][1]//a[contains(@class, 'catalog-product__name')]"
    link_product2 = "//div[@data-id='product'][2]//a[contains(@class, 'catalog-product__name')]"
    button_product1_buy = "//div[@data-id='product'][1]//button[2]"
    button_product2_buy = "//div[@data-id='product'][2]//button[2]"
    name_product1 = '//div[@data-id="product"][1]//a[@class="catalog-product__name ui-link ui-link_black"]//span'
    name_product2 = '//div[@data-id="product"][2]//a[@class="catalog-product__name ui-link ui-link_black"]//span'
    price_product1 = '//div[@data-id="product"][1]//div[@class="product-buy__price"]'
    price_product2 = '//div[@data-id="product"][2]//div[@class="product-buy__price"]'
    # на старнице каталога sku появляются только после наведения курсора
    product1_code = ''
    product2_code = ''

    # Getters
    def get_filter_price_min(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.filter_price_min)))

    def get_filter_price_max(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.filter_price_max)))

    def get_button_submit(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.button_submit)))

    # Actions
    def input_filter_price_min(self):
        action = ActionChains(self.driver)
        target = self.driver.find_element(By.XPATH, self.filter_price_min)
        # TODO кажется, что надо разделять действия
        action.move_to_element(target).perform()
        # action.move_to_element(target).click(target).send_keys("1500").perform()
        action.click(target).send_keys("1500").perform()

        # self.get_filter_price_min().click().send_keys("1500")

    def input_filter_price_max(self):
        action = ActionChains(self.driver)
        target = self.driver.find_element(By.XPATH, self.filter_price_max)
        action.click(target).send_keys("15000").perform()
        # self.get_filter_price_max().click().send_keys("15000")

    def click_button_submit(self):
        self.get_button_submit().click()

    # Methods
    def set_price(self):
        print("something happened")
        # action = ActionChains(self.driver)
        # target = self.driver.find_element(By.XPATH, self.filter_price_min)
        # action.move_to_element(target).click(target).send_keys("1500").perform()
        # time.sleep(5)
        # self.input_filter_price_min()
        # self.input_filter_price_max()
        self.click_button_submit()
        time.sleep(5)
