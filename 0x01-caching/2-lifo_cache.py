#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from queue import LifoQueue
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.stack = LifoQueue(maxsize=self.MAX_ITEMS)

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return

        if self.stack.full():
            old_key = self.stack.get()
            del self.cache_data[old_key]
            print("DISCARD: " + str(old_key))
        self.stack.put(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
