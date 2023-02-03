from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators
    sku_product = '//div[@class="product-card-top__code"]'
    name_product = '//a[contains(@class,"product-card-tabs__product-title")]'
    price_product = '//div[@class="product-buy__price"]'
    button_buy = '//div[@class="product-card-top__buy"]//button[contains(@class,"buy-btn")]'

    # Getters
    def get_sku_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.sku_product))).text

    def get_name_product(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.name_product))).text

    def get_price_product(self):
        text = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product))).text
        text = text.replace(' ', '').split('₽')
        price = int(text[0])
        return price

    def get_link_product(self):
        return self.driver.current_url

    def get_button_buy(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.button_buy)))

    # Actions
    def click_button_buy(self):
        self.get_button_buy().click()

    # Methods
