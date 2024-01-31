#!/usr/bin/env python3
"""
This module contains the BasicCache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Instance initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        A method that assigns to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything

        Args:
            key: The dictionary key
            item: The dictionary item

        Return: None
        """
        if key and item:
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
