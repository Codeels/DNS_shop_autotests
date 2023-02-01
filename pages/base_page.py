import datetime
import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait_time = 15

    # Locators
    button_login_header = '//div[@class="header-bottom__user-menu"]'
    button_login = '//button[contains(@class, "base-ui-button-v2")]'
    button_enter_with_password = '//div[@class="block-other-login-methods__password-button"]'
    field_email = '//div[@class="form-entry-with-password__input"]//input'
    field_password = '//div[@class="form-entry-with-password__password"]//input'
    button_enter = '//div[@class="form-entry-with-password__main-button"]//button'

    button_cart = "//div[@class='cart-button']"

    button_compare = "//a[@class='compare-link-counter']"

    button_catalog = '//span[@class="header-bottom__catalog-spoiler"]'
    pc_parts = '//div[@class="header-menu-desktop__root"][6]'
    cpus = '//a[contains(@href, "/processory/")]'

    # Getters
    def get_button_login_header(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.button_login_header)))

    def get_button_login(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, self.button_login)))

    def get_button_enter_with_password(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_enter_with_password)))

    def get_field_email(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.field_email)))

    def get_field_password(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.field_password)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_button_compare(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_compare)))

    def get_button_catalog(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_link_pc_parts(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.pc_parts)))

    def get_link_cpus(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.cpus)))

    # Actions

    def click_button_login_header(self):
        self.get_button_login_header().click()

    def click_button_login(self):
        self.get_button_login().click()

    def click_button_enter_with_password(self):
        self.get_button_enter_with_password().click()

    def input_field_email(self, login):
        self.get_field_email().send_keys(login)

    def input_field_password(self, password):
        self.get_field_password().send_keys(password)

    def click_button_enter(self):
        self.get_button_enter().click()

    def click_button_cart(self):
        self.get_button_cart().click()

    def click_button_compare(self):
        self.get_button_compare().click()

    # Метод для получения ссылки текущей страницы
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Текущая страница: {get_url}")

    # Метод для получения скриншота
    def get_screenshot(self):
        time.sleep(1)
        date = datetime.datetime.utcnow().strftime(" %Y-%m-%d %H.%M.%S")
        screenshot_name = f"Screenshot{date}.png"
        self.driver.save_screenshot(f"\\DNS_shop\\screens\\{screenshot_name}")

    # Метод для проверки ссылки на страницу
    def confirm_url(self, url):
        get_url = self.driver.current_url
        assert get_url == url
        print("URL OK")

    def log_in(self, login, password):
        action = ActionChains(self.driver)
        target = self.driver.find_element(By.XPATH, self.button_login_header)
        action.move_to_element(target).perform()
        # action.move_to_element(self.get_button_login_header()).perform()
        target = self.driver.find_element(By.XPATH, self.button_login)
        action.move_to_element(target).click(target).perform()
        # action.move_to_element(self.get_button_login()).click().perform()
        self.click_button_enter_with_password()
        self.input_field_email(login)
        self.input_field_password(password)
        self.click_button_enter()
        self.driver.refresh()

    def go_to_cart(self):
        self.click_button_cart()

    def go_to_comparison_page(self):
        self.click_button_compare()

# TODO надо ли сюда добавить assert для сравнения цен, названий и т.д. на разных страницах?

