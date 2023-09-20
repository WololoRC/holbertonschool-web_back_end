#!/usr/bin/python3
""" LIFO is amazing! """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ Put new staff on self.cache_items """
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                print(f"DISCARD: {self.last_key}")
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """ Get a specific item from self.cache_data """
        if key:
            return self.cache_data.get(key)
