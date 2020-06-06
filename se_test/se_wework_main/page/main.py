from time import sleep
from selenium.webdriver.common.by import By

from page.add_number import AddNumber
from page.base_page import BasePage


class Main(BasePage):
    _base_page = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_number(self):
        # self.find(
        #     By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)')
        #     .click()
        self.find(By.ID, 'menu_contacts').click()
        sleep(3)
        self.find(By.CSS_SELECTOR,
                  '.js_has_member>div:nth-child(1) .js_add_member').click()
        return AddNumber(self._driver)
