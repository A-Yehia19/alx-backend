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
            old_key = self.order[0]
            print("DISCARD: " + str(old_key))
            del self.cache_data[old_key]
            self.order.pop(0)

        if key in self.order:
            self.order.remove(key)

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get item from chace """
        if key is None or key not in self.cache_data.keys():
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
