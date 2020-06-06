from time import sleep
from page.main import Main


class TestAddNumber:
    def setup(self):
        self.main = Main()

    def test_addnumber(self):
        add_number = self.main.goto_add_number()
        add_number.add_number()
        sleep(3)
        assert "测试1" in add_number.get_number()
