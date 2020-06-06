import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    """三种等待方式：直接等待，隐式等待，显式等待"""
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        # self.driver.quit()
        pass

    def test_wait(self):
        self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        time.sleep(3)  # 直接等待

        # 显式等待
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable
            ((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(
            By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
