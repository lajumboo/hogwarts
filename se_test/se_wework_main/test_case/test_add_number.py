from page.main import Main


class TestAddNumber:
    def setup(self):
        self.main = Main()

    def test_addnumber(self):
        assert self.main.goto_add_number().add_number()
