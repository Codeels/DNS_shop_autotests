from selenium.webdriver import ActionChains, Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    # кнопка с надписью "выбрать магазин"
    button_choose_shop0 = '//button[contains(@class, "base-checkout-getting-pickup__shop-change-btn")]'
    button_choose_shop1 = '//div[contains(@class,"checkout-getting__pickup")]/button'
    button_choose_shop2 = '//div[@class="shop-view__voblers-item shop-view__voblers-item_type_corporate"]/../../../..//button'

    field_telephone_number = '//input[@type="tel"]'
    field_email = '//input[@type="text"]'
    button_confirm_order = '//div[@class="apply-button checkout-container__apply"]//button'
    field_sms_code = '//div[contains(@class,"base-phone-confirm-code-check__input")]//input'
    button_confirm_sms_code = '//button[contains(@class, "base-phone-confirm-code-check__btn")]'
    error_message = '//div[@class="base-phone-confirm-code-check__error"]'

    # Getters
    def get_field_telephone_number(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.field_telephone_number)))

    def get_field_email(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.field_email)))

    def get_field_sms_code(self):
        return WebDriverWait(self.driver, 30).until(
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

    def get_button_choose_shop0(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_choose_shop0)))

    def get_button_choose_shop1(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_choose_shop1)))

    def get_button_choose_shop2(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_choose_shop2)))

    # Actions
    def input_telephone_number(self, telephone_number):
        action = ActionChains(self.driver)
        action.click(self.get_field_telephone_number()).send_keys(telephone_number).perform()

    def input_email(self, email):
        action = ActionChains(self.driver)
        self.get_field_email().click()
        action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.BACKSPACE).perform()
        action.send_keys(email).perform()

    def click_button_confirm_order(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_confirm_order()).perform()
        action.click(self.get_button_confirm_order()).perform()

    def input_sms_code(self, sms_code):
        action = ActionChains(self.driver)
        action.click(self.get_field_sms_code()).send_keys(sms_code).perform()

    def click_button_confirm_sms_code(self):
        self.get_button_confirm_sms_code().click()

    def click_button_choose_shop0(self):
        self.get_button_choose_shop0().click()

    def click_button_choose_shop1(self):
        self.get_button_choose_shop1().click()

    def click_button_choose_shop2(self):
        self.get_button_choose_shop2().click()

    # Methods
    def check_error_message(self):
        assert self.get_error_message() == 'Сессия не инициализирована.', 'something went wrong'
        return True

    def input_credentials_and_confirm(self, telephone_number, email):
        self.input_telephone_number(telephone_number)
        self.input_email(email)
        self.choose_shop()
        self.click_button_confirm_order()

    def choose_shop(self):
        if self.element_is_present('//button[contains(@class, "base-checkout-getting-pickup__shop-change-btn")]'):
            pass
        if self.element_is_present('//div[contains(@class,"checkout-getting__pickup")]/button'):
            self.click_button_choose_shop1()
            self.click_button_choose_shop2()
