#!/usr/bin/python3
""" Task 0 """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A simple cache system Class """

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})

    def get(self, key):
        if key is None or key not in self.cache_data:
            pass
        else:
            return self.cache_data.get(key)
