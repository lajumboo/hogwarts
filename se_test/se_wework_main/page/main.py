from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from page.add_number import AddNumber


class Main:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)  # 复用模式
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self._driver.maximize_window()
        self._driver.implicitly_wait(3)

    def goto_add_number(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddNumber(self._driver)
