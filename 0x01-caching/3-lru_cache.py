#!/usr/bin/env python3
"""module doc"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache class """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ put item in cache """
        if key is None or item is None:
            return

        if len(self.order) == self.MAX_ITEMS and key not in self.order:
            print("DISCARD: " + str(self.order[0]))
            self.order.pop(0)

        try:
            self.order.remove(key)
        finally:
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get item from chace """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
