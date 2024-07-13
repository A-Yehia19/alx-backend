#!/usr/bin/env python3
"""module doc"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache class """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """ put item in cache """
        if key is None or item is None:
            return

        if key in self.freq.keys() or len(self.freq.keys()) < self.MAX_ITEMS:
            self.freq[key] = self.freq.get(key, 0) + 1
            self.cache_data[key] = item
        else:
            items = list(self.freq.items())
            min_key = items[0][0]
            min_val = items[0][1]

            for key, val in items:
                if val < min_val:
                    min_val = val
                    min_key = key

            del self.cache_data[min_key]
            del self.freq[min_key]

            self.freq[key] = 0
            self.cache_data[key] = item
            print("DISCARD: " + str(min_key))

    def get(self, key):
        """ get item from chace """
        if key is None or key not in self.cache_data.keys():
            return None
        self.freq[key] += 1
        return self.cache_data[key]
