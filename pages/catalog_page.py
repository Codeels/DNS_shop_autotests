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
    filter_stock = '//div[@data-id="stock"]'
    filter_stock_in_stock = '//div[@data-id="stock"]/label[1]/span[2]'
    filter_stock_order_today = '//div[@data-id="stock"]/label[2]/span[2]'
    filter_stock_order_tomorrow = '//div[@data-id="stock"]/label[3]/span[2]'
    filter_stock_order_later = '//div[@data-id="stock"]/label[4]/span[2]'

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
    filter_ram_ddr4 = "//div[@data-id='f[ykgf]']//label[3]/span[2]"
    filter_ram_ddr5 = "//div[@data-id='f[ykgf]']//label[4]/span[2]"

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
    # TODO подумать, нужны ли эти локаторы
    service_rating_product1 = '//div[@data-id="product"][1]//a[contains(@class,"catalog-product__service-rating")]'
    service_rating_product2 = '//div[@data-id="product"][2]//a[contains(@class,"catalog-product__service-rating")]'

    # Getters
    # TODO добавить фильтры для наличия товара
    def get_filter_stock(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_stock)))

    def get_filter_stock_in_stock(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_stock_in_stock)))

    def get_filter_stock_order_today(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_stock_order_today)))

    def get_filter_stock_order_tomorrow(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_stock_order_tomorrow)))

    def get_filter_stock_order_later(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_stock_order_later)))

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

    def get_button_product1_compare(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product1_compare)))

    def get_button_product2_compare(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product2_compare)))

    def get_link_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.XPATH, self.link_product1))).get_attribute('href')

    def get_link_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((By.XPATH, self.link_product2))).get_attribute('href')

    def get_button_product1_buy(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product1_buy)))

    def get_button_product2_buy(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product2_buy)))

    def get_name_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product1))).text

    def get_name_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product2))).text

    def get_price_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product1))).text

    def get_price_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product2))).text

    def get_service_rating_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.service_rating_product1))).text

    def get_service_rating_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.service_rating_product2))).text

    # Actions

    # TODO может объединить фильрацию по цене и добавить ввод значений "снаружи"?
    def input_filter_stock(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_stock()).perform()
        self.get_filter_stock_order_today().click()
        self.get_filter_stock_order_tomorrow().click()
        self.get_filter_stock_order_later().click()
        # проблема с несколькими кликами подряд. почему-то не работает
        # action.click(self.get_filter_stock_order_today).click(self.get_filter_stock_order_tomorrow).click(self.get_filter_stock_order_later()).perform()

    def input_filter_price(self, price_min, price_max):
        action = ActionChains(self.driver)
        # надо было взять другой локатор
        action.move_to_element(self.get_filter_price()).perform()
        action.click(self.get_filter_price_min()).send_keys(price_min).perform()
        action.click(self.get_filter_price_max()).send_keys(price_max).perform()

        # self.get_filter_price_min().click().send_keys("1500")

    # def input_filter_price_max(self, price_max):
    #     action = ActionChains(self.driver)
    #     # target = self.driver.find_element(By.XPATH, self.filter_price_max)
    #     action.click(self.get_filter_price_max()).send_keys(price_max).perform()
    #     # self.get_filter_price_max().click().send_keys("15000")

    def input_filter_brand(self, amd=False, intel=False):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_brand()).perform()
        if amd and intel:
            action.click(self.get_filter_brand_amd()).click(self.get_filter_brand_intel()).perform()
        elif amd:
            action.click(self.get_filter_brand_amd()).perform()
        elif intel:
            action.click(self.get_filter_brand_intel()).perform()

    def input_filter_cores(self, cores_4=False, cores_6=False, cores_8=False):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_cores()).perform()
        # почему-то заработало только после разделения перехода и клика на фильтр с количеством ядер
        action.click(self.get_filter_cores()).perform()
        if cores_4 and cores_6 and cores_8:
            action.click(self.get_filter_cores_4()).click(self.get_filter_cores_6()).click(
                self.get_filter_cores_8()).perform()
        elif cores_4 and cores_6:
            action.click(self.get_filter_cores_4()).click(self.get_filter_cores_6()).perform()
        elif cores_4 and cores_8:
            action.click(self.get_filter_cores_4()).click(self.get_filter_cores_8()).perform()
        elif cores_6 and cores_8:
            action.click(self.get_filter_cores_6()).click(self.get_filter_cores_8()).perform()
        elif cores_4:
            action.click(self.get_filter_cores_4()).perform()
        elif cores_6:
            action.click(self.get_filter_cores_6()).perform()
        elif cores_8:
            action.click(self.get_filter_cores_8()).perform()

    # здесь странная логика, так как на сайте вместо радиобатона использован чекбокс при выборе двух элементов
    def input_filter_internal_graphics(self, yes=False, no=False):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_internal_graphics()).perform()
        action.click(self.get_filter_internal_graphics()).perform()
        if yes and no:
            action.click(self.get_filter_internal_graphics_yes()).click(
                self.get_filter_internal_graphics_no()).perform()
        elif yes:
            action.click(self.get_filter_internal_graphics_yes()).perform()
        elif no:
            action.click(self.get_filter_internal_graphics_no()).perform()

    def input_filter_ram(self, ddr4=False, ddr5=False):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_filter_ram()).perform()
        action.click(self.get_filter_ram()).perform()
        if ddr4 and ddr5:
            action.click(self.get_filter_ram_ddr4()).click(self.get_filter_ram_ddr5()).perform()
        elif ddr4:
            action.click(self.get_filter_ram_ddr4()).perform()
        elif ddr5:
            action.click(self.get_filter_ram_ddr5()).perform()

    def click_button_product1_compare(self):
        self.get_button_product1_compare().click()

    def click_button_product2_compare(self):
        self.get_button_product2_compare().click()

    def click_button_product1_buy(self):
        self.get_button_product1_buy().click()

    def click_button_product2_buy(self):
        self.get_button_product2_buy().click()

    # TODO может быть стоит переместить в методы из actions
    def click_button_submit(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_submit()).click(self.get_button_submit()).perform()

    def click_button_reset(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_reset()).click(self.get_button_reset()).perform()

    # Methods
    def set_price(self, price_min, price_max):
        self.input_filter_price(price_min, price_max)

    def set_brand(self, amd=False, intel=False):
        self.input_filter_brand(amd, intel)

    def set_cores(self, cores_4=False, cores_6=False, cores_8=False):
        self.input_filter_cores(cores_4, cores_6, cores_8)

    def set_internal_graphics(self, yes=False, no=False):
        self.input_filter_internal_graphics(yes, no)

    def set_ram(self, ddr4=False, ddr5=False):
        self.input_filter_ram(ddr4, ddr5)

    def set_stock(self):
        self.input_filter_stock()
