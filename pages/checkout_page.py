import time

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators
    # страница оформления заказа (checkp = checkout page)
    button_login_checkp = '//div[contains(@class,"base-login-button_tE_")]'
    button_enter_with_password = '//div[@class="block-other-login-methods__password-button"]'
    field_email_checkp = '//div[@class="form-entry-with-password__input"]//input'
    field_password_checkp = '//div[@class="form-entry-with-password__password"]//input'
    button_enter_checkp = '//div[@class="form-entry-with-password__main-button"]//button'
    button_confirm_order_checkp = '//div[@class="apply-button checkout-container__apply"]//button'
    # TODO добавить локаторов для заполнения телефона, для кнопки подтвердить зака, и для проверки номера


    # Getters


    # Actions


    # Methods


