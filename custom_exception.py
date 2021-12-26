"""
@author: Dibyesh Mishra
@date: 24-12-2021 00:29
"""


class UnitErrorException(Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return self.message
