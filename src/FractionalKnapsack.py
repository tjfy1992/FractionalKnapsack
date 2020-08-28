"""
Date: 09/24/2019
The implementation of the fractional knapsack algorithm
"""
from src.PriorityQueue import PriorityQueue


class FractionalKnapsack:
    def __init__(self, items):
        max_weight_str = input("Please input the max weight：")
        self.max_weight = float(max_weight_str)
        self.queue = PriorityQueue()
        for item in items:
            self.queue.enqueue(item, item.get_value())
        self.total_weight = 0

    @staticmethod
    def min_value(a, b):
        if a > b:
            return b
        else:
            return a

    def knapsack_handler(self):
        return_list = []
        while self.total_weight < self.max_weight:
            item = self.queue.dequeue()
            item.set_amount(self.min_value(item.get_weight(), self.max_weight - self.total_weight))
            self.total_weight += + item.get_amount()
            return_list.append((item.get_amount(), item.get_id()))
        return return_list
