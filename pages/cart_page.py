import time
import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators
    button_delete_product = '//button[@class="menu-control-button remove-button"]/p'
    button_delete_products = '//div[@class="mass-selection__delete-btn"]'
    button_cart = "//div[@class='cart-button']"
    link_product = '//div[@class="cart-items__product-info"]//a'
    name_product = "//div[@class='cart-items__product-name']//a"
    price_product = '//div[@class="summary-header__sum"]//span'
    sku_product = '//div[@class="cart-items__product-code"]'
    button_checkout = '//div[@class="cart-tab-total-amount"]//span[@class="base-ui-button-v2__text"]'
    message_empty_cart = '//div[@class="empty-message"]'

    # Getters
    def get_name_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.name_product))).text

    def get_price_product(self):
        text = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product))).text
        text = text.replace(' ', '').split('₽')
        price = int(text[0])
        return price

    def get_sku_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.sku_product))).text

    def get_link_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.link_product))).get_attribute('href')

    def get_button_checkout(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    def get_button_delete_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_delete_product)))

    def get_button_delete_products(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_delete_products)))

    def get_message_empty_cart(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.message_empty_cart)))

    # Actions
    def click_button_checkout(self):
        with allure.step('Переход на страницу оформления заказа'):
            self.get_button_checkout().click()
            time.sleep(2)

    def click_button_delete_product(self):
        self.get_button_delete_product().click()

    def click_button_delete_products(self):
        self.get_button_delete_products().click()

    # Methods
    def delete_products_in_cart(self):
        if self.element_is_present(self.message_empty_cart):
            pass
        elif not self.element_is_present('//div[@class="cart-items__product"][2]'):
            self.click_button_delete_product()
        elif self.element_is_present('//div[@class="cart-items__product"][2]'):
            self.click_button_delete_products()

    def check_name_price_link(self,
                              name_in_catalog, name_in_cart,
                              price_in_catalog, price_in_cart,
                              link_in_catalog, link_in_cart):
        print(f'name:{self.check_name(name_in_catalog, name_in_cart)}')
        print(f'price:{self.check_price(price_in_catalog, price_in_cart)}')
        print(f'link:{self.check_links(link_in_catalog, link_in_cart)}')


