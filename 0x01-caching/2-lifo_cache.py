#!/usr/bin/env python3
"""module doc"""
from queue import LifoQueue
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache class """
    def __init__(self):
        """ intialize empty cache
        """
        super().__init__()
        self.stack = LifoQueue(maxsize=self.MAX_ITEMS)

    def put(self, key, item):
        """ put item in cache """
        if key is None or item is None:
            return

        if self.stack.full():
            old_key = self.stack.get()
            del self.cache_data[old_key]
            print("DISCARD: " + str(old_key))
        self.stack.put(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get item from chace """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
