import time
import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_time = 15

    # Locators
    link_computer_parts = "//a//a[@href='/catalog/17aa522a16404e77/komplektuyushhie-dlya-pk/']"
    link_major_parts = "//a[@href='/catalog/88f4ff1d39dee00e/osnovnye-komplektuyushhie-dlya-pk/']"
    link_cpus = '//a[@href="/catalog/17a899cd16404e77/processory/"]'

    # Getters

    def get_computer_parts_link(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.link_computer_parts)))

    def get_major_parts_link(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.link_major_parts)))

    def get_link_cpus(self):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, self.link_cpus)))

    # Actions

    def click_computer_parts_link(self):
        self.get_computer_parts_link().click()
        print("Click")

    def click_major_parts_link(self):
        self.get_major_parts_link().click()

    def click_link_cpus(self):
        self.get_link_cpus().click()

    # Methods
    def go_to_cpus(self):
        with allure.step('Переход к странице с процессорами'):
            self.click_computer_parts_link()
            self.click_major_parts_link()
            self.click_link_cpus()
            time.sleep(2)
