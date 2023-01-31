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
    filter_price = '//div[@data-id="price"]'
    filter_price_min = "//div[@data-id='price']//div[@class='ui-input-small ui-input-small_list'][1]/input"
    filter_price_max = "//div[@data-id='price']//div[@class='ui-input-small ui-input-small_list'][2]/input"

    filter_brand = '//div[@data-id="brand"]'
    filter_brand_amd = "//div[@data-id='brand']//label[1]"
    filter_brand_intel = "//div[@data-id='brand']//label[2]"

    filter_cores = '//div[@data-id="f[mo]"]'
    filter_cores_4 = "//div[@data-id='f[mo]']//label[2]"
    filter_cores_6 = "//div[@data-id='f[mo]']//label[3]"
    filter_cores_8 = "//div[@data-id='f[mo]']//label[4]"

    filter_internal_graphics = '//div[@data-id="f[ykgj]"]'
    filter_internal_graphics_yes = "//div[@data-id='f[ykgj]']//label[1]"
    filter_internal_graphics_no = "//div[@data-id='f[ykgj]']//label[2]"

    filter_ram = '//div[@data-id="f[ykgf]"]'
    filter_ram_ddr4 = "//div[@data-id='f[ykgf]']//label[3]"
    filter_ram_ddr5 = "//div[@data-id='f[ykgf]']//label[4]"

    button_submit = "//*[@data-role='filters-submit']"
    button_reset = "//*[@data-role='filters-reset']"

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
    def get_filter_price(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.filter_price)))

    def get_filter_price_min(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.filter_price_min)))

    def get_filter_price_max(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.filter_price_max)))

    def get_filter_brand(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand)))

    def get_filter_brand_amd(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_amd)))

    def get_filter_brand_intel(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_intel)))

    def get_filter_cores(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_cores)))

    def get_filter_cores_4(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_cores_4)))

    def get_filter_cores_6(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_cores_6)))

    def get_filter_cores_8(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_cores_8)))

    def get_filter_internal_graphics(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_internal_graphics)))

    def get_filter_internal_graphics_yes(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_internal_graphics_yes)))

    def get_filter_internal_graphics_no(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_internal_graphics_no)))

    def get_filter_ram(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_ram)))

    def get_filter_ram_ddr4(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_ram_ddr4)))

    def get_filter_ram_ddr5(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_ram_ddr5)))

    def get_button_submit(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_submit)))

    def get_button_reset(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_reset)))

    # Actions

    # TODO может объединить фильрацию по цене и добавить ввод значений "снаружи"?
    def input_filter_price_min(self):
        action = ActionChains(self.driver)
        # надо было взять другой локатор
        action.move_to_element(self.get_filter_price()).perform()
        action.click(self.get_filter_price_min()).send_keys("1500").perform()

        # self.get_filter_price_min().click().send_keys("1500")

    def input_filter_price_max(self):
        action = ActionChains(self.driver)
        # target = self.driver.find_element(By.XPATH, self.filter_price_max)
        action.click(self.get_filter_price_max()).send_keys("15000").perform()
        # self.get_filter_price_max().click().send_keys("15000")

    def input_filter_brand(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_brand()).perform()
        action.click(self.get_filter_brand_intel()).perform()

    def click_button_submit(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_submit()).click(self.get_button_submit()).perform()
        # self.get_button_submit().click()

    # Methods
    def set_price(self):
        self.input_filter_price_min()
        self.input_filter_price_max()
        self.click_button_submit()
