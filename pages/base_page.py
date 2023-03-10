import datetime
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait_time = 15

    # Locators
    button_login_header_main = '//div[@class="header-bottom__user-menu"]'
    button_login_main = '//button[contains(@class, "base-ui-button-v2")]'
    button_login_checkout = '//a[@class="base-login-button__link_LYc"]/div[2]'
    button_enter_with_password = '//div[@class="block-other-login-methods__password-button"]'
    field_email = '//div[@class="form-entry-with-password__input"]//input'
    field_password = '//div[@class="form-entry-with-password__password"]//input'
    button_enter = '//div[@class="form-entry-with-password__main-button"]//button'

    button_cart = "//div[@class='cart-button']"

    button_compare = "//a[@class='compare-link-counter']"

    button_main = '//div[@id="header-logo"]'

    button_catalog = '//span[@class="header-bottom__catalog-spoiler"]'
    pc_parts = '//div[@class="header-menu-desktop__root"][6]'
    cpus = '//a[contains(@href, "/processory/")]'

    # Getters
    def get_button_login_header_main(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_login_header_main)))

    def get_button_login_main(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_login_main)))

    def get_button_login_checkout(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.button_login_checkout)))

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
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_button_compare(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_compare)))

    def get_button_main(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.button_main)))

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

    def click_button_login_header_main(self):
        self.get_button_login_header_main().click()

    def click_button_login_main(self):
        self.get_button_login_main().click()

    def click_button_login_checkout(self):
        self.get_button_login_checkout().click()

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

    def click_button_main(self):
        self.get_button_main().click()

    # ?????????? ?????? ?????????????????? ???????????? ?????????????? ????????????????
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"?????????????? ????????????????: {get_url}")

    # ?????????? ?????? ?????????????????? ??????????????????
    def get_screenshot(self):
        time.sleep(1)
        date = datetime.datetime.utcnow().strftime(" %Y-%m-%d %H.%M.%S")
        screenshot_name = f"Screenshot{date}.png"
        self.driver.save_screenshot(f"\\DNS_shop\\screens\\{screenshot_name}")

    # ?????????? ?????? ???????????????? ???????????? ???? ????????????????
    def confirm_url(self, url):
        get_url = self.driver.current_url
        assert get_url == url
        print("URL OK")

    def log_in(self, login, password, main=False, checkout=False):
        action = ActionChains(self.driver)
        # target = self.driver.find_element(By.XPATH, self.button_login_header)
        # action.move_to_element(target).perform()
        if main:
            action.move_to_element(self.get_button_login_header_main()).perform()
            # target = self.driver.find_element(By.XPATH, self.button_login)
            # action.move_to_element(target).click(target).perform()
            action.move_to_element(self.get_button_login_main()).click().perform()
        else:
            self.get_button_login_checkout().click()
        self.click_button_enter_with_password()
        self.input_field_email(login)
        self.input_field_password(password)
        time.sleep(1)
        self.click_button_enter()
        time.sleep(1)
        # self.driver.refresh()

    def go_to_cart(self):
        self.click_button_cart()

    def go_to_comparison_page(self):
        self.click_button_compare()

    def go_to_main_page(self):
        self.click_button_main()

    def check_name(self, name1, name2):
        assert name2 in name1, "Product names are not the same"
        return True

    def check_price(self, price1, price2):
        assert price1 == price2, "Product prices are not the same"
        return True

    def check_service_rating(self, service_rating1, service_rating2):
        assert service_rating1 == service_rating2, "Product service ratings are not the same"
        return True

    def check_links(self, link1, link2):
        assert link1 == link2, "Product links are not the same"
        return True

    def check_skus(self, sku1, sku2):
        assert sku1 == sku2, "Product skus are not the same"
        return True

    def element_is_present(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True

