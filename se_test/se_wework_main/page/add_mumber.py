from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Addmumber(BasePage):

    def add_mumber(self):
        self.find(By.ID, 'username').send_keys("测试1")
        self.find(By.ID, 'memberAdd_acctid').send_keys("test1")
        self.find(By.ID, 'memberAdd_phone').send_keys("12345678901")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def search_mumber(self):
        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        self.find(By.ID, 'memberSearchInput').send_keys("测试1")
        search_name = self.find(
            By.CSS_SELECTOR, '.ww_searchResult_title_peopleName').text
        return search_name

    # def delete_mumber(self):
    #     self.find(By.CSS_SELECTOR, '.js_del_member').click()
    #     self.find(By.CSS_SELECTOR, '.ww_dialog_foot>a:nth-child(1)').click()
