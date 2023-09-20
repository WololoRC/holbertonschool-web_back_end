#!/usr/bin/python3
""" Task 0 """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache that inherits from BaseCaching and is a caching system
        This caching system doesn’t have limit.
     """

    def put(self, key, item):
        """ Put new data on Cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Return specific data from Cache """
        if key is None or key not in self.cache_data:
            pass
        else:
            return self.cache_data.get(key)
