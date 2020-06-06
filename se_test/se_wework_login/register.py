from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        self._driver.find_element(By.ID, 'corp_name').send_keys("test1")
        self._driver.find_element(By.ID, 'manager_name').send_keys("manager1")
        sleep(5)
        self._driver.quit()
        return True
