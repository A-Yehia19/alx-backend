#!/usr/bin/env python3
"""module doc"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache class """
    def put(self, key, item):
        """ put item in cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get item from chace """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
