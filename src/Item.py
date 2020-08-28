"""
Date: 09/24/2019
Class: CS5310
Assignment: Fractional Knapsack
Author(s): Zhongqiu Gao
Item class
"""


class Item:
    def __init__(self, weight, benefit, item_id):
        self.__weight = weight
        self.__benefit = benefit
        self.__amount = 0
        self.__item_id = item_id

    def get_amount(self):
        return self.__amount

    def get_weight(self):
        return self.__weight

    def get_benefit(self):
        return self.__benefit

    def set_amount(self, value):
        self.__amount = round(value * 1.0, 3)

    def get_value(self):
        return round(self.__benefit * 1.0 / self.__weight, 3)

    def get_id(self):
        return self.__item_id


