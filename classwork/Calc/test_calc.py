import pytest
import yaml
from calc import Calc


class TestCalc:
    @pytest.mark.parametrize(("a", "b", "expect"), yaml.safe_load
                             (open("data/add_data.yml")))
    def test_add(self, a, b, expect):
        self.calc = Calc()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize(("a", "b", "expect"), yaml.safe_load
                             (open("data/div_data.yml")))
    def test_div(self, a, b, expect):
        self.calc = Calc()
        result = self.calc.div(a, b)
        assert result == expect
