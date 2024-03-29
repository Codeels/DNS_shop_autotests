import time
import allure

from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage
from pages.comparison_page import ComparisonPage
from pages.product_page import ProductPage


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
    service_rating_product1 = '//div[@data-id="product"][1]//a[contains(@class,"catalog-product__service-rating")]'
    service_rating_product2 = '//div[@data-id="product"][2]//a[contains(@class,"catalog-product__service-rating")]'

    # Getters

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
        text1 = WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product1))).text
        text1 = text1.replace(' ', '').split('₽')
        price = int(text1[0])
        return price

    def get_price_product2(self):
        text2 = WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product2))).text
        text2 = text2.replace(' ', '').split('₽')
        price = int(text2[0])
        return price

    def get_service_rating_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.service_rating_product1))).text

    def get_service_rating_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.service_rating_product2))).text

    # Actions

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
        time.sleep(2)

    def click_button_product2_compare(self):
        self.get_button_product2_compare().click()
        time.sleep(2)

    def click_button_product1_buy(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_product1_buy()).perform()
        self.get_button_product1_buy().click()
        time.sleep(2)

    def click_button_product2_buy(self):
        self.get_button_product2_buy().click()

    def click_button_submit(self):
        with allure.step('Применение фильтров'):
            action = ActionChains(self.driver)
            action.move_to_element(self.get_button_submit()).click(self.get_button_submit()).perform()
            time.sleep(2)

    def click_button_reset(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_reset()).click(self.get_button_reset()).perform()

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

    def go_to_product_page(self, link):
        self.driver.get(link)
        time.sleep(2)

    # Methods
    def check_name_price_link2(self):
        catalog = CatalogPage(self.driver)
        product_name_in_catalog = catalog.get_name_product1()
        product_price_in_catalog = catalog.get_price_product1()
        product_link_in_catalog = catalog.get_link_product1()
        print(product_name_in_catalog)
        print(product_price_in_catalog)
        print(product_link_in_catalog)

    def get_product_info_and_check_catalog_cart(self):
        with allure.step('Проверка названия, цены и ссылки товара'):
            catalog = CatalogPage(self.driver)
            product_name_in_catalog = catalog.get_name_product1()
            product_price_in_catalog = catalog.get_price_product1()
            product_link_in_catalog = catalog.get_link_product1()
            catalog.click_button_product1_buy()
            catalog.go_to_cart()
            cart = CartPage(self.driver)
            product_name_in_cart = cart.get_name_product()
            product_price_in_cart = cart.get_price_product()
            product_link_in_cart = cart.get_link_product()
            cart.check_name_price_link(product_name_in_catalog, product_name_in_cart,
                                       product_price_in_catalog, product_price_in_cart,
                                       product_link_in_catalog, product_link_in_cart)

    def get_product_info_and_check_catalog_compare(self):
        with allure.step('Проверка названия, цены и ссылки товара'):
            catalog = CatalogPage(self.driver)

            product1_name_in_catalog = catalog.get_name_product1()
            product1_price_in_catalog = catalog.get_price_product1()
            product1_link_in_catalog = catalog.get_link_product1()
            product2_name_in_catalog = catalog.get_name_product2()
            product2_price_in_catalog = catalog.get_price_product2()
            product2_link_in_catalog = catalog.get_link_product2()

            catalog.click_button_product1_compare()
            catalog.click_button_product2_compare()
            catalog.go_to_comparison_page()
            compare = ComparisonPage(self.driver)

            product1_name_in_comparison = compare.get_name_product1()
            product1_price_in_comparison = compare.get_price_product1()
            product1_link_in_comparison = compare.get_link_product1()
            product2_name_in_comparison = compare.get_name_product2()
            product2_price_in_comparison = compare.get_price_product2()
            product2_link_in_comparison = compare.get_link_product2()

            compare.check_name_price_link(product1_name_in_catalog, product1_name_in_comparison,
                                          product1_price_in_catalog, product1_price_in_comparison,
                                          product1_link_in_catalog, product1_link_in_comparison,
                                          product2_name_in_catalog, product2_name_in_comparison,
                                          product2_price_in_catalog, product2_price_in_comparison,
                                          product2_link_in_catalog, product2_link_in_comparison)

    def get_product_info_and_check_catalog_product(self):
        with allure.step('Проверка названия, цены и ссылки товара'):
            catalog = CatalogPage(self.driver)

            product_name_in_catalog = catalog.get_name_product1()
            product_price_in_catalog = catalog.get_price_product1()
            product_link_in_catalog = catalog.get_link_product1()

            catalog.go_to_product_page(product_link_in_catalog)

            product = ProductPage(self.driver)

            product_name_in_product = product.get_name_product()
            product_price_in_product = product.get_price_product()
            product_link_in_product = product.get_link_product()

            product.check_name_price_link(product_name_in_catalog, product_name_in_product,
                                          product_price_in_catalog, product_price_in_product,
                                          product_link_in_catalog, product_link_in_product)
