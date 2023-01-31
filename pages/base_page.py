import datetime
import time


class BasePage():

    def __init__(self, driver):
        self.driver = driver

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