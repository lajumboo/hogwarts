import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


class TestWechat:
    def setup(self):
        """
        1、关闭chrome浏览器
        2、执行命令:chrome --remote-debugging-port=9222
        """
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()  # 复用模式 options=options
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wechat(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()  # 复用模式保存cookie
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(5)
        db.close()
