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
        return self.cache_data[key]


my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()