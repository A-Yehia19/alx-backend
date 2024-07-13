#!/usr/bin/env python3
"""module doc"""
from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache class """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.queue = Queue(maxsize=self.MAX_ITEMS)

    def put(self, key, item):
        """ put item in cache """
        if key is None or item is None:
            return

        if self.queue.full():
            old_key = self.queue.get()
            del self.cache_data[old_key]
            print("DISCARD:" + str(old_key))
        self.queue.put(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get item from chace """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
