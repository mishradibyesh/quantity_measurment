"""
@author: Dibyesh Mishra
@date: 24-12-2021 00:12
"""
from custom_exception import UnitErrorException


class UnitConversion:
    '''
    Description:
        Converts the length from feet to inch
    Parameter:
        length(int): length in feet
    Return:
        length_inch(int): length in inch
    '''

    def __eq__(self, length):
        if length is None:
            return None
        elif length >= 0:
            length_in_inch = length*12
            return length_in_inch
        else:
            raise UnitErrorException("invalid")

    def feet_to_yard(self, length):
        '''
        Description:
            Converts the length from feet to yard
        Parameter:
            length(int): length in feet
        Return:
            length_yard(float): length in inch with 2 decimal precision
        '''

        if length == None:
            return None
        elif length >= 0:
            length_yard = length / 3
            return round(length_yard, 2)
        else:
            raise UnitErrorException("invalid")
