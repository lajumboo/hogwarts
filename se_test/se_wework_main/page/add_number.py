from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AddNumber:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_number(self):
        self._driver.find_element(By.ID, 'username').send_keys("测试1")
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("test1")
        self._driver.find_element(
            By.ID, 'memberAdd_phone').send_keys("12345678901")
        self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        return True
