from page.main import Main


class TestAddmumber:
    def setup(self):
        self.main = Main()

    def test_addmumber(self):
        add_mumber = self.main.goto_add_mumber()
        add_mumber.add_mumber()
        assert "测试1" == add_mumber.search_mumber()