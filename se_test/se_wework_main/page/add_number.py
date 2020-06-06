from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddNumber(BasePage):

    def add_number(self):
        self.find(By.ID, 'username').send_keys("测试1")
        self.find(By.ID, 'memberAdd_acctid').send_keys("test1")
        self.find(By.ID, 'memberAdd_phone').send_keys("12345678901")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return True

    def get_number(self):
        elements = self.finds(
            By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute("title") for element in elements]
