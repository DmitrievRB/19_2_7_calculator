import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_calc_multiply(self):
        assert self.calculator.multiply(self,2,2)==4

    def test_calc_division(self):
        assert self.calculator.division(self,2,2) == 1

    def test_calc_subtrction(self):
        assert self.calculator.subtrction(self,5.3) == 2

    def test_calc_add(self):
        assert self.calculator.add(self,2,2) == 4

    