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

    field_telephone_number = '//input[@type="tel"]'
    field_email = '//input[@type="text"]'
    button_confirm_order = '//div[@class="apply-button checkout-container__apply"]//button'
    field_sms_code = '//input[@id="ir-atvt4"]'
    button_confirm_sms_code = '//button[contains(@class, "base-phone-confirm-code-check__btn")]'
    error_message = '//div[@class="base-phone-confirm-code-check__error"]'

    # TODO добавить локаторов для заполнения телефона, для кнопки подтвердить заказ, и для проверки номера

    # Getters
    def get_field_telephone_number(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.field_telephone_number)))

    def get_field_email(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.field_email)))

    def get_field_sms_code(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.field_sms_code)))

    def get_button_confirm_order(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_confirm_order)))

    def get_button_confirm_sms_code(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_confirm_sms_code)))

    def get_error_message(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.error_message))).text

    # Actions
    def input_telephone_number(self, telephone_number):
        action = ActionChains(self.driver)
        action.click(self.get_field_telephone_number()).send_keys(telephone_number).perform()

    def input_email(self, email):
        action = ActionChains(self.driver)
        action.click(self.get_field_email()).send_keys(email).perform()

    def click_button_confirm_order(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_confirm_order()).perform()
        action.click(self.get_button_confirm_order()).perform()

    def input_sms_code(self, sms_code):
        action = ActionChains(self.driver)
        action.click(self.get_field_sms_code()).send_keys(sms_code).perform()

    def click_button_confirm_sms_code(self):
        self.get_button_confirm_sms_code().click()

    # Methods
    def check_error_message(self):
        assert self.get_error_message() == 'Сессия не инициализирована.', 'something went wrong'

    def input_credentials_and_confirm(self, telephone_number, email):
        self.input_telephone_number(telephone_number)
        self.input_email(email)
        self.click_button_confirm_order()
