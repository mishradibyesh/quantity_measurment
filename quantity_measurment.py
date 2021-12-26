"""
@author: Dibyesh Mishra
@date: 24-12-2021 00:12
"""
from custom_exception import UnitErrorException


class UnitConversion:


    def feet_to_inch(self, length):
        if length is None:
            return None
        elif length >= 0:
            length_in_inch = length*12
            return length_in_inch
        else:
            raise UnitErrorException("invalid")