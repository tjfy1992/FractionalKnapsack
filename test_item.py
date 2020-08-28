"""
Date: 09/30/2019
Class: CS5310
Assignment: Fractional Knapsack
Author(s): Zhongqiu Gao
test script for Item class
"""
from src.Item import Item

t_item = Item(4, 16, 1)


def test_item_instantiate():
    assert isinstance(t_item, Item)


def test_get_weight():
    assert t_item.get_weight() == 4


def test_get_benefit():
    assert t_item.get_benefit() == 16


def test_get_value():
    assert t_item.get_value() == t_item.get_benefit() * 1.0 / t_item.get_weight()


def test_get_id():
    assert t_item.get_id() == 1


def test_set_and_get_amount():
    t_item.set_amount(2.0)
    assert t_item.get_amount() == 2.0
