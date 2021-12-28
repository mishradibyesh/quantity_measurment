"""
@author: Dibyesh Mishra
@date: 24-12-2021 00:13
"""
import pytest
from quantity_measurment import UnitConversion
from custom_exception import UnitErrorException


class TestQuantity:
    @pytest.fixture()
    def unit(self):
        unit = UnitConversion()
        return unit

    def test_feet_to_inch_if_zero(self, unit):
        assert unit.__eq__(0) == 0

    def test_feet_to_inch_if_none(self, unit):
        assert unit.__eq__(None) is None

    @pytest.mark.parametrize("length", [2.0])
    def test_feet_to_inch_reference(self, unit,length):
        unit1 = UnitConversion()
        assert unit.__eq__(length) == unit1.__eq__(2)

    @pytest.mark.parametrize("length", [2])
    def test_feet_to_inch_type(self, unit,length):
        assert type(unit.__eq__(length)) == int

    @pytest.mark.parametrize("length", [-5])
    def test_feet_to_inch_if_exception(self, unit,length):
        with pytest.raises(UnitErrorException) as exception :
            result = unit.__eq__(length)
            assert exception.__str__() == "invalid"

    def test_feet_to_yard_if_none(self, unit):
        assert unit.feet_to_yard(None) is None

    def test_feet_to_yard_if_zero(self, unit):
        assert unit.feet_to_yard(0) == 0

    @pytest.mark.parametrize("length", [-5])
    def test_feet_to_yard_if_exception(self, unit, length):
        with pytest.raises(UnitErrorException) as exception:
            result = unit.feet_to_yard(length)
            assert exception.__str__() == "invalid"

