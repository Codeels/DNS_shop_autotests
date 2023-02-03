from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComparisonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators
    rating_product1 = "//div[@class='compare-scoring__grades-grade'][2]//span[contains(@data-rating,'')][2]"
    rating_product2 = "//div[@class='compare-scoring__grades-grade'][1]//span[contains(@data-rating,'')][2]"
    button_product1_buy = '//div[@class="products-slider__item"][2]//div[@class="buy-button"]//button'
    button_product2_buy = '//div[@class="products-slider__item"][1]//div[@class="buy-button"]//button'
    name_product1 = "//div[@class='products-slider__item'][2]//div[@class='products-slider__product-name']"
    name_product2 = "//div[@class='products-slider__item'][1]//div[@class='products-slider__product-name']"
    price_product1 = '//div[@class="products-slider__item"][2]//div[@class="product-min-price__current"]'
    price_product2 = '//div[@class="products-slider__item"][1]//div[@class="product-min-price__current"]'
    link_product1 = '//div[@class="products-slider__item"][2]/div[2]/a'
    link_product2 = '//div[@class="products-slider__item"][1]/div[2]/a'
    button_delete_products = '//div[@class="clear-app"]/span[2]'

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
        text1 = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product1))).text
        text1 = text1.replace(' ', '').split('₽')
        price = int(text1[0])
        return price

    def get_price_product2(self):
        text2 = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product2))).text
        text2 = text2.replace(' ', '').split('₽')
        price = int(text2[0])
        return price

    def get_link_product1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.link_product1))).get_attribute('href')

    def get_link_product2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.link_product2))).get_attribute('href')

    def get_button_product1_buy(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product1_buy)))

    def get_button_product2_buy(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_product2_buy)))

    def get_button_delete_products_in_comparison(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_delete_products)))

    # Actions

    def click_button_product1_buy(self):
        self.get_button_product1_buy().click()

    def click_button_product2_buy(self):
        self.get_button_product2_buy().click()

    def click_button_delete_products_in_comparison(self):
        self.get_button_delete_products_in_comparison().click()

    # Methods
    def delete_products_in_comparison(self):
        if self.element_is_present(self.button_delete_products):
            self.click_button_delete_products_in_comparison()
        else:
            pass

    def choose_best_product(self):
        if self.get_price_product1() < self.get_price_product2():
            self.click_button_product1_buy()
        else:
            self.click_button_product2_buy()

