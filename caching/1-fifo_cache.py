#!/usr/bin/python3
""" FIFO is amazing! """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """  class FIFOCache that inherits from BaseCaching and is a caching system
         if lennght == MAX_ITEMS discard the first item os self.cache_data and
         print it.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put new data and discard if len(seld.cache_data) > 4 """
        if key is None or item is None:
            return

        else:
            self.cache_data.update({key: item})

        if len(self.cache_data) > self.MAX_ITEMS:
            rm_key = [item for item in self.cache_data.keys()]
            self.cache_data.pop(rm_key[0])
            print(f"DISCARD: {rm_key[0]}")

    def get(self, key):
        """ Get content of self.cache_data """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
