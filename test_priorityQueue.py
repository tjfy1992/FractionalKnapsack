"""
Date: 09/24/2019
Class: CS5310
Assignment: Fractional Knapsack
Author(s): Zhongqiu Gao
test script for priority queue
"""

from src.PriorityQueue import PriorityQueue
from src.Item import Item

priority_queue = PriorityQueue()


def test_instantiate():
    assert isinstance(priority_queue, PriorityQueue)


def test_enqueue():
    # weight = 4, benefit = 12, id = 1; value = 3
    item = Item(4, 12, 1)
    priority_queue.enqueue(item, item.get_value())
    # weight = 4, benefit = 16, id = 2; value = 4
    item = Item(4, 16, 2)
    priority_queue.enqueue(item, item.get_value())
    assert priority_queue.size() == 2
    item = priority_queue.first()
    assert item.get_id() == 2
    assert not priority_queue.is_empty()


def test_dequeue():
    item = priority_queue.dequeue()
    assert isinstance(item, Item)
    assert item.get_id() == 2
    assert priority_queue.size() == 1
    item = priority_queue.dequeue()
    assert item.get_id() == 1
    assert priority_queue.is_empty()


def test_multiple_operations():
    # weight = 4, benefit = 20, id = 1; value = 5
    item = Item(4, 20, 1)
    priority_queue.enqueue(item, item.get_value())

    # weight = 3, benefit = 12, id = 2; value = 4
    item = Item(3, 12, 2)
    priority_queue.enqueue(item, item.get_value())

    assert priority_queue.size() == 2
    assert priority_queue.dequeue().get_id() == 1
    assert priority_queue.first().get_id() == 2
    priority_queue.dequeue()
    assert priority_queue.is_empty()
    assert priority_queue.first() is None

