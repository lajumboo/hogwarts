from selenium.webdriver.common.by import By

from page.add_mumber import Addmumber
from page.base_page import BasePage


class Main(BasePage):
    _base_page = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_mumber(self):
        # self.find(By.CSS_SELECTOR,
        #           '.index_service_cnt_itemWrap:nth-child(1)').click()
        self.find(By.ID, 'menu_contacts').click()

        def wait_add_mumber(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, '#username'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member').click()
            return elements_len > 0

        self.wait_for_elem(wait_add_mumber)
        return Addmumber(self._driver)
