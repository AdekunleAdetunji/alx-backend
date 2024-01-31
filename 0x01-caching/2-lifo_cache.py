#!/usr/bin/env python3
"""
This module contains the LIFOcache class that inherits from BaseCaching
"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """
    A class LIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Instance initializer
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        A method that assigns to the dictionary self.cache_data the item value
        for the key key

        Args:
            key: The key to hold the value
            value: The value to be stored in the dictionary

        Return: None
        """
        if key and item:
            if len(self.queue) == self.MAX_ITEMS:
                if key not in self.queue:
                    leftmost = self.queue.pop()
                    print("DISCARD: {}".format(leftmost))
                    del self.cache_data[leftmost]
                else:
                    self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        A method that return the value in self.cache_data linked to key

        Args:
            key: The key for the value to be retrieved

        Return: Value linked to key if key is not None
        """
        if key:
            return self.cache_data.get(key)
