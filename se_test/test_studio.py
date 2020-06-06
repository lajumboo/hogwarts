from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestStudio:
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_studio(self):
        # self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_link_text("热门").click()
        self.driver.find_element_by_link_text("分类").click()
