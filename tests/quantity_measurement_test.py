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
        assert unit.feet_to_inch(0) == 0

    def test_feet_to_inch_if_none(self, unit):
        assert unit.feet_to_inch(None) is None

    def test_feet_to_inch_reference(self, unit):
        unit1 = UnitConversion()
        assert unit.feet_to_inch(2) == unit1.feet_to_inch(2)

    def test_feet_to_inch_type(self, unit):
        assert type(unit.feet_to_inch(2)) == int

    def test_feet_to_inch_if_exception(self, unit):
        with pytest.raises(UnitErrorException) as exception :
            result = unit.feet_to_inch(-5)
            assert exception.__str__() == "invalid"
