import time

from pages.base_page import BasePage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




    # Locators

    link_computer_parts = "//a//a[@href='/catalog/17aa522a16404e77/komplektuyushhie-dlya-pk/']"
    link_major_parts = "//a[@href='/catalog/88f4ff1d39dee00e/osnovnye-komplektuyushhie-dlya-pk/']"
    link_cpus = "//a[@href='/catalog/17a899cd16404e77/processory/']//input[@id='Процессоры']"
    # нашлось две кнопки. Одна с наведением мыши, другая без
    # после нажатия на кнопку ниже вызывается окно. наверное, надо будет переключиться
    button_login = '//button[contains(@class, "base-ui-button-v2")]'

    # страница каталога (catp = catalog page)
    filter_price_min = "//div[@data-id='price']//div[@class='ui-input-small ui-input-small_list'][1]"
    filter_price_max = "//div[@data-id='price']//div[@class='ui-input-small ui-input-small_list'][2]"
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

    # страница товара (prodp = product page)
    sku_product_prodp = '//div[@class="product-card-top__code"]'
    name_product_prodp = '//a[contains(@class,"product-card-tabs__product-title")]'
    name2_product_prodp = '//div[@class="product-characteristics__group"][2]//div[@id="pcv-QYN4Ba"]'
    price_product_prodp = '//div[@class="product-buy__price"]'

    # кнопка для перехода на страницу сравнения
    button_compare = "//a[@class='compare-link-counter']"

    # страница сравнения товаров (compp = comparison page)
    rating_product1 = "//div[@class='compare-scoring__grades-grade'][1]//span[contains(@data-rating,'')][2]"
    rating_product2 = "//div[@class='compare-scoring__grades-grade'][2]//span[contains(@data-rating,'')][2]"
    button_product1_buy_compp = "//div[@class='buy-button'][1]"
    button_product2_buy_compp = "//div[@class='buy-button'][2]"
    name_product1_compp = "//div[@class='products-slider__item'][1]//div[@class='products-slider__product-name']"
    name_product2_compp = "//div[@class='products-slider__item'][2]//div[@class='products-slider__product-name']"
    price_product1_compp = '//div[@class="products-slider__item"][1]//div[@class="product-min-price__current"]'
    price_product2_compp = '//div[@class="products-slider__item"][2]//div[@class="product-min-price__current"]'

    # страница корзины
    button_cart = "//div[@class='cart-button']"
    name_product_cart = "//div[@class='cart-items__product-name']//a"
    price_product_cart = '//div[@class="summary-header__sum"]//span'
    sku_product_cart = '//div[@class="cart-items__product-code"]'


    # страница оформления заказа (checkp = checkout page)
    button_checkout = '//div[@class="cart-tab-total-amount"]//span[@class="base-ui-button-v2__text"]'
    button_login_checkp = '//div[contains(@class,"base-login-button_tE_")]'
    button_enter_with_password_checkp = '//div[@class="block-other-login-methods__password-button"]'
    field_email_checkp = '//div[@class="form-entry-with-password__input"]//input'
    field_password_checkp = '//div[@class="form-entry-with-password__password"]//input'
    button_enter_checkp = '//div[@class="form-entry-with-password__main-button"]//button'
    button_confirm_order_checkp = '//div[@class="apply-button checkout-container__apply"]//button'
    # надо проверить, что покупка не проходит без введения данных

    # Getters

    def get_computer_parts_link(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.link_computer_parts)))

    def get_computer_parts_link(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.link_computer_parts)))


    # Actions

    def click_computer_parts_link(self):
        self.get_computer_parts_link().click()
        print("Click")

    # Methods

    link = "https://www.dns-shop.ru/"
    driver = webdriver.Chrome(service=Service("DNS_shop\\chromedriver.exe"))
    driver.get(link)
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_login))).click()
    time.sleep(2)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_computer_parts))).click()
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_major_parts))).click()
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_cpus))).click()
