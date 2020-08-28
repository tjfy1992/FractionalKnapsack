"""
Date: 09/24/2019
Class: CS5310
Assignment: Fractional Knapsack
Author(s): Zhongqiu Gao
The priority queue class
"""

import heapq
from src.Item import Item


class PriorityQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item: Item, priority):
        heapq.heappush(self.__queue, (-priority, -item.get_id(), item))

    def dequeue(self) -> Item:
        if len(self.__queue) == 0:
            return None
        # returns the item with largest value from the queue.
        return heapq.heappop(self.__queue)[-1]

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return self.size() == 0

    def first(self) -> Item:
        if len(self.__queue) == 0:
            return None
        return self.__queue[0][-1]
